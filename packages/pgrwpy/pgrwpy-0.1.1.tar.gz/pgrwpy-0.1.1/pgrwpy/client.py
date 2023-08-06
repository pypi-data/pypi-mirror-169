import hmac
import hashlib
import base64
import json
import requests
import uuid
import datetime

import pkg_resources
from pkg_resources import DistributionNotFound

from types import ModuleType
from .constants import URL, HTTP_STATUS_CODE

from . import resources


def capitalize_camel_case(string):
    return "".join(map(str.capitalize, string.split('_')))


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and \
            capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[capitalize_camel_case(name)] = module.__dict__[
            capitalize_camel_case(name)]


class Client:
    """PayPay client class"""
    DEFAULTS = {
        'sandbox_base_url': URL.SANDBOX_BASE_URL,
        'production_base_url': URL.PRODUCTION_BASE_URL
    }

    def __init__(self,
                 session=None,
                 auth=None,
                 production_mode=False,
                 **options):
        """
        Initialize a Client object with session,
        optional auth handler, and options
        """
        self.session = session or requests.Session()
        self.token_res = {}
        self.token_current_time = None
        self.auth = auth
        self.production_mode = production_mode

        self.base_url = self._set_base_url(**options)
        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def get_version(self):
        version = ""
        try:
            version = pkg_resources.require("pgrwpy")[0].version
        except DistributionNotFound:
            print('DistributionNotFound')
        return version

    def _set_base_url(self, **options):
        if self.production_mode is False:
            base_url = self.DEFAULTS['sandbox_base_url']
        if self.production_mode is True:
            base_url = self.DEFAULTS['production_base_url']
        if 'base_url' in options:
            base_url = options['base_url']
            del (options['base_url'])
        return base_url

    def _check_token_exists(self):
        """ 
        Verify that the token response exists to avoid repeat calls within 59 seconds
        """
        if isinstance(self.token_current_time, datetime.datetime) and isinstance(self.token_res, dict) and 'token' in self.token_res:
            time_calculate = datetime.datetime.now() - self.token_current_time
            if time_calculate.total_seconds() < 59:
                return True
        return False

    def auth_header(self, userID, secretKey):
        if not userID or not secretKey:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for userID and secretKey")
        if self._check_token_exists():
            return self.token_res
        payload = {
            "userID": userID,
            "secretKey": secretKey
        }
        url = self.base_url + URL.TOKEN
        try:
            response, status_code = self.request("post",
                                                 url,
                                                 data=json.dumps(payload),
                                                 auth_token=None)
        except Exception as e:
            raise ValueError("\x1b[31m ERROR REQUEST")

        if (not response or status_code < 200 or status_code >= 400):
            response_dict = json.loads(response)
            raise ValueError("\x1b[31m ERROR REQUEST",
                             response_dict.get('error', ''))

        self.token_current_time = datetime.datetime.now()
        self.token_res = json.loads(response)
        return json.loads(response)

    def request(self, method, path, auth_token, **options):
        """
        Dispatches a request to the PayPay HTTP API
        """
        api_name = options['api_id']
        del options['api_id']
        url = "{}{}".format(self.base_url, path)
        response = getattr(self.session, method)(url, headers={
            'Authorization': 'Bearer ' + auth_token["token"],
            'Content-Type': 'application/json;charset=UTF-8'
        }, **options)
        if ((response.status_code >= HTTP_STATUS_CODE.OK) and
                (response.status_code < HTTP_STATUS_CODE.REDIRECT)):
            return response.json()
        else:
            json_response = response.json()
            resolve_url = "{}?api_name={}&code={}&code_id={}".format(
                URL.RESOLVE,
                api_name,
                json_response['resultInfo']['code'],
                json_response['resultInfo']['codeId'])
            print("This link should help you to troubleshoot the error: " + resolve_url)
            return json_response

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        method = "GET"
        data, auth_header = self._update_request(None, path, method)
        return self.request("get",
                            path,
                            params=params,
                            auth_token=auth_header,
                            **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        method = "POST"
        data, auth_header = self._update_request(data, path, method)
        return self.request("post",
                            path,
                            data=data,
                            auth_token=auth_header,
                            **options)

    def patch(self, path, data, **options):
        """
        Parses PATCH request options and dispatches a request
        """
        method = "PATCH"
        data, auth_header = self._update_request(data, path, method)
        return self.request("patch",
                            path,
                            auth_token=auth_header,
                            **options)

    def delete(self, path, data, **options):
        """
        Parses DELETE request options and dispatches a request
        """
        method = "DELETE"
        data, auth_header = self._update_request(data, path, method)
        return self.request("delete",
                            path,
                            data=data,
                            auth_token=auth_header,
                            **options)

    def put(self, path, data, **options):
        """
        Parses PUT request options and dispatches a request
        """
        method = "PUT"
        data, auth_header = self._update_request(data, path, method)
        return self.request("put",
                            path,
                            data=data,
                            auth_token=auth_header,
                            **options)

    def _update_request(self, data, path, method):
        """
        Updates The resource data and header options
        """
        _data = None
        content_type = "empty"
        if data is not None:
            _data = json.dumps(data)
            content_type = "application/json;charset=UTF-8"
        uri_path = path
        _auth_header = self.auth_header(
            self.auth[0],
            self.auth[1],
            method,
            uri_path,
            content_type,
            _data)
        return _data, _auth_header
