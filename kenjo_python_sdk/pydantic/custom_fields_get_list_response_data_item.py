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

from kenjo_python_sdk.pydantic.custom_fields_get_list_response_data_item_values import CustomFieldsGetListResponseDataItemValues

class CustomFieldsGetListResponseDataItem(BaseModel):
    # The Kenjo _id of the custom field.
    _id: typing.Optional[str] = Field(None, alias='_id')

    # The name of custom field section.
    section: typing.Optional[str] = Field(None, alias='section')

    # The name of custom field label.
    label: typing.Optional[str] = Field(None, alias='label')

    # The api name is a required identifier to perform POST and PUT operations with employees.
    api_name: typing.Optional[str] = Field(None, alias='apiName')

    # The data type of the custom field. Possible values \"Text\", \"TextArea\", \"List\", \"Date\", \"Number\", \"Email\", \"Boolean\" and \"Url\"
    type: typing.Optional[str] = Field(None, alias='type')

    values: typing.Optional[CustomFieldsGetListResponseDataItemValues] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )