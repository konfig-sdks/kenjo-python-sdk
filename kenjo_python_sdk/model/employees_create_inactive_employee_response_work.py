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


class EmployeesCreateInactiveEmployeeResponseWork(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            companyId = schemas.StrSchema
            officeId = schemas.StrSchema
            departmentId = schemas.StrSchema
            startDate = schemas.StrSchema
            jobTitle = schemas.StrSchema
            workPhone = schemas.StrSchema
            workMobile = schemas.StrSchema
            isAssistant = schemas.BoolSchema
            probationPeriodEnd = schemas.StrSchema
            reportsToId = schemas.StrSchema
            weeklyHours = schemas.NumberSchema
            __annotations__ = {
                "companyId": companyId,
                "officeId": officeId,
                "departmentId": departmentId,
                "startDate": startDate,
                "jobTitle": jobTitle,
                "workPhone": workPhone,
                "workMobile": workMobile,
                "isAssistant": isAssistant,
                "probationPeriodEnd": probationPeriodEnd,
                "reportsToId": reportsToId,
                "weeklyHours": weeklyHours,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["officeId"]) -> MetaOapg.properties.officeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departmentId"]) -> MetaOapg.properties.departmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobTitle"]) -> MetaOapg.properties.jobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workPhone"]) -> MetaOapg.properties.workPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workMobile"]) -> MetaOapg.properties.workMobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAssistant"]) -> MetaOapg.properties.isAssistant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probationPeriodEnd"]) -> MetaOapg.properties.probationPeriodEnd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportsToId"]) -> MetaOapg.properties.reportsToId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weeklyHours"]) -> MetaOapg.properties.weeklyHours: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["companyId", "officeId", "departmentId", "startDate", "jobTitle", "workPhone", "workMobile", "isAssistant", "probationPeriodEnd", "reportsToId", "weeklyHours", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["officeId"]) -> typing.Union[MetaOapg.properties.officeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departmentId"]) -> typing.Union[MetaOapg.properties.departmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobTitle"]) -> typing.Union[MetaOapg.properties.jobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workPhone"]) -> typing.Union[MetaOapg.properties.workPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workMobile"]) -> typing.Union[MetaOapg.properties.workMobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAssistant"]) -> typing.Union[MetaOapg.properties.isAssistant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probationPeriodEnd"]) -> typing.Union[MetaOapg.properties.probationPeriodEnd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportsToId"]) -> typing.Union[MetaOapg.properties.reportsToId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weeklyHours"]) -> typing.Union[MetaOapg.properties.weeklyHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["companyId", "officeId", "departmentId", "startDate", "jobTitle", "workPhone", "workMobile", "isAssistant", "probationPeriodEnd", "reportsToId", "weeklyHours", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        officeId: typing.Union[MetaOapg.properties.officeId, str, schemas.Unset] = schemas.unset,
        departmentId: typing.Union[MetaOapg.properties.departmentId, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, schemas.Unset] = schemas.unset,
        jobTitle: typing.Union[MetaOapg.properties.jobTitle, str, schemas.Unset] = schemas.unset,
        workPhone: typing.Union[MetaOapg.properties.workPhone, str, schemas.Unset] = schemas.unset,
        workMobile: typing.Union[MetaOapg.properties.workMobile, str, schemas.Unset] = schemas.unset,
        isAssistant: typing.Union[MetaOapg.properties.isAssistant, bool, schemas.Unset] = schemas.unset,
        probationPeriodEnd: typing.Union[MetaOapg.properties.probationPeriodEnd, str, schemas.Unset] = schemas.unset,
        reportsToId: typing.Union[MetaOapg.properties.reportsToId, str, schemas.Unset] = schemas.unset,
        weeklyHours: typing.Union[MetaOapg.properties.weeklyHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesCreateInactiveEmployeeResponseWork':
        return super().__new__(
            cls,
            *args,
            companyId=companyId,
            officeId=officeId,
            departmentId=departmentId,
            startDate=startDate,
            jobTitle=jobTitle,
            workPhone=workPhone,
            workMobile=workMobile,
            isAssistant=isAssistant,
            probationPeriodEnd=probationPeriodEnd,
            reportsToId=reportsToId,
            weeklyHours=weeklyHours,
            _configuration=_configuration,
            **kwargs,
        )
