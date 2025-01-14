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


class RequiredEmployeesGetWorkSchedulesResponseDataItem(TypedDict):
    pass

class OptionalEmployeesGetWorkSchedulesResponseDataItem(TypedDict, total=False):
    # The _id of the Kenjo employee.
    _id: str

    # Indicate if mondays are working days for the employee.
    mondayWorkingDay: bool

    # Indicate if tuesdays are working days for the employee.
    tuesdayWorkingDay: bool

    # Indicate if wednesdays are working days for the employee.
    wednesdayWorkingDay: bool

    # Indicate if thursdays are working days for the employee.
    thursdayWorkingDay: bool

    # Indicate if fridays are working days for the employee.
    fridayWorkingDay: bool

    # Indicate if saturdays are working days for the employee.
    saturdayWorkingDay: bool

    # Indicate if sundays are working days for the employee.
    sundayWorkingDay: bool

    # The activation status of attendance tracking for the employee.
    trackAttendance: bool

class EmployeesGetWorkSchedulesResponseDataItem(RequiredEmployeesGetWorkSchedulesResponseDataItem, OptionalEmployeesGetWorkSchedulesResponseDataItem):
    pass
