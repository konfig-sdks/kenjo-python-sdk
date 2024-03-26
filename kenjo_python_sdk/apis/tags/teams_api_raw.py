# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from kenjo_python_sdk.paths.teams.post import CreateTeamRaw
from kenjo_python_sdk.paths.teams_id.get import GetByIdRaw
from kenjo_python_sdk.paths.teams.get import GetListRaw
from kenjo_python_sdk.paths.teams_id.delete import RemoveTeamRaw
from kenjo_python_sdk.paths.teams_id.put import UpdateTeamAttributesRaw


class TeamsApiRaw(
    CreateTeamRaw,
    GetByIdRaw,
    GetListRaw,
    RemoveTeamRaw,
    UpdateTeamAttributesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
