from http import HTTPStatus

import jwt
from flask import Flask

from ks.ks_api.key_service_api import key_service_api

import json
import unittest


__author__ = "paulq@cisco.com"
__maintainer__ = "Alena Lifar"
__email__ = "alifar@cisco.com"
__copyright__ = "Copyright(c) 2017, Cisco Systems, Inc."
__version__ = "0.4.1"
__status__ = "alpha"


class TestKeyServiceApi(unittest.TestCase):
    
    def test_get_asset_keys_info(self):
        key_info = {}
        self.key_service_api = self.key_service_api(key_info)
        self.assertEquals(self.key_service_api[0], True)
        self.assertEquals(self.key_service_api[1], {})
        
