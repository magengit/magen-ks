#! /usr/bin/python3.5

import json
import unittest
from ks.tests.test_base import KsTest, update_key_ids, update_reply, update_reply_value
from ks.tests.ks_rest_test_jwt_messages import *

__author__ = "paulq@cisco.com"
__maintainer__ = "Alena Lifar"
__email__ = "alifar@cisco.com"
__copyright__ = "Copyright(c) 2017, Cisco Systems, Inc."
__version__ = "0.4.1"
__status__ = "alpha"


class KsRestTest(KsTest):
    """
    JWT format keys tests
    """

    def test_multi_keygen(self):
        """
        Testing Multiple Key Generation

        :return: void
        """
        print("TESTING MULTIPLE KEY GENERATION")
        self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=KS_CREATE_MULTI_KEY_JWT,
            compare_data=KS_CREATE_MULTI_KEY_RESP_JSON
        )

    def test_single_keygen(self):
        """
        Testing Single Key Generation

        :return: void
        """
        print("TESTING SINGLE KEY GENERATION")
        self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=KS_CREATE_SINGLE_KEY_JWT,
            compare_data=KS_CREATE_SINGLE_KEY_RESP_JSON
        )

    def test_get_multikeys(self):
        """
        Testing Multiple Key Get

        :return: void
        """
        print("TESTING MUTIPLE KEY GET")
        self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=GET_TEST_SETUP_MULTI_JWT
        )
        self.get_helper(
            url_str=type(self).key_server_assets_url + '?asset_id=100&asset_id=200&format=jwt',
            compare_data=KS_GET_MULTI_KEY_RESP_JSON
        )

    def test_get_singlekey(self):
        """
        Testing Single Key Get

        :return: void
        """
        print("TESTING SINGLE KEY GET")
        self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=GET_TEST_SETUP_SINGLE_JWT
        )
        self.get_helper(
            url_str=type(self).key_server_asset_url + '1000/?format=jwt',
            compare_data=KS_GET_SINGLE_KEY_RESP_JSON
        )

    def test_multi_key_update(self):
        """
        Testing Multiple Key Update

        :return: void
        """
        print("TESTING MULTIPLE KEY UPDATE")
        key_ids = self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=UPDATE_MULTI_KEY_SETUP
        )
        key_ids2 = key_ids.copy()

        updated_dict = json.dumps(update_key_ids(KS_UPDATE_MULTI_KEY_REQ_JWT, key_ids))
        updated_with_key_ids = update_reply(KS_UPDATE_MULTI_KEY_RESP_JSON, key_ids2)
        self.put_helper(
            url_str=type(self).key_server_asset_keys_keys_url,
            test_data=updated_dict,
            compare_data=updated_with_key_ids
        )

    def test_single_key_update(self):
        """
        Testing Single Key Update

        :return: void
        """
        print("TESTING SINGLE KEY UPDATE")
        key_ids = self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=UPDATE_SINGLE_KEY_SETUP,
        )
        key_ids2 = key_ids.copy()

        updated_dict = json.dumps(update_key_ids(KS_UPDATE_SINGLE_KEY_REQ_JWT, key_ids))
        updated_with_keyids = update_reply(KS_UPDATE_SINGLE_KEY_JSON_RESP, key_ids2)
        self.put_helper(
            url_str=type(self).key_server_asset_keys_keys_key_url,
            test_data=updated_dict,
            compare_data=updated_with_keyids
        )

    def test_get_multi_key_info(self):
        """
        Testing Getting Multiple Key Info

        :return: void
        """
        print("TESTING GETTING MULTIPLE KEY INFO")
        key_ids = self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=KS_GET_MULTI_KEY_SETUP
        )

        get_url_str = type(self).key_server_asset_keys_keys_url + '?key_id=' + key_ids[0] + '&key_id=' + key_ids[1] + '&format=jwt'
        updated_with_key_ids = update_reply_value(KS_GET_MULTI_KEY_INFO_RESP_JSON, key_ids)
        self.get_helper(
            url_str=get_url_str,
            compare_data=updated_with_key_ids
        )

    def test_get_single_key_info(self):
        """
        Testing Getting Single Key Info

        :return: void
        """
        print("TESTING GETTING SINGLE KEY INFO")
        key_ids = self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=KS_GET_SINGLE_KEY_SETUP
        )

        get_url_str = type(self).key_server_asset_keys_keys_key_url + key_ids[0] + '/?format=jwt'
        updated_with_key_ids = update_reply_value(KS_GET_SINGLE_INFO_RESP_JSON, key_ids)
        self.get_helper(
            url_str=get_url_str,
            compare_data=updated_with_key_ids
        )

    def test_del_multikey(self):
        """
        Testing Multiple Key Delete

        :return: void
        """
        print()
        print("TESTING MULTI KEY DELETE")
        key_ids = self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=DEL_TEST_SETUP_MULTI
        )

        delete_url_str = type(self).key_server_asset_keys_keys_url + '?key_id=' + key_ids[0] + '&key_id=' + key_ids[1] + '&format=jwt'
        updated_with_key_ids = update_reply(DEL_MULTI_KEY_JSON_RESP, key_ids)
        self.delete_helper(
            url_str=delete_url_str,
            compare_data=updated_with_key_ids
        )

    def test_del_singlekey(self):
        """
        Testing Single Key Delete

        :return: void
        """
        print()
        print("TESTING SINGLE KEY DELETE")
        key_ids = self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=KS_DEL_SINGLE_KEY_SETUP
        )

        delete_url_str = type(self).key_server_asset_keys_keys_key_url + key_ids[0] + '/?format=jwt'
        updated_with_keyids = update_reply(DEL_SINGLE_KEY_JSON_RESP, key_ids)
        self.delete_helper(
            url_str=delete_url_str,
            compare_data=updated_with_keyids
        )


if __name__ == '__main__':
    unittest.main()
