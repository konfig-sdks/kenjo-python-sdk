# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from kenjo_python_sdk.paths.employees_employee_id_activate.put import ActivateEmployeeRaw
from kenjo_python_sdk.paths.employees.post import CreateInactiveEmployeeRaw
from kenjo_python_sdk.paths.employees_employee_id_deactivate.put import DeactivateEmployeeByIdRaw
from kenjo_python_sdk.paths.employees_accounts.get import GetAccountsRaw
from kenjo_python_sdk.paths.employees_employee_id.get import GetEmployeeInformationRaw
from kenjo_python_sdk.paths.employees.get import GetListRaw
from kenjo_python_sdk.paths.employees_work_schedules.get import GetWorkSchedulesRaw
from kenjo_python_sdk.paths.employees_addresses.get import ListAddressesRaw
from kenjo_python_sdk.paths.employees_financials.get import ListFinancialsRaw
from kenjo_python_sdk.paths.employees_homes.get import ListHomesRaw
from kenjo_python_sdk.paths.employees_personals.get import ListPersonalsRaw
from kenjo_python_sdk.paths.employees_works.get import ListWorksRaw
from kenjo_python_sdk.paths.employees_employee_id_addresses.put import UpdateAddressRaw
from kenjo_python_sdk.paths.employees_employee_id_accounts.put import UpdateEmployeeAccountsRaw
from kenjo_python_sdk.paths.employees_employee_id_financials.put import UpdateFinancialsRaw
from kenjo_python_sdk.paths.employees_employee_id_homes.put import UpdateHomeRaw
from kenjo_python_sdk.paths.employees_employee_id_personals.put import UpdatePersonalsRaw
from kenjo_python_sdk.paths.employees_employee_id_work_schedules.put import UpdateWorkScheduleRaw
from kenjo_python_sdk.paths.employees_employee_id_works.put import UpdateWorksRaw


class EmployeesApiRaw(
    ActivateEmployeeRaw,
    CreateInactiveEmployeeRaw,
    DeactivateEmployeeByIdRaw,
    GetAccountsRaw,
    GetEmployeeInformationRaw,
    GetListRaw,
    GetWorkSchedulesRaw,
    ListAddressesRaw,
    ListFinancialsRaw,
    ListHomesRaw,
    ListPersonalsRaw,
    ListWorksRaw,
    UpdateAddressRaw,
    UpdateEmployeeAccountsRaw,
    UpdateFinancialsRaw,
    UpdateHomeRaw,
    UpdatePersonalsRaw,
    UpdateWorkScheduleRaw,
    UpdateWorksRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
