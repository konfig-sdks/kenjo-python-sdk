# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from kenjo_python_sdk.pydantic.employees_get_employee_information_response_account import EmployeesGetEmployeeInformationResponseAccount
from kenjo_python_sdk.pydantic.employees_get_employee_information_response_address import EmployeesGetEmployeeInformationResponseAddress
from kenjo_python_sdk.pydantic.employees_get_employee_information_response_financial import EmployeesGetEmployeeInformationResponseFinancial
from kenjo_python_sdk.pydantic.employees_get_employee_information_response_home import EmployeesGetEmployeeInformationResponseHome
from kenjo_python_sdk.pydantic.employees_get_employee_information_response_personal import EmployeesGetEmployeeInformationResponsePersonal
from kenjo_python_sdk.pydantic.employees_get_employee_information_response_work import EmployeesGetEmployeeInformationResponseWork
from kenjo_python_sdk.pydantic.employees_get_employee_information_response_work_schedule import EmployeesGetEmployeeInformationResponseWorkSchedule

class EmployeesGetEmployeeInformationResponse(BaseModel):
    account: typing.Optional[EmployeesGetEmployeeInformationResponseAccount] = Field(None, alias='account')

    personal: typing.Optional[EmployeesGetEmployeeInformationResponsePersonal] = Field(None, alias='personal')

    work: typing.Optional[EmployeesGetEmployeeInformationResponseWork] = Field(None, alias='work')

    work_schedule: typing.Optional[EmployeesGetEmployeeInformationResponseWorkSchedule] = Field(None, alias='workSchedule')

    address: typing.Optional[EmployeesGetEmployeeInformationResponseAddress] = Field(None, alias='address')

    financial: typing.Optional[EmployeesGetEmployeeInformationResponseFinancial] = Field(None, alias='financial')

    home: typing.Optional[EmployeesGetEmployeeInformationResponseHome] = Field(None, alias='home')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
