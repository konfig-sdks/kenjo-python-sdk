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


class AttendanceCreateEntryRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "startTime",
        }
        
        class properties:
            date = schemas.StrSchema
            startTime = schemas.StrSchema
            userId = schemas.StrSchema
            email = schemas.StrSchema
            externalId = schemas.StrSchema
            endTime = schemas.StrSchema
        
            @staticmethod
            def breaks() -> typing.Type['AttendanceCreateEntryRequestBreaks']:
                return AttendanceCreateEntryRequestBreaks
            comment = schemas.StrSchema
            __annotations__ = {
                "date": date,
                "startTime": startTime,
                "userId": userId,
                "email": email,
                "externalId": externalId,
                "endTime": endTime,
                "breaks": breaks,
                "comment": comment,
            }
    
    date: MetaOapg.properties.date
    startTime: MetaOapg.properties.startTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalId"]) -> MetaOapg.properties.externalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endTime"]) -> MetaOapg.properties.endTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breaks"]) -> 'AttendanceCreateEntryRequestBreaks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "startTime", "userId", "email", "externalId", "endTime", "breaks", "comment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalId"]) -> typing.Union[MetaOapg.properties.externalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endTime"]) -> typing.Union[MetaOapg.properties.endTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breaks"]) -> typing.Union['AttendanceCreateEntryRequestBreaks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "startTime", "userId", "email", "externalId", "endTime", "breaks", "comment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, ],
        startTime: typing.Union[MetaOapg.properties.startTime, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        externalId: typing.Union[MetaOapg.properties.externalId, str, schemas.Unset] = schemas.unset,
        endTime: typing.Union[MetaOapg.properties.endTime, str, schemas.Unset] = schemas.unset,
        breaks: typing.Union['AttendanceCreateEntryRequestBreaks', schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttendanceCreateEntryRequest':
        return super().__new__(
            cls,
            *args,
            date=date,
            startTime=startTime,
            userId=userId,
            email=email,
            externalId=externalId,
            endTime=endTime,
            breaks=breaks,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )

from kenjo_python_sdk.model.attendance_create_entry_request_breaks import AttendanceCreateEntryRequestBreaks