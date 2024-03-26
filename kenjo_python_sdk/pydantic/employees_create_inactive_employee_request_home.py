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


class EmployeesCreateInactiveEmployeeRequestHome(BaseModel):
    # The marital status. Only is valid one of the following values \"Divorced\", \"Domestic Partnership\", \"Married\", \"Separated\", \"Single\", \"Widowed\".
    marital_status: typing.Optional[str] = Field(None, alias='maritalStatus')

    # The first name of the employee's spouse.
    spouse_first_name: typing.Optional[str] = Field(None, alias='spouseFirstName')

    # The last name of the employee's spouse.
    spouse_last_name: typing.Optional[str] = Field(None, alias='spouseLastName')

    # The birth date of the employee's spouse. Format YYYY-MM-DDThh:mm:ss.000Z.
    spouse_birthdate: typing.Optional[str] = Field(None, alias='spouseBirthdate')

    # The employee's spouse gender. Only is valid one of the following values 'Male' (male), 'Female' (female) or 'Other' (other).
    spouse_gender: typing.Optional[str] = Field(None, alias='spouseGender')

    # The employee personal email.
    personal_email: typing.Optional[str] = Field(None, alias='personalEmail')

    # The employee personal phone.
    personal_phone: typing.Optional[str] = Field(None, alias='personalPhone')

    # The employee personal phone
    personal_mobile: typing.Optional[str] = Field(None, alias='personalMobile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
