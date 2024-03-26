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

from jina_ai_python_sdk.type.api_schemas_rank_usage import ApiSchemasRankUsage
from jina_ai_python_sdk.type.ranking_output_results import RankingOutputResults

class RequiredRankingOutput(TypedDict):
    # The identifier of the model.  Available models and corresponding param size and dimension: - `jina-embedding-t-en-v1`, 14m, 312 - `jina-embedding-s-en-v1`, 35m, 512 (default) - `jina-embedding-b-en-v1`, 110m, 768 - `jina-embedding-l-en-v1`, 330, 1024  For more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224). 
    model: str

    results: RankingOutputResults

    # Total usage of the request.
    usage: ApiSchemasRankUsage

class OptionalRankingOutput(TypedDict, total=False):
    pass

class RankingOutput(RequiredRankingOutput, OptionalRankingOutput):
    pass