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


class RequiredCompensationGetContractsResponseDataItem(TypedDict):
    pass

class OptionalCompensationGetContractsResponseDataItem(TypedDict, total=False):
    # The Kenjo _id of the returned contracts.
    _id: str

    # The employee id associated to the contract.
    _userId: str

    # The company id associated to the contract.
    _companyId: str

    # The start date of the contract in format YYYY-MM-DDThh:mm:ss.
    startDate: str

    # The contract type id associated to the contract.
    contractTypeId: str

class CompensationGetContractsResponseDataItem(RequiredCompensationGetContractsResponseDataItem, OptionalCompensationGetContractsResponseDataItem):
    pass