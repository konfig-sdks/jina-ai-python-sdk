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


class ApiSchemasMultiEmbeddingsTextEmbeddingInput(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The input to the API for text embedding. OpenAI compatible
    """


    class MetaOapg:
        required = {
            "input",
            "model",
        }
        
        class properties:
            model = schemas.StrSchema
            
            
            class input(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_0':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    any_of_1 = schemas.StrSchema
                    
                    
                    class any_of_2(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ApiSchemasEmbeddingTextDoc']:
                                return ApiSchemasEmbeddingTextDoc
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ApiSchemasEmbeddingTextDoc'], typing.List['ApiSchemasEmbeddingTextDoc']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_2':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ApiSchemasEmbeddingTextDoc':
                            return super().__getitem__(i)
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                            cls.any_of_2,
                            ApiSchemasEmbeddingTextDoc,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'input':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class input_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def QUERY(cls):
                    return cls("query")
                
                @schemas.classproperty
                def DOCUMENT(cls):
                    return cls("document")
            
            
            class encoding_format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FLOAT(cls):
                    return cls("float")
                
                @schemas.classproperty
                def BASE64(cls):
                    return cls("base64")
            __annotations__ = {
                "model": model,
                "input": input,
                "input_type": input_type,
                "encoding_format": encoding_format,
            }
    
    input: MetaOapg.properties.input
    model: MetaOapg.properties.model
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_type"]) -> MetaOapg.properties.input_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encoding_format"]) -> MetaOapg.properties.encoding_format: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["model", "input", "input_type", "encoding_format", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_type"]) -> typing.Union[MetaOapg.properties.input_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encoding_format"]) -> typing.Union[MetaOapg.properties.encoding_format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["model", "input", "input_type", "encoding_format", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        input: typing.Union[MetaOapg.properties.input, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        input_type: typing.Union[MetaOapg.properties.input_type, str, schemas.Unset] = schemas.unset,
        encoding_format: typing.Union[MetaOapg.properties.encoding_format, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiSchemasMultiEmbeddingsTextEmbeddingInput':
        return super().__new__(
            cls,
            *args,
            input=input,
            model=model,
            input_type=input_type,
            encoding_format=encoding_format,
            _configuration=_configuration,
            **kwargs,
        )

from jina_ai_python_sdk.model.api_schemas_embedding_text_doc import ApiSchemasEmbeddingTextDoc
