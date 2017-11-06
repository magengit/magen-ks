#! /usr/bin/python3.6

import ks.ks_server.ks_server as ks_server
import json
import unittest
from ks.tests.ks_rest_test_messages import *
from ks.tests.test_base import KsTest, update_key_ids, update_reply, update_reply_value

__author__ = "paulq@cisco.com"
__maintainer__ = "Alena Lifar"
__email__ = "alifar@cisco.com"
__copyright__ = "Copyright(c) 2017, Cisco Systems, Inc."
__version__ = "0.4.1"
__status__ = "alpha"


class KsRestTest(KsTest):
    """
    JSON format keys tests
    """

    def test_KeyServerMain(self):
        """
        Testing ks Main

        :return: void
        """
        ks_server.main(["--unittest"])

    def test_clean_test(self):
        """
        Testing System Clean Up

        :return: void
        """
        print()
        print("TEST CLEANING UP SYSTEM")
        test_response_obj = self.app.get(type(self).server_urls.key_server_base_url + 'ks/reset/')
        data_str = test_response_obj.data.decode("utf-8")  # decoding bytes to str
        expected_str = 'ks reset\n'
        self.assertEqual(expected_str, data_str)

    def test_multi_keygen(self):
        """
        Testing Multiple Key Generation

        :return: void
        """
        print()
        print("TESTING MUTIPLE KEY GENERATION")

        self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=KS_CREATE_MULTI_KEY_JSON,
            compare_data=KS_CREATE_MULTI_KEY_RESP_JSON
        )

    def test_single_keygen(self):
        """
        Testing Single Key Generation

        :return: void
        """
        print()
        print("TESTING SINGLE KEY GENERATION")

        self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=KS_CREATE_SINGLE_KEY_JSON,
            compare_data=KS_CREATE_SINGLE_KEY_JSON_RESP
        )

    def test_get_multikeys(self):
        """
        Testing Multiple Key Get

        :return: void
        """
        print()
        print("TESTING MUTIPLE KEY GET")

        self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=GET_TEST_SETUP_MULTI_JSON
        )
        self.get_helper(
            url_str=type(self).key_server_assets_url + '?asset_id=100&asset_id=200',
            compare_data=KS_GET_MULTI_KEY_JSON_RESP
        )

    def test_get_single_key(self):
        """
        Testing Single Key Get

        :return: void
        """
        print()
        print("TESTING SINGLE KEY GET")
        self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=GET_TEST_SETUP_SINGLE_JSON
        )
        self.get_helper(
            url_str=type(self).key_server_asset_url + '1000/',
            compare_data=KS_GET_SINGLE_KEY_JSON_RESP
        )

    def test_multi_key_update(self):
        """
        Testing Multiple Key Update

        :return: void
        """
        print()
        print("TESTING MULTIPLE KEY UPDATE")
        key_ids = self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=UPDATE_MULTI_KEY_SETUP
        )
        key_ids2 = key_ids.copy()

        updated_dict = json.dumps(update_key_ids(KS_UPDATE_MULTI_KEY_JSON_REQ, key_ids))
        updated_with_key_ids = update_reply(KS_UPDATE_MULTI_KEY_JSON_RESP, key_ids2)
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
        print()
        print("TESTING SINGLE KEY UPDATE")
        key_ids = self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=UPDATE_SINGLE_KEY_SETUP
        )
        key_ids2 = key_ids.copy()

        updated_dict = json.dumps(update_key_ids(KS_UPDATE_SINGLE_KEY_JSON_REQ, key_ids))
        updated_with_key_ids = update_reply(KS_UPDATE_SINGLE_KEY_JSON_RESP, key_ids2)
        self.put_helper(
            url_str=type(self).key_server_asset_keys_keys_key_url,
            test_data=updated_dict,
            compare_data=updated_with_key_ids
        )

    def test_get_multi_key_info(self):
        """
        Testing Getting Multiple Key Info

        :return: void
        """
        print()
        print("TESTING GETTING MULTIPLE KEY INFO")
        key_ids = self.post_helper(
            url_str=type(self).key_server_assets_url,
            test_data=KS_GET_MULTI_KEY_SETUP
        )

        get_url_str = type(self).key_server_asset_keys_keys_url + '?key_id=' + key_ids[0] + '&key_id=' + key_ids[1]
        updated_with_key_ids = update_reply_value(KS_GET_MULTI_KEY_INFO_JSON_RESP, key_ids)  # empties key_ids list
        self.get_helper(
            url_str=get_url_str,
            compare_data=updated_with_key_ids
        )

    def test_get_single_key_info(self):
        """
        Testing Getting Single Key Info

        :return: void
        """
        print()
        print("TESTING GETTING SINGLE KEY INFO")
        key_ids = self.post_helper(
            url_str=type(self).key_server_asset_url,
            test_data=KS_GET_SINGLE_KEY_SETUP
        )

        get_url_str = type(self).key_server_asset_keys_keys_key_url + key_ids[0] + '/'
        updated_with_key_ids = update_reply_value(KS_GET_SINGLE_INFO_JSON_RESP, key_ids)
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
            test_data=KS_DEL_MULTI_KEY_SETUP
        )

        delete_url_str = type(self).key_server_asset_keys_keys_url + '?key_id=' + key_ids[0] + '&key_id=' + key_ids[1]
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

        delete_url_str = type(self).key_server_asset_keys_keys_key_url + key_ids[0] + '/'
        updated_with_key_ids = update_reply(DEL_SINGLE_KEY_JSON_RESP, key_ids)
        self.delete_helper(
            url_str=delete_url_str,
            compare_data=updated_with_key_ids
        )


if __name__ == '__main__':
    unittest.main()
