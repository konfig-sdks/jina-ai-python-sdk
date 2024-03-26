# coding: utf-8

"""
    The Jina Embedding Serving API

    This is the UniversalAPI to access all the Jina embedding models

    The version of the OpenAPI document: 0.0.86
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from jina_ai_python_sdk.type.api_schemas_embedding_text_doc import ApiSchemasEmbeddingTextDoc

class RequiredApiSchemasEmbeddingTextEmbeddingInput(TypedDict):
    # The identifier of the model.  Available models and corresponding param size and dimension: - `jina-embedding-t-en-v1`, 14m, 312 - `jina-embedding-s-en-v1`, 35m, 512 (default) - `jina-embedding-b-en-v1`, 110m, 768 - `jina-embedding-l-en-v1`, 330, 1024  For more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224). 
    model: str

    # List of texts to embed
    input: typing.Union[typing.List[str], str, typing.List[ApiSchemasEmbeddingTextDoc], ApiSchemasEmbeddingTextDoc]

class OptionalApiSchemasEmbeddingTextEmbeddingInput(TypedDict, total=False):
    # The format in which you want the embeddings to be returned.Possible value are `float` and `base64`. Defaults to `float`
    encoding_format: str

class ApiSchemasEmbeddingTextEmbeddingInput(RequiredApiSchemasEmbeddingTextEmbeddingInput, OptionalApiSchemasEmbeddingTextEmbeddingInput):
    pass
