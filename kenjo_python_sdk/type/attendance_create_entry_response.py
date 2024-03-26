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

from kenjo_python_sdk.type.attendance_create_entry_response_breaks import AttendanceCreateEntryResponseBreaks

class RequiredAttendanceCreateEntryResponse(TypedDict):
    pass

class OptionalAttendanceCreateEntryResponse(TypedDict, total=False):
    # The Kenjo _id of the new attendance entry.
    _id: str

    # The id of the employee assigned to the requested attendance entry.
    userId: str

    # The email of the employee assigned to the requested attendance entry.
    email: str

    # The external Id of the employee assigned to the requested attendance entry.
    externalId: str

    # The start date time of the created attendance entry
    startTime: str

    # The end date time of the created attendance entry.
    endTime: str

    breaks: AttendanceCreateEntryResponseBreaks

    # DEPRECATED field, use the 'breaks' field to specify the breaktime. The time in minutes to indicate a break of time. It cannot be greater than the total of minutes reported for the attendance entry.
    breakTime: typing.Union[int, float]

    # Optional text to describe an attendance record (pair of startTime and endTime). The maximum number of characters is 150.
    comment: str

class AttendanceCreateEntryResponse(RequiredAttendanceCreateEntryResponse, OptionalAttendanceCreateEntryResponse):
    pass
