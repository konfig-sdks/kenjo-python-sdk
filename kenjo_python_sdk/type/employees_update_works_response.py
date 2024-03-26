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


class RequiredEmployeesUpdateWorksResponse(TypedDict):
    pass

class OptionalEmployeesUpdateWorksResponse(TypedDict, total=False):
    # The employee Kenjo *_id*.
    _id: str

    # The company id of the Kenjo employee.
    companyId: str

    # The office id of the Kenjo employee.
    officeId: str

    # The department id of the Kenjo employee.
    departmentId: str

    # The starting date of the Kenjo employee in format YYYY-MM-DDThh:mm:ss.
    startDate: str

    # The job title of the employee.
    jobTitle: str

    # The work phone of the employee.
    workPhone: str

    # The work mobile of the employee.
    workMobile: str

    # Allow to indicate if the employee has or not the assistant role.
    isAssistant: bool

    # The probation period of the employee. Format YYYY-MM-DDThh:mm:ss.000Z.
    probationPeriodEnd: str

    # The Kenjo employee id of the user to whom the employee reports. The employee id to assign can be an active or inactive user. Trying to assign the own employee id or the id of someone who is already reporting will arise an error.
    reportsToId: str

class EmployeesUpdateWorksResponse(RequiredEmployeesUpdateWorksResponse, OptionalEmployeesUpdateWorksResponse):
    pass
