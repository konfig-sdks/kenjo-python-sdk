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


class EmployeesGetEmployeeInformationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def account() -> typing.Type['EmployeesGetEmployeeInformationResponseAccount']:
                return EmployeesGetEmployeeInformationResponseAccount
        
            @staticmethod
            def personal() -> typing.Type['EmployeesGetEmployeeInformationResponsePersonal']:
                return EmployeesGetEmployeeInformationResponsePersonal
        
            @staticmethod
            def work() -> typing.Type['EmployeesGetEmployeeInformationResponseWork']:
                return EmployeesGetEmployeeInformationResponseWork
        
            @staticmethod
            def workSchedule() -> typing.Type['EmployeesGetEmployeeInformationResponseWorkSchedule']:
                return EmployeesGetEmployeeInformationResponseWorkSchedule
        
            @staticmethod
            def address() -> typing.Type['EmployeesGetEmployeeInformationResponseAddress']:
                return EmployeesGetEmployeeInformationResponseAddress
        
            @staticmethod
            def financial() -> typing.Type['EmployeesGetEmployeeInformationResponseFinancial']:
                return EmployeesGetEmployeeInformationResponseFinancial
        
            @staticmethod
            def home() -> typing.Type['EmployeesGetEmployeeInformationResponseHome']:
                return EmployeesGetEmployeeInformationResponseHome
            __annotations__ = {
                "account": account,
                "personal": personal,
                "work": work,
                "workSchedule": workSchedule,
                "address": address,
                "financial": financial,
                "home": home,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account"]) -> 'EmployeesGetEmployeeInformationResponseAccount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal"]) -> 'EmployeesGetEmployeeInformationResponsePersonal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work"]) -> 'EmployeesGetEmployeeInformationResponseWork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workSchedule"]) -> 'EmployeesGetEmployeeInformationResponseWorkSchedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'EmployeesGetEmployeeInformationResponseAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["financial"]) -> 'EmployeesGetEmployeeInformationResponseFinancial': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["home"]) -> 'EmployeesGetEmployeeInformationResponseHome': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account", "personal", "work", "workSchedule", "address", "financial", "home", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account"]) -> typing.Union['EmployeesGetEmployeeInformationResponseAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal"]) -> typing.Union['EmployeesGetEmployeeInformationResponsePersonal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work"]) -> typing.Union['EmployeesGetEmployeeInformationResponseWork', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workSchedule"]) -> typing.Union['EmployeesGetEmployeeInformationResponseWorkSchedule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['EmployeesGetEmployeeInformationResponseAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["financial"]) -> typing.Union['EmployeesGetEmployeeInformationResponseFinancial', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["home"]) -> typing.Union['EmployeesGetEmployeeInformationResponseHome', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account", "personal", "work", "workSchedule", "address", "financial", "home", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        account: typing.Union['EmployeesGetEmployeeInformationResponseAccount', schemas.Unset] = schemas.unset,
        personal: typing.Union['EmployeesGetEmployeeInformationResponsePersonal', schemas.Unset] = schemas.unset,
        work: typing.Union['EmployeesGetEmployeeInformationResponseWork', schemas.Unset] = schemas.unset,
        workSchedule: typing.Union['EmployeesGetEmployeeInformationResponseWorkSchedule', schemas.Unset] = schemas.unset,
        address: typing.Union['EmployeesGetEmployeeInformationResponseAddress', schemas.Unset] = schemas.unset,
        financial: typing.Union['EmployeesGetEmployeeInformationResponseFinancial', schemas.Unset] = schemas.unset,
        home: typing.Union['EmployeesGetEmployeeInformationResponseHome', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesGetEmployeeInformationResponse':
        return super().__new__(
            cls,
            *args,
            account=account,
            personal=personal,
            work=work,
            workSchedule=workSchedule,
            address=address,
            financial=financial,
            home=home,
            _configuration=_configuration,
            **kwargs,
        )

from kenjo_python_sdk.model.employees_get_employee_information_response_account import EmployeesGetEmployeeInformationResponseAccount
from kenjo_python_sdk.model.employees_get_employee_information_response_address import EmployeesGetEmployeeInformationResponseAddress
from kenjo_python_sdk.model.employees_get_employee_information_response_financial import EmployeesGetEmployeeInformationResponseFinancial
from kenjo_python_sdk.model.employees_get_employee_information_response_home import EmployeesGetEmployeeInformationResponseHome
from kenjo_python_sdk.model.employees_get_employee_information_response_personal import EmployeesGetEmployeeInformationResponsePersonal
from kenjo_python_sdk.model.employees_get_employee_information_response_work import EmployeesGetEmployeeInformationResponseWork
from kenjo_python_sdk.model.employees_get_employee_information_response_work_schedule import EmployeesGetEmployeeInformationResponseWorkSchedule