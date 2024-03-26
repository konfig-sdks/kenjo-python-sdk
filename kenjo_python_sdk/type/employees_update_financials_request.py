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


class RequiredEmployeesUpdateFinancialsRequest(TypedDict):
    pass

class OptionalEmployeesUpdateFinancialsRequest(TypedDict, total=False):
    # The accounts holder's name.
    accountHolderName: str

    # The bank name.
    bankName: str

    # The account number.
    accountNumber: str

    # The IBAN.
    iban: str

    # The SWIFT code.
    swiftCode: str

    # The national id document.
    nationalId: str

    # The passport number.
    passport: str

    # The national insurance number
    nationalInsuranceNumber: str

    # The tax number.
    taxCode: str

    # The tax identification number.
    taxIdentificationNumber: str

class EmployeesUpdateFinancialsRequest(RequiredEmployeesUpdateFinancialsRequest, OptionalEmployeesUpdateFinancialsRequest):
    pass
