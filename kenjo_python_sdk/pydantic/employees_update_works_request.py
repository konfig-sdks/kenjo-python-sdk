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


class EmployeesUpdateWorksRequest(BaseModel):
    # The company id of the Kenjo employee.
    company_id: typing.Optional[str] = Field(None, alias='companyId')

    # The office id of the Kenjo employee.
    office_id: typing.Optional[str] = Field(None, alias='officeId')

    # The department id of the Kenjo employee.
    department_id: typing.Optional[str] = Field(None, alias='departmentId')

    # The starting date of the Kenjo employee in format YYYY-MM-DDThh:mm:ss.
    start_date: typing.Optional[str] = Field(None, alias='startDate')

    # The job title of the employee.
    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    # The work phone of the employee.
    work_phone: typing.Optional[str] = Field(None, alias='workPhone')

    # The work mobile of the employee.
    work_mobile: typing.Optional[str] = Field(None, alias='workMobile')

    # Allow to indicate if the employee has or not the assistant role.
    is_assistant: typing.Optional[bool] = Field(None, alias='isAssistant')

    # The probation period of the employee. Format YYYY-MM-DDThh:mm:ss.000Z.
    probation_period_end: typing.Optional[str] = Field(None, alias='probationPeriodEnd')

    # The Kenjo employee id of the user to whom the employee reports. The employee id to assign can be an active or inactive user. Trying to assign the own employee id or the id of someone who is already reporting will arise an error.
    reports_to_id: typing.Optional[str] = Field(None, alias='reportsToId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )