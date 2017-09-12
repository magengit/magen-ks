
KS_CREATE_MULTI_KEY_JWT = '''{
  "assets": [
    {
      "asset": {
        "asset_id": "1"
      }
    },
    {
      "asset": {
        "asset_id": "2"
      }
    }
  ],
  "format" : "jwt",
  "ks_type" : "local"
}'''

KS_CREATE_MULTI_KEY_RESP_JSON = {
    "response": {
        "keys": [
            {
                "key": {
                    "algorithm": "AES256",
                    "asset_id": "1",
                    "iv": "dynamic iv",
                    "key": "dynamic key",
                    "key_id": "dynamic key_id",
                    "key_server": "local",
                    "state": "active",
                    "use": "asset encryption"
                }
            },
            {
                "key": {
                    "algorithm": "AES256",
                    "asset_id": "2",
                    "iv": "dynamic iv",
                    "key": "dynamic key",
                    "key_id": "dynamic key_id",
                    "key_server": "local",
                    "state": "active",
                    "use": "asset encryption"
                }
            }
        ]
    },
    "status": 200,
    "title": "create new keys"
}

KS_CREATE_SINGLE_KEY_JWT = '''{
      "asset": {
        "asset_id": "5"
      },
        "format" : "jwt",
      "ks_type" : "local"
}'''

KS_CREATE_SINGLE_KEY_RESP_JSON = {
    "response": {
        "algorithm": "AES256",
        "asset_id": "5",
        "iv": "dynamic iv",
        "key": "dynamic key",
        "key_id": "dynamic key_id",
        "key_server": "local",
        "state": "active",
        "use": "asset encryption"
    },
    "status": 200,
    "title": "create new key"
}

KS_GET_MULTI_KEY_RESP_JSON = {
    'response':
        {'keys':
             [{'key': {'key_id': 'dynamic key_id', 'algorithm': 'AES256',
                       'key_server': 'local', 'asset_id': '100', 'key': 'dynamic_key',
                       'ttl': 86400, 'iv': "dynamic iv", 'state': 'active'}}, {
                  'key': {'key_id': 'dynamic key_id', 'algorithm': 'AES256',
                          'key_server': 'local', 'asset_id': '200',
                          'key': 'dynamic iv', 'ttl': 86400,
                          'iv': "dynamic iv", 'state': 'active'}}]}, 'status': 200,
    'title': 'requested keying material'
}

KS_GET_SINGLE_KEY_RESP_JSON = {
  "response": {
    "key": {
      "algorithm": "AES256",
      "asset_id": "1000",
      "iv": "dynamic iv",
      "key": "dynamic key",
      "key_id": "dynamic key_id",
      "key_server": "local",
      "state": "active",
      "ttl": 86400
    }
  },
  "status": 200,
  "title": "key details"
}


KS_UPDATE_MULTI_KEY_JWT = {
  "keys": [
    {
      "key": {
        "key_id": "TEMP",
        "active" : 0
      }
    },
    {
      "key": {
        "key_id": "TEMP",
        "active" : 0
      }
    }
  ],
  "format" : "jwt"
}


KS_UPDATE_MULTI_KEY_REQ_JWT = {
  "keys": [
    {
      "key": {
        "key_id": "",
        "active" : 0
      }
    },
    {
      "key": {
        "key_id": "",
        "active" : 0
      }
    }
  ],
  "format" : "jwt"
}

KS_UPDATE_MULTI_KEY_RESP_JSON = {
 "response": {
    "keys": [
      {
        "key": {
          "CHANGEME": "state deactive"
        }
      },
      {
        "key": {
          "CHANGEME": "state deactive"
        }
      }
    ]
  },
  "status": 200,
  "title": "updated keys"
}


KS_UPDATE_SINGLE_KEY_REQ_JWT = {
      "key": {
        "key_id": "",
        "active" : 0
      },
  "format" : "jwt"
}

KS_UPDATE_SINGLE_KEY_JSON_RESP = {
  "response": {
    "CHANGEME": "state deactive"
  },
  "status": 200,
  "title": "updated key"
}


KS_GET_MULTI_KEY_INFO_RESP_JSON = {
  "response": {
    "keys": [
      {
        "algorithm": "AES256",
        "asset_id": "1",
        "iv": "dyanmic iv",
        "key_id": "CHANGEME",
        "key_server": "local",
        "state": "active",
        "use": "asset encryption"
      },
      {
        "algorithm": "AES256",
        "asset_id": "2",
        "iv": "dynamic iv'",
        "key_id": "ChANGEME",
        "key_server": "local",
        "state": "active",
        "use": "asset encryption"
      }
    ]
  },
  "status": 200,
  "title": "key details"
}


KS_GET_SINGLE_INFO_RESP_JSON = {
  "response": {
    "algorithm": "AES256",
    "asset_id": "5010",
    "iv": "b'dynamic iv",
    "key_id": "CHANGEME",
    "key_server": "local",
    "state": "active",
    "use": "asset encryption"
  },
  "status": 200,
  "title": "key details"
}


DEL_MULTI_KEY_JSON_RESP = {
  "response": {
    "keys": [
      {
        "key": {
          "CHANGEME": "state --> deleted"
        }
      },
      {
        "key": {
          "CHANGEME": "state --> deleted"
        }
      }
    ]
  },
  "status": 200,
  "title": "delete keys"
}

DEL_SINGLE_KEY_JSON_RESP = {
  "response": {
    "CHANGEME": "state --> deleted"
  },
  "status": 200,
  "title": "delete key"

}

GET_TEST_SETUP_MULTI_JWT = '''{
  "assets": [
    {
      "asset": {
        "asset_id": "100"
      }
    },
    {
      "asset": {
        "asset_id": "200"
      }
    }
  ],
  "format" : "jwt",
  "ks_type" : "local"
}'''

GET_TEST_SETUP_SINGLE_JWT = '''{
      "asset": {
        "asset_id": "1000"
      },
        "format" : "jwt",
      "ks_type" : "local"
}'''

UPDATE_MULTI_KEY_SETUP_JWT = '''{
  "assets": [
    {
      "asset": {
        "asset_id": "123"
      }
    },
    {
      "asset": {
        "asset_id": "456"
      }
    }
  ],
  "format" : "jwt",
  "ks_type" : "local"
}'''

UPDATE_SINGLE_KEY_SETUP = '''{
      "asset": {
        "asset_id": "501"
      },
        "format" : "json",
      "ks_type" : "local"
}'''

KS_GET_MULTI_KEY_SETUP = '''{
  "assets": [
    {
      "asset": {
        "asset_id": "1"
      }
    },
    {
      "asset": {
        "asset_id": "2"
      }
    }
  ],
  "format" : "json",
  "ks_type" : "local"
}'''


KS_GET_SINGLE_KEY_SETUP = '''{
      "asset": {
        "asset_id": "5010"
      },
        "format" : "json",
      "ks_type" : "local"
}'''


DEL_TEST_SETUP_MULTI = '''{
  "assets": [
    {
      "asset": {
        "asset_id": "1230"
      }
    },
    {
      "asset": {
        "asset_id": "4567"
      }
    }
  ],
  "format" : "json",
  "ks_type" : "local"
}'''


UPDATE_MULTI_KEY_SETUP = '''{
  "assets": [
    {
      "asset": {
        "asset_id": "123"
      }
    },
    {
      "asset": {
        "asset_id": "456"
      }
    }
  ],
  "format" : "json",
  "ks_type" : "local"
}'''

KS_DEL_SINGLE_KEY_SETUP = '''{
      "asset": {
        "asset_id": "50100"
      },
        "format" : "json",
      "ks_type" : "local"
}'''