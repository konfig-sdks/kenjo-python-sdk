import typing_extensions

from kenjo_python_sdk.apis.tags import TagValues
from kenjo_python_sdk.apis.tags.employees_api import EmployeesApi
from kenjo_python_sdk.apis.tags.attendance_api import AttendanceApi
from kenjo_python_sdk.apis.tags.offices_api import OfficesApi
from kenjo_python_sdk.apis.tags.departments_api import DepartmentsApi
from kenjo_python_sdk.apis.tags.teams_api import TeamsApi
from kenjo_python_sdk.apis.tags.areas_api import AreasApi
from kenjo_python_sdk.apis.tags.compensation_api import CompensationApi
from kenjo_python_sdk.apis.tags.authentication_api import AuthenticationApi
from kenjo_python_sdk.apis.tags.calendars_api import CalendarsApi
from kenjo_python_sdk.apis.tags.user_accounts_api import UserAccountsApi
from kenjo_python_sdk.apis.tags.companies_api import CompaniesApi
from kenjo_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from kenjo_python_sdk.apis.tags.time_off_api import TimeOffApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.OFFICES: OfficesApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.AREAS: AreasApi,
        TagValues.COMPENSATION: CompensationApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.CALENDARS: CalendarsApi,
        TagValues.USER_ACCOUNTS: UserAccountsApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.TIME_OFF: TimeOffApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.OFFICES: OfficesApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.AREAS: AreasApi,
        TagValues.COMPENSATION: CompensationApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.CALENDARS: CalendarsApi,
        TagValues.USER_ACCOUNTS: UserAccountsApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.TIME_OFF: TimeOffApi,
    }
)
