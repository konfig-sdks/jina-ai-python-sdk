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


class RequiredApiSchemasEmbeddingUsage(TypedDict):
    # The number of tokens used by all the texts in the input
    total_tokens: int

    # Same as total_tokens
    prompt_tokens: int

class OptionalApiSchemasEmbeddingUsage(TypedDict, total=False):
    pass

class ApiSchemasEmbeddingUsage(RequiredApiSchemasEmbeddingUsage, OptionalApiSchemasEmbeddingUsage):
    pass
