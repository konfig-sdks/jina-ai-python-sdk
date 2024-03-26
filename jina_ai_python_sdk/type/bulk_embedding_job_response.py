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

from jina_ai_python_sdk.type.bulk_embedding_job_status import BulkEmbeddingJobStatus

class RequiredBulkEmbeddingJobResponse(TypedDict):
    # The user ID of the user who created the job
    user_id: str

    # The name of the model to use
    model_name: str

    # The status of the job
    status: BulkEmbeddingJobStatus

    # The name of the input file
    file_name: str

    # The ID of the job
    _id: str

class OptionalBulkEmbeddingJobResponse(TypedDict, total=False):
    # The model package ARN
    model_package_arn: str

    # The email of the user who created the job
    user_email: str

    # Time of creation of the job.
    created_at: datetime

    # Time of completion of the job.
    completed_at: datetime

    # The error message of the job
    error: str

    # The number of tokens used for the job
    used_token_count: int

class BulkEmbeddingJobResponse(RequiredBulkEmbeddingJobResponse, OptionalBulkEmbeddingJobResponse):
    pass