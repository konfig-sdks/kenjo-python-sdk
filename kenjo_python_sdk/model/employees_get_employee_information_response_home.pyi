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


class EmployeesGetEmployeeInformationResponseHome(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            maritalStatus = schemas.StrSchema
            spouseFirstName = schemas.StrSchema
            spouseLastName = schemas.StrSchema
            spouseBirthdate = schemas.StrSchema
            spouseGender = schemas.StrSchema
            personalEmail = schemas.StrSchema
            personalPhone = schemas.StrSchema
            personalMobile = schemas.StrSchema
            __annotations__ = {
                "maritalStatus": maritalStatus,
                "spouseFirstName": spouseFirstName,
                "spouseLastName": spouseLastName,
                "spouseBirthdate": spouseBirthdate,
                "spouseGender": spouseGender,
                "personalEmail": personalEmail,
                "personalPhone": personalPhone,
                "personalMobile": personalMobile,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maritalStatus"]) -> MetaOapg.properties.maritalStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spouseFirstName"]) -> MetaOapg.properties.spouseFirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spouseLastName"]) -> MetaOapg.properties.spouseLastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spouseBirthdate"]) -> MetaOapg.properties.spouseBirthdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spouseGender"]) -> MetaOapg.properties.spouseGender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalEmail"]) -> MetaOapg.properties.personalEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalPhone"]) -> MetaOapg.properties.personalPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalMobile"]) -> MetaOapg.properties.personalMobile: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maritalStatus", "spouseFirstName", "spouseLastName", "spouseBirthdate", "spouseGender", "personalEmail", "personalPhone", "personalMobile", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maritalStatus"]) -> typing.Union[MetaOapg.properties.maritalStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spouseFirstName"]) -> typing.Union[MetaOapg.properties.spouseFirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spouseLastName"]) -> typing.Union[MetaOapg.properties.spouseLastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spouseBirthdate"]) -> typing.Union[MetaOapg.properties.spouseBirthdate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spouseGender"]) -> typing.Union[MetaOapg.properties.spouseGender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalEmail"]) -> typing.Union[MetaOapg.properties.personalEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalPhone"]) -> typing.Union[MetaOapg.properties.personalPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalMobile"]) -> typing.Union[MetaOapg.properties.personalMobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maritalStatus", "spouseFirstName", "spouseLastName", "spouseBirthdate", "spouseGender", "personalEmail", "personalPhone", "personalMobile", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maritalStatus: typing.Union[MetaOapg.properties.maritalStatus, str, schemas.Unset] = schemas.unset,
        spouseFirstName: typing.Union[MetaOapg.properties.spouseFirstName, str, schemas.Unset] = schemas.unset,
        spouseLastName: typing.Union[MetaOapg.properties.spouseLastName, str, schemas.Unset] = schemas.unset,
        spouseBirthdate: typing.Union[MetaOapg.properties.spouseBirthdate, str, schemas.Unset] = schemas.unset,
        spouseGender: typing.Union[MetaOapg.properties.spouseGender, str, schemas.Unset] = schemas.unset,
        personalEmail: typing.Union[MetaOapg.properties.personalEmail, str, schemas.Unset] = schemas.unset,
        personalPhone: typing.Union[MetaOapg.properties.personalPhone, str, schemas.Unset] = schemas.unset,
        personalMobile: typing.Union[MetaOapg.properties.personalMobile, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesGetEmployeeInformationResponseHome':
        return super().__new__(
            cls,
            *args,
            maritalStatus=maritalStatus,
            spouseFirstName=spouseFirstName,
            spouseLastName=spouseLastName,
            spouseBirthdate=spouseBirthdate,
            spouseGender=spouseGender,
            personalEmail=personalEmail,
            personalPhone=personalPhone,
            personalMobile=personalMobile,
            _configuration=_configuration,
            **kwargs,
        )
