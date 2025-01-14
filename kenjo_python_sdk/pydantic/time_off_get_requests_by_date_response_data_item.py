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


class TimeOffGetRequestsByDateResponseDataItem(BaseModel):
    # The provided description on the time-off request.
    description: typing.Optional[str] = Field(None, alias='description')

    # The Kenjo _id of the returned time-off request.
    _id: typing.Optional[str] = Field(None, alias='_id')

    # The employee id associated to the time-off request.
    _user_id: typing.Optional[str] = Field(None, alias='_userId')

    # The time-off type id associated to the time-off request.
    _time_of_type_id: typing.Optional[str] = Field(None, alias='_timeOfTypeId')

    # The policy id associated to the time-off request.
    _policy_id: typing.Optional[str] = Field(None, alias='_policyId')

    # The name of the policy id associated to the time-off request.
    policy_name: typing.Optional[str] = Field(None, alias='policyName')

    # The type of the policy associated to the time-off request. It can be type *Hour* or *Day*.
    _policy_type: typing.Optional[str] = Field(None, alias='_policyType')

    # The status of the time-off request.
    status: typing.Optional[str] = Field(None, alias='status')

    # The from date of the time-off request in format YYYY-MM-DDThh:mm:ss.
    from_: typing.Optional[str] = Field(None, alias='from')

    # The to date of the time-off request in format YYYY-MM-DDThh:mm:ss.
    to: typing.Optional[str] = Field(None, alias='to')

    # The duration of the time-off request. It doesn't exclude bank holidays nor non-working days.
    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    # The duration of the time-off request. It excludes bank holidays and non-working days.
    working_time: typing.Optional[typing.Union[int, float]] = Field(None, alias='workingTime')

    # The date that the time-off request was created in format YYYY-MM-DDThh:mm:ss.
    _created_at: typing.Optional[str] = Field(None, alias='_createdAt')

    # Determines if the time-off request has related attachments.
    has_attachment: typing.Optional[bool] = Field(None, alias='hasAttachment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
