# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
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

from kenjo_python_sdk import schemas  # noqa: F401


class AttendanceGetExpectedTimeByUserResponseDataItemDaysItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            date = schemas.StrSchema
            expectedHours = schemas.NumberSchema
            expectedMinutes = schemas.NumberSchema
            __annotations__ = {
                "date": date,
                "expectedHours": expectedHours,
                "expectedMinutes": expectedMinutes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectedHours"]) -> MetaOapg.properties.expectedHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expectedMinutes"]) -> MetaOapg.properties.expectedMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "expectedHours", "expectedMinutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectedHours"]) -> typing.Union[MetaOapg.properties.expectedHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expectedMinutes"]) -> typing.Union[MetaOapg.properties.expectedMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "expectedHours", "expectedMinutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        expectedHours: typing.Union[MetaOapg.properties.expectedHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        expectedMinutes: typing.Union[MetaOapg.properties.expectedMinutes, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttendanceGetExpectedTimeByUserResponseDataItemDaysItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            expectedHours=expectedHours,
            expectedMinutes=expectedMinutes,
            _configuration=_configuration,
            **kwargs,
        )
