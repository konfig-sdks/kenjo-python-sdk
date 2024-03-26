# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kenjo_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTH_LOGIN = "/auth/login"
    AUTH_LOGOUT = "/auth/logout"
    ATTENDANCES_ATTENDANCE_ID = "/attendances/{attendanceId}"
    ATTENDANCES = "/attendances"
    ATTENDANCES_TRACKTIME = "/attendances/track-time"
    ATTENDANCES_CATEGORIES = "/attendances/categories"
    ATTENDANCES_EXPECTEDTIME = "/attendances/expected-time"
    COMPANIES = "/companies"
    OFFICES = "/offices"
    OFFICES_ID = "/offices/{id}"
    DEPARTMENTS = "/departments"
    DEPARTMENTS_ID = "/departments/{id}"
    TEAMS = "/teams"
    TEAMS_ID = "/teams/{id}"
    AREAS = "/areas"
    AREAS_ID = "/areas/{id}"
    CALENDARS = "/calendars"
    CALENDARS_ID = "/calendars/{id}"
    USERACCOUNTS = "/user-accounts"
    EMPLOYEES = "/employees"
    EMPLOYEES_EMPLOYEE_ID = "/employees/{employeeId}"
    EMPLOYEES_ACCOUNTS = "/employees/accounts"
    EMPLOYEES_PERSONALS = "/employees/personals"
    EMPLOYEES_WORKS = "/employees/works"
    EMPLOYEES_WORKSCHEDULES = "/employees/work-schedules"
    EMPLOYEES_ADDRESSES = "/employees/addresses"
    EMPLOYEES_FINANCIALS = "/employees/financials"
    EMPLOYEES_HOMES = "/employees/homes"
    EMPLOYEES_EMPLOYEE_ID_ACCOUNTS = "/employees/{employeeId}/accounts"
    EMPLOYEES_EMPLOYEE_ID_PERSONALS = "/employees/{employeeId}/personals"
    EMPLOYEES_EMPLOYEE_ID_WORKS = "/employees/{employeeId}/works"
    EMPLOYEES_EMPLOYEE_ID_WORKSCHEDULES = "/employees/{employeeId}/work-schedules"
    EMPLOYEES_EMPLOYEE_ID_ADDRESSES = "/employees/{employeeId}/addresses"
    EMPLOYEES_EMPLOYEE_ID_FINANCIALS = "/employees/{employeeId}/financials"
    EMPLOYEES_EMPLOYEE_ID_HOMES = "/employees/{employeeId}/homes"
    EMPLOYEES_EMPLOYEE_ID_ACTIVATE = "/employees/{employeeId}/activate"
    EMPLOYEES_EMPLOYEE_ID_DEACTIVATE = "/employees/{employeeId}/deactivate"
    CUSTOMFIELDS = "/custom-fields"
    TIMEOFF_REQUESTS = "/time-off/requests"
    COMPENSATION_CONTRACTS = "/compensation/contracts"
    COMPENSATION_CONTRACTTYPES = "/compensation/contract-types"
    COMPENSATION_SALARIES = "/compensation/salaries"
    COMPENSATION_ADDITIONALPAYMENTS = "/compensation/additional-payments"
    COMPENSATION_ADDITIONALPAYMENTTYPES = "/compensation/additional-payment-types"
