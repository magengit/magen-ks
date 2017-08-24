NAME = "bob"

KS_CREATE_MULTI_KEY_JSON = '''{
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
  "ks_type" : "awskms"
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
                    "key_server": "awskms",
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
                    "key_server": "awskms",
                    "state": "active",
                    "use": "asset encryption"
                }
            }
        ]
    },
    "status": 200,
    "title": "create new keys"
}

KS_CREATE_SINGLE_KEY_JSON = '''{
      "asset": {
        "asset_id": "5"
      },
        "format" : "json",
      "ks_type" : "local"
}'''

KS_CREATE_SINGLE_KEY_JSON_RESP = {
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

KS_GET_MULTI_KEY_JSON_RESP = {
    'response':
        {'keys':
             [{'key': {'key_id': 'dynamic key_id', 'algorithm': 'AES256',
                       'key_server': 'awskms', 'asset_id': '100', 'key': 'dynamic_key',
                       'ttl': 86400, 'iv': "dynamic iv", 'state': 'active'}}, {
                  'key': {'key_id': 'dynamic key_id', 'algorithm': 'AES256',
                          'key_server': 'awskms', 'asset_id': '200',
                          'key': 'dynamic iv', 'ttl': 86400,
                          'iv': "dynamic iv", 'state': 'active'}}]}, 'status': 200,
    'title': 'requested keying material'
}

KS_GET_SINGLE_KEY_JSON_RESP = {
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


KS_UPDATE_MULTI_KEY_JSON = {
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
  "format" : "json"
}


KS_UPDATE_MULTI_KEY_JSON_REQ = {
  "keys": [
    {
      "key": {
        "key_id": "",
        "active": 0
      }
    },
    {
      "key": {
        "key_id": "",
        "active": 0
      }
    }
  ],
  "format": "json"
}

KS_UPDATE_MULTI_KEY_JSON_RESP = {
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


KS_UPDATE_SINGLE_KEY_JSON_REQ = {
      "key": {
        "key_id": "",
        "active" : 0
      },
  "format" : "json"
}

KS_UPDATE_SINGLE_KEY_JSON_RESP = {
  "response": {
    "CHANGEME": "state deactive"
  },
  "status": 200,
  "title": "updated key"
}



KS_GET_MULTI_KEY_INFO_JSON_RESP = {
  "response": {
    "keys": [
      {
        "algorithm": "AES256",
        "asset_id": "1",
        "iv": "dyanmic iv",
        "key_id": "CHANGEME",
        "key_server": "awskms",
        "state": "active",
        "use": "asset encryption"
      },
      {
        "algorithm": "AES256",
        "asset_id": "2",
        "iv": "dynamic iv'",
        "key_id": "ChANGEME",
        "key_server": "awskms",
        "state": "active",
        "use": "asset encryption"
      }
    ]
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


KS_GET_SINGLE_INFO_JSON_RESP = {
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




# KS_UPDATE_SINGLE_KEY_JSON

# KS_DEL_MULTI_KEY_JSON

# KS_DEL_SINGLE_KEY_JSON

# KS_INFO_MULTI_KEY_JSON

# KS_INFO_SINGLE_KEY_JSON



GET_TEST_SETUP_MULTI_JSON = '''{
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
  "format" : "json",
  "ks_type" : "awskms"
}'''

GET_TEST_SETUP_SINGLE_JSON = '''{
      "asset": {
        "asset_id": "1000"
      },
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
  "ks_type" : "awskms"
}'''

UPDATE_SINGLE_KEY_SETUP = '''{
      "asset": {
        "asset_id": "501"
      },
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
  "ks_type" : "awskms"
}'''



KS_DEL_MULTI_KEY_SETUP = '''{
    "assets": [
    {
      "asset": {
        "asset_id": "90"
      }
    },
    {
      "asset": {
        "asset_id": "80"
      }
    }
  ],
  "format" : "json",
  "ks_type" : "awskms"
}'''


KS_DEL_SINGLE_KEY_SETUP = '''{
      "asset": {
        "asset_id": "50100"
      },
        "format" : "json",
      "ks_type" : "local"
}'''