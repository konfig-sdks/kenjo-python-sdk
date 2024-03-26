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


class UserAccountsListEmployeesResponseItem(BaseModel):
    # The Kenjo employee _id.
    _id: typing.Optional[str] = Field(None, alias='_id')

    # The employee email in Kenjo.
    email: typing.Optional[str] = Field(None, alias='email')

    # Indicates the active status of the Kenjo employee.
    is_active: typing.Optional[str] = Field(None, alias='isActive')

    # The first name of the Kenjo employee.
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The last name of the Kenjo employee.
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # The complete name of the Kenjo employee.
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # The Kenjo Id of the company for this employee.
    company_id: typing.Optional[str] = Field(None, alias='companyId')

    # The Kenjo Id of the office for this employee.
    office_id: typing.Optional[str] = Field(None, alias='officeId')

    # The Kenjo Id of the department for this employee.
    department_id: typing.Optional[str] = Field(None, alias='departmentId')

    # The job title for this employee.
    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
