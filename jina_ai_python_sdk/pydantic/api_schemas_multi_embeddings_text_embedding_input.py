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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from jina_ai_python_sdk.pydantic.api_schemas_embedding_text_doc import ApiSchemasEmbeddingTextDoc

class ApiSchemasMultiEmbeddingsTextEmbeddingInput(BaseModel):
    # The identifier of the model.  Available models and corresponding param size and dimension: - `jina-embedding-t-en-v1`, 14m, 312 - `jina-embedding-s-en-v1`, 35m, 512 (default) - `jina-embedding-b-en-v1`, 110m, 768 - `jina-embedding-l-en-v1`, 330, 1024  For more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224). 
    model: str = Field(alias='model')

    # List of texts to embed
    input: typing.Union[typing.List[str], str, typing.List[ApiSchemasEmbeddingTextDoc], ApiSchemasEmbeddingTextDoc] = Field(alias='input')

    # Type of the embedding to compute, query or document
    input_type: typing.Optional[Literal["query", "document"]] = Field(None, alias='input_type')

    # The format in which you want the embeddings to be returned.Possible value are `float` and `base64`. Defaults to `float`
    encoding_format: typing.Optional[Literal["float", "base64"]] = Field(None, alias='encoding_format')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )