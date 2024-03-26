# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from kenjo_python_sdk.paths.companies.get import GetList
from kenjo_python_sdk.apis.tags.companies_api_raw import CompaniesApiRaw


class CompaniesApi(
    GetList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CompaniesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CompaniesApiRaw(api_client)
