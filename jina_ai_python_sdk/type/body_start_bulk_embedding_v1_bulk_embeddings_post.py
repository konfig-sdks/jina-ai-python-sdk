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


class RequiredBodyStartBulkEmbeddingV1BulkEmbeddingsPost(TypedDict):
    file: typing.IO

    model: str

class OptionalBodyStartBulkEmbeddingV1BulkEmbeddingsPost(TypedDict, total=False):
    email: str

class BodyStartBulkEmbeddingV1BulkEmbeddingsPost(RequiredBodyStartBulkEmbeddingV1BulkEmbeddingsPost, OptionalBodyStartBulkEmbeddingV1BulkEmbeddingsPost):
    pass
