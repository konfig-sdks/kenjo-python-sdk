# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import kenjo_python_sdk
from kenjo_python_sdk.model.employees_list_works_response_data_item import EmployeesListWorksResponseDataItem
from kenjo_python_sdk import configuration


class TestEmployeesListWorksResponseDataItem(unittest.TestCase):
    """EmployeesListWorksResponseDataItem unit test stubs"""
    pass


if __name__ == '__main__':
    unittest.main()
