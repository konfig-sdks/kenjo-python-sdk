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


class RequiredEmployeesCreateInactiveEmployeeResponseAccount(TypedDict):
    pass

class OptionalEmployeesCreateInactiveEmployeeResponseAccount(TypedDict, total=False):
    # The employee Kenjo *_id*.
    _id: str

    # The employee email in Kenjo.
    email: str

    # The employee external id for integration proposals.
    externalId: str

    # The activation status, once created is false.
    isActive: str

    # The employee language. Only is valid one of the following values 'en' (english), 'es' (spanish) or 'de' (german).
    language: str

class EmployeesCreateInactiveEmployeeResponseAccount(RequiredEmployeesCreateInactiveEmployeeResponseAccount, OptionalEmployeesCreateInactiveEmployeeResponseAccount):
    pass
