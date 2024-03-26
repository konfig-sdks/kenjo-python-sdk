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


class TimeOffGetRequestsByDateResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            _id = schemas.StrSchema
            _userId = schemas.StrSchema
            _timeOfTypeId = schemas.StrSchema
            _policyId = schemas.StrSchema
            policyName = schemas.StrSchema
            _policyType = schemas.StrSchema
            status = schemas.StrSchema
            _from = schemas.StrSchema
            to = schemas.StrSchema
            duration = schemas.NumberSchema
            workingTime = schemas.NumberSchema
            _createdAt = schemas.StrSchema
            hasAttachment = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "_id": _id,
                "_userId": _userId,
                "_timeOfTypeId": _timeOfTypeId,
                "_policyId": _policyId,
                "policyName": policyName,
                "_policyType": _policyType,
                "status": status,
                "from": _from,
                "to": to,
                "duration": duration,
                "workingTime": workingTime,
                "_createdAt": _createdAt,
                "hasAttachment": hasAttachment,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_id"]) -> MetaOapg.properties._id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_userId"]) -> MetaOapg.properties._userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_timeOfTypeId"]) -> MetaOapg.properties._timeOfTypeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_policyId"]) -> MetaOapg.properties._policyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policyName"]) -> MetaOapg.properties.policyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_policyType"]) -> MetaOapg.properties._policyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workingTime"]) -> MetaOapg.properties.workingTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_createdAt"]) -> MetaOapg.properties._createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasAttachment"]) -> MetaOapg.properties.hasAttachment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "_id", "_userId", "_timeOfTypeId", "_policyId", "policyName", "_policyType", "status", "from", "to", "duration", "workingTime", "_createdAt", "hasAttachment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_id"]) -> typing.Union[MetaOapg.properties._id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_userId"]) -> typing.Union[MetaOapg.properties._userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_timeOfTypeId"]) -> typing.Union[MetaOapg.properties._timeOfTypeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_policyId"]) -> typing.Union[MetaOapg.properties._policyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policyName"]) -> typing.Union[MetaOapg.properties.policyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_policyType"]) -> typing.Union[MetaOapg.properties._policyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workingTime"]) -> typing.Union[MetaOapg.properties.workingTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_createdAt"]) -> typing.Union[MetaOapg.properties._createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasAttachment"]) -> typing.Union[MetaOapg.properties.hasAttachment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "_id", "_userId", "_timeOfTypeId", "_policyId", "policyName", "_policyType", "status", "from", "to", "duration", "workingTime", "_createdAt", "hasAttachment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _id: typing.Union[MetaOapg.properties._id, str, schemas.Unset] = schemas.unset,
        _userId: typing.Union[MetaOapg.properties._userId, str, schemas.Unset] = schemas.unset,
        _timeOfTypeId: typing.Union[MetaOapg.properties._timeOfTypeId, str, schemas.Unset] = schemas.unset,
        _policyId: typing.Union[MetaOapg.properties._policyId, str, schemas.Unset] = schemas.unset,
        policyName: typing.Union[MetaOapg.properties.policyName, str, schemas.Unset] = schemas.unset,
        _policyType: typing.Union[MetaOapg.properties._policyType, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        to: typing.Union[MetaOapg.properties.to, str, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        workingTime: typing.Union[MetaOapg.properties.workingTime, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _createdAt: typing.Union[MetaOapg.properties._createdAt, str, schemas.Unset] = schemas.unset,
        hasAttachment: typing.Union[MetaOapg.properties.hasAttachment, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffGetRequestsByDateResponseDataItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            _id=_id,
            _userId=_userId,
            _timeOfTypeId=_timeOfTypeId,
            _policyId=_policyId,
            policyName=policyName,
            _policyType=_policyType,
            status=status,
            to=to,
            duration=duration,
            workingTime=workingTime,
            _createdAt=_createdAt,
            hasAttachment=hasAttachment,
            _configuration=_configuration,
            **kwargs,
        )
