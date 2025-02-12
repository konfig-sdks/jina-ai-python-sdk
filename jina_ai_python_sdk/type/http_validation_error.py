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

from jina_ai_python_sdk.type.validation_error import ValidationError

class RequiredHTTPValidationError(TypedDict):
    pass

class OptionalHTTPValidationError(TypedDict, total=False):
    detail: typing.List[ValidationError]

class HTTPValidationError(RequiredHTTPValidationError, OptionalHTTPValidationError):
    pass
