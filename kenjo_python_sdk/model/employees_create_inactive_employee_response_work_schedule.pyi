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


class EmployeesCreateInactiveEmployeeResponseWorkSchedule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            mondayWorkingDay = schemas.BoolSchema
            tuesdayWorkingDay = schemas.BoolSchema
            wednesdayWorkingDay = schemas.BoolSchema
            thursdayWorkingDay = schemas.BoolSchema
            fridayWorkingDay = schemas.BoolSchema
            saturdayWorkingDay = schemas.BoolSchema
            sundayWorkingDay = schemas.BoolSchema
            trackAttendance = schemas.BoolSchema
            __annotations__ = {
                "mondayWorkingDay": mondayWorkingDay,
                "tuesdayWorkingDay": tuesdayWorkingDay,
                "wednesdayWorkingDay": wednesdayWorkingDay,
                "thursdayWorkingDay": thursdayWorkingDay,
                "fridayWorkingDay": fridayWorkingDay,
                "saturdayWorkingDay": saturdayWorkingDay,
                "sundayWorkingDay": sundayWorkingDay,
                "trackAttendance": trackAttendance,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mondayWorkingDay"]) -> MetaOapg.properties.mondayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tuesdayWorkingDay"]) -> MetaOapg.properties.tuesdayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wednesdayWorkingDay"]) -> MetaOapg.properties.wednesdayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thursdayWorkingDay"]) -> MetaOapg.properties.thursdayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fridayWorkingDay"]) -> MetaOapg.properties.fridayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saturdayWorkingDay"]) -> MetaOapg.properties.saturdayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sundayWorkingDay"]) -> MetaOapg.properties.sundayWorkingDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackAttendance"]) -> MetaOapg.properties.trackAttendance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mondayWorkingDay", "tuesdayWorkingDay", "wednesdayWorkingDay", "thursdayWorkingDay", "fridayWorkingDay", "saturdayWorkingDay", "sundayWorkingDay", "trackAttendance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mondayWorkingDay"]) -> typing.Union[MetaOapg.properties.mondayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tuesdayWorkingDay"]) -> typing.Union[MetaOapg.properties.tuesdayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wednesdayWorkingDay"]) -> typing.Union[MetaOapg.properties.wednesdayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thursdayWorkingDay"]) -> typing.Union[MetaOapg.properties.thursdayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fridayWorkingDay"]) -> typing.Union[MetaOapg.properties.fridayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saturdayWorkingDay"]) -> typing.Union[MetaOapg.properties.saturdayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sundayWorkingDay"]) -> typing.Union[MetaOapg.properties.sundayWorkingDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackAttendance"]) -> typing.Union[MetaOapg.properties.trackAttendance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mondayWorkingDay", "tuesdayWorkingDay", "wednesdayWorkingDay", "thursdayWorkingDay", "fridayWorkingDay", "saturdayWorkingDay", "sundayWorkingDay", "trackAttendance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        mondayWorkingDay: typing.Union[MetaOapg.properties.mondayWorkingDay, bool, schemas.Unset] = schemas.unset,
        tuesdayWorkingDay: typing.Union[MetaOapg.properties.tuesdayWorkingDay, bool, schemas.Unset] = schemas.unset,
        wednesdayWorkingDay: typing.Union[MetaOapg.properties.wednesdayWorkingDay, bool, schemas.Unset] = schemas.unset,
        thursdayWorkingDay: typing.Union[MetaOapg.properties.thursdayWorkingDay, bool, schemas.Unset] = schemas.unset,
        fridayWorkingDay: typing.Union[MetaOapg.properties.fridayWorkingDay, bool, schemas.Unset] = schemas.unset,
        saturdayWorkingDay: typing.Union[MetaOapg.properties.saturdayWorkingDay, bool, schemas.Unset] = schemas.unset,
        sundayWorkingDay: typing.Union[MetaOapg.properties.sundayWorkingDay, bool, schemas.Unset] = schemas.unset,
        trackAttendance: typing.Union[MetaOapg.properties.trackAttendance, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesCreateInactiveEmployeeResponseWorkSchedule':
        return super().__new__(
            cls,
            *args,
            mondayWorkingDay=mondayWorkingDay,
            tuesdayWorkingDay=tuesdayWorkingDay,
            wednesdayWorkingDay=wednesdayWorkingDay,
            thursdayWorkingDay=thursdayWorkingDay,
            fridayWorkingDay=fridayWorkingDay,
            saturdayWorkingDay=saturdayWorkingDay,
            sundayWorkingDay=sundayWorkingDay,
            trackAttendance=trackAttendance,
            _configuration=_configuration,
            **kwargs,
        )
