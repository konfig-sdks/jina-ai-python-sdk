# coding: utf-8

"""
    The Jina Embedding Serving API

    This is the UniversalAPI to access all the Jina embedding models

    The version of the OpenAPI document: 0.0.86
    Generated by: https://konfigthis.com
"""

from jina_ai_python_sdk.paths.v1_multi_embeddings.post import GenerateEmbeddings
from jina_ai_python_sdk.apis.tags.multi_embeddings_api_raw import MultiEmbeddingsApiRaw


class MultiEmbeddingsApi(
    GenerateEmbeddings,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MultiEmbeddingsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MultiEmbeddingsApiRaw(api_client)
