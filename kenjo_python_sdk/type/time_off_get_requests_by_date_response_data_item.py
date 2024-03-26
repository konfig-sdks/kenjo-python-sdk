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


RequiredTimeOffGetRequestsByDateResponseDataItem = TypedDict("RequiredTimeOffGetRequestsByDateResponseDataItem", {
    })

OptionalTimeOffGetRequestsByDateResponseDataItem = TypedDict("OptionalTimeOffGetRequestsByDateResponseDataItem", {
    # The provided description on the time-off request.
    "description": str,

    # The Kenjo _id of the returned time-off request.
    "_id": str,

    # The employee id associated to the time-off request.
    "_userId": str,

    # The time-off type id associated to the time-off request.
    "_timeOfTypeId": str,

    # The policy id associated to the time-off request.
    "_policyId": str,

    # The name of the policy id associated to the time-off request.
    "policyName": str,

    # The type of the policy associated to the time-off request. It can be type *Hour* or *Day*.
    "_policyType": str,

    # The status of the time-off request.
    "status": str,

    # The from date of the time-off request in format YYYY-MM-DDThh:mm:ss.
    "from": str,

    # The to date of the time-off request in format YYYY-MM-DDThh:mm:ss.
    "to": str,

    # The duration of the time-off request. It doesn't exclude bank holidays nor non-working days.
    "duration": typing.Union[int, float],

    # The duration of the time-off request. It excludes bank holidays and non-working days.
    "workingTime": typing.Union[int, float],

    # The date that the time-off request was created in format YYYY-MM-DDThh:mm:ss.
    "_createdAt": str,

    # Determines if the time-off request has related attachments.
    "hasAttachment": bool,
    }, total=False)

class TimeOffGetRequestsByDateResponseDataItem(RequiredTimeOffGetRequestsByDateResponseDataItem, OptionalTimeOffGetRequestsByDateResponseDataItem):
    pass
