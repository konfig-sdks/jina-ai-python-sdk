# coding: utf-8

"""
    The Jina Embedding Serving API

    This is the UniversalAPI to access all the Jina embedding models

    The version of the OpenAPI document: 0.0.86
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from jina_ai_python_sdk import JinaAi

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        jinaai = JinaAi(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(jinaai)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
