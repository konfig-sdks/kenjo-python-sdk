# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kenjo_python_sdk import schemas  # noqa: F401


class OfficesGetListResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OfficesGetListResponseItem']:
            return OfficesGetListResponseItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OfficesGetListResponseItem'], typing.List['OfficesGetListResponseItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OfficesGetListResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OfficesGetListResponseItem':
        return super().__getitem__(i)

from kenjo_python_sdk.model.offices_get_list_response_item import OfficesGetListResponseItem
