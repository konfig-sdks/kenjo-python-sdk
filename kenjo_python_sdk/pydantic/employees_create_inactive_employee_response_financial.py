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


class EmployeesCreateInactiveEmployeeResponseFinancial(BaseModel):
    # The accounts holder's name.
    account_holder_name: typing.Optional[str] = Field(None, alias='accountHolderName')

    # The bank name.
    bank_name: typing.Optional[str] = Field(None, alias='bankName')

    # The account number.
    account_number: typing.Optional[str] = Field(None, alias='accountNumber')

    # The IBAN.
    iban: typing.Optional[str] = Field(None, alias='iban')

    # The SWIFT code.
    swift_code: typing.Optional[str] = Field(None, alias='swiftCode')

    # The national id document.
    national_id: typing.Optional[str] = Field(None, alias='nationalId')

    # The passport number.
    passport: typing.Optional[str] = Field(None, alias='passport')

    # The national insurance number
    national_insurance_number: typing.Optional[str] = Field(None, alias='nationalInsuranceNumber')

    # The tax number.
    tax_code: typing.Optional[str] = Field(None, alias='taxCode')

    # The tax identification number.
    tax_identification_number: typing.Optional[str] = Field(None, alias='taxIdentificationNumber')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
