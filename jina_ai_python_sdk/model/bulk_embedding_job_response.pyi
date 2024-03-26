# coding: utf-8

"""
    The Jina Embedding Serving API

    This is the UniversalAPI to access all the Jina embedding models

    The version of the OpenAPI document: 0.0.86
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from jina_ai_python_sdk import schemas  # noqa: F401


class BulkEmbeddingJobResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "model_name",
            "user_id",
            "file_name",
            "_id",
            "status",
        }
        
        class properties:
            user_id = schemas.StrSchema
            model_name = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['BulkEmbeddingJobStatus']:
                return BulkEmbeddingJobStatus
            file_name = schemas.StrSchema
            _id = schemas.StrSchema
            model_package_arn = schemas.StrSchema
            user_email = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            completed_at = schemas.DateTimeSchema
            error = schemas.StrSchema
            used_token_count = schemas.IntSchema
            __annotations__ = {
                "user_id": user_id,
                "model_name": model_name,
                "status": status,
                "file_name": file_name,
                "_id": _id,
                "model_package_arn": model_package_arn,
                "user_email": user_email,
                "created_at": created_at,
                "completed_at": completed_at,
                "error": error,
                "used_token_count": used_token_count,
            }
    
    model_name: MetaOapg.properties.model_name
    user_id: MetaOapg.properties.user_id
    file_name: MetaOapg.properties.file_name
    _id: MetaOapg.properties._id
    status: 'BulkEmbeddingJobStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_name"]) -> MetaOapg.properties.model_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'BulkEmbeddingJobStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_id"]) -> MetaOapg.properties._id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_package_arn"]) -> MetaOapg.properties.model_package_arn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed_at"]) -> MetaOapg.properties.completed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["used_token_count"]) -> MetaOapg.properties.used_token_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_id", "model_name", "status", "file_name", "_id", "model_package_arn", "user_email", "created_at", "completed_at", "error", "used_token_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_name"]) -> MetaOapg.properties.model_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'BulkEmbeddingJobStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_id"]) -> MetaOapg.properties._id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_package_arn"]) -> typing.Union[MetaOapg.properties.model_package_arn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_email"]) -> typing.Union[MetaOapg.properties.user_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed_at"]) -> typing.Union[MetaOapg.properties.completed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["used_token_count"]) -> typing.Union[MetaOapg.properties.used_token_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_id", "model_name", "status", "file_name", "_id", "model_package_arn", "user_email", "created_at", "completed_at", "error", "used_token_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        model_name: typing.Union[MetaOapg.properties.model_name, str, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        _id: typing.Union[MetaOapg.properties._id, str, ],
        status: 'BulkEmbeddingJobStatus',
        model_package_arn: typing.Union[MetaOapg.properties.model_package_arn, str, schemas.Unset] = schemas.unset,
        user_email: typing.Union[MetaOapg.properties.user_email, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        completed_at: typing.Union[MetaOapg.properties.completed_at, str, datetime, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        used_token_count: typing.Union[MetaOapg.properties.used_token_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkEmbeddingJobResponse':
        return super().__new__(
            cls,
            *args,
            model_name=model_name,
            user_id=user_id,
            file_name=file_name,
            _id=_id,
            status=status,
            model_package_arn=model_package_arn,
            user_email=user_email,
            created_at=created_at,
            completed_at=completed_at,
            error=error,
            used_token_count=used_token_count,
            _configuration=_configuration,
            **kwargs,
        )

from jina_ai_python_sdk.model.bulk_embedding_job_status import BulkEmbeddingJobStatus