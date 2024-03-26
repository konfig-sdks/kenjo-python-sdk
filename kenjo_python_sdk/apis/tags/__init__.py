# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kenjo_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EMPLOYEES = "Employees"
    ATTENDANCE = "Attendance"
    OFFICES = "Offices"
    DEPARTMENTS = "Departments"
    TEAMS = "Teams"
    AREAS = "Areas"
    COMPENSATION = "Compensation"
    AUTHENTICATION = "Authentication"
    CALENDARS = "Calendars"
    USER_ACCOUNTS = "User accounts"
    COMPANIES = "Companies"
    CUSTOM_FIELDS = "Custom fields"
    TIME_OFF = "Time off"
