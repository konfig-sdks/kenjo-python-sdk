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


class AttendanceCreateTrackTimeRequest(BaseModel):
    # The date and the time of the Kenjo employee in format YYYY-MM-DDThh:mm:ss.
    date_time: str = Field(alias='dateTime')

    # The Kenjo employee *_id*.
    user_id: typing.Optional[str] = Field(None, alias='userId')

    # The Kenjo *email* for an employee.
    email: typing.Optional[str] = Field(None, alias='email')

    # The *external id* for an employee for integrations.
    external_id: typing.Optional[str] = Field(None, alias='externalId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )