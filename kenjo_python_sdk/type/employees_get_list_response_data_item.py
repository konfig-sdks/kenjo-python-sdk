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


class RequiredEmployeesGetListResponseDataItem(TypedDict):
    pass

class OptionalEmployeesGetListResponseDataItem(TypedDict, total=False):
    # The Kenjo employee _id.
    _id: str

    # The employee email in Kenjo.
    email: str

    # Indicates the active status of the Kenjo employee.
    isActive: str

    # The external id for this employee.
    externalId: str

    # The employee language. The available values are 'en' (english), 'es' (spanish) or 'de' (german).
    language: str

class EmployeesGetListResponseDataItem(RequiredEmployeesGetListResponseDataItem, OptionalEmployeesGetListResponseDataItem):
    pass