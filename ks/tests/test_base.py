from http import HTTPStatus

import jwt
from flask import Flask
from magen_rest_apis.server_urls import ServerUrls

from ks.ks_server.key_server_api import key_service_bp, key_service_bp_v3

from ks.settings import mongo_settings
import json
import unittest

from magen_rest_apis.rest_client_apis import RestClientApis
# from magen_test_utils_apis.test_magen_object_apis import TestMagenObjectApis
from magen_utils_apis.compare_utils import compare_dicts
from magen_utils_apis.domain_resolver import mongo_host_port

__author__ = "paulq@cisco.com"
__maintainer__ = "Alena Lifar"
__email__ = "alifar@cisco.com"
__copyright__ = "Copyright(c) 2017, Cisco Systems, Inc."
__version__ = "0.4.1"
__status__ = "alpha"


def update_key_ids(obj, key_ids: list):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "key_id":
                obj['key_id'] = key_ids.pop(0)
            elif isinstance(v, dict):
                update_key_ids(v, key_ids)
            elif isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        update_key_ids(i, key_ids)
        return obj
    else:
        return "not a dict"


def update_reply(obj, key_ids: list):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "CHANGEME":
                keyidv = key_ids.pop(0)
                obj[keyidv] = obj["CHANGEME"]
                del obj["CHANGEME"]
            elif isinstance(v, dict):
                update_reply(v, key_ids)
            elif isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        update_reply(i, key_ids)
        return obj
    else:
        return "not a dict"


def update_reply_value(obj, key_ids: list):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v == "CHANGEME":
                obj[k] = key_ids.pop(0)
            elif isinstance(v, dict):
                update_reply_value(v, key_ids)
            elif isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        update_reply_value(i, key_ids)
        return obj
    else:
        return "not a dict"


def collect_ids(data: dict):
    data_list = data['response'].get('keys', None) or data['response']
    return [key_data['key']['key_id'] for key_data in data_list if isinstance(key_data, dict)] or [data_list['key_id']]


def decode_jwt(payload):
    clear = jwt.decode(payload, 'secret')
    return clear


class KsTest(unittest.TestCase):
    mongo = None

    @classmethod
    def setUpClass(cls):
        print()
        print("Searching for correct Mongo server")

        mongo_server_ip, mongo_port = mongo_host_port()

        print("Setting up Mongo DB")
        cls.mongo = mongo_settings.MongoSettings(mongo_server_ip, mongo_port)
        cls.server_urls = ServerUrls()
        cls.key_server_asset_url = cls.server_urls.key_server_asset_url
        cls.key_server_assets_url = cls.server_urls.key_server_assets_url
        cls.key_server_asset_keys_keys_url = cls.server_urls.key_server_asset_keys_keys_url
        cls.key_server_asset_keys_keys_key_url = cls.server_urls.key_server_asset_keys_keys_key_url

    def setUp(self):
        """
            Setting up a Test Flask App for Unittests
            Without establishing actual network connection.
        """
        print()
        print("CLEAN UP BEFORE TEST")
        type(self).mongo.drop_db()
        print("Starting Test Client")
        magen = Flask(__name__)
        magen.config['TESTING'] = True
        magen.register_blueprint(key_service_bp)
        magen.register_blueprint(key_service_bp_v3, url_prefix='/magen/ks/v3')
        self.app = magen.test_client()

    def tearDown(self):
        print()
        print("CLEAN UP AFTER TEST")
        type(self).mongo.drop_db()

    # def compare_dicts(self, test_data: dict, expected_data: dict):
    #     self.assertTrue(TestMagenObjectApis.compare_json(expected_data, test_data)[0])

    def check_helper(self, test_response_obj, compare_data):
        self.assertEquals(test_response_obj.status_code, HTTPStatus.OK)
        test_data = json.loads(test_response_obj.data.decode("utf-8"))
        # decoding if key format is jwt
        test_data['response'] = decode_jwt(test_data['response']) \
            if isinstance(test_data['response'], str) \
            else test_data['response']
        if compare_data:
            compare_dicts(test_data, compare_data)
        return test_data

    def post_helper(self, url_str, test_data, compare_data=None):
        post_response_obj = self.app.post(
            url_str,
            data=test_data,
            headers=RestClientApis.put_json_headers
        )
        post_data = self.check_helper(post_response_obj, compare_data)
        return collect_ids(post_data) if not compare_data else None

    def get_helper(self, url_str, compare_data=None):
        get_response_obj = self.app.get(url_str)
        get_data = self.check_helper(get_response_obj, compare_data)
        return get_data if not compare_data else None

    def put_helper(self, url_str, test_data, compare_data=None):
        put_response_obj = self.app.put(
            url_str,
            data=test_data,
            headers=RestClientApis.put_json_headers
        )
        put_data = self.check_helper(put_response_obj, compare_data)
        return put_data if not compare_data else None

    def delete_helper(self, url_str, compare_data=None):
        delete_response_obj = self.app.delete(url_str)
        delete_data = self.check_helper(delete_response_obj, compare_data)
        return delete_data if not compare_data else None
