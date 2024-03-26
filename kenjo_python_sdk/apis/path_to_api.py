import typing_extensions

from kenjo_python_sdk.paths import PathValues
from kenjo_python_sdk.apis.paths.auth_login import AuthLogin
from kenjo_python_sdk.apis.paths.auth_logout import AuthLogout
from kenjo_python_sdk.apis.paths.attendances_attendance_id import AttendancesAttendanceId
from kenjo_python_sdk.apis.paths.attendances import Attendances
from kenjo_python_sdk.apis.paths.attendances_track_time import AttendancesTrackTime
from kenjo_python_sdk.apis.paths.attendances_categories import AttendancesCategories
from kenjo_python_sdk.apis.paths.attendances_expected_time import AttendancesExpectedTime
from kenjo_python_sdk.apis.paths.companies import Companies
from kenjo_python_sdk.apis.paths.offices import Offices
from kenjo_python_sdk.apis.paths.offices_id import OfficesId
from kenjo_python_sdk.apis.paths.departments import Departments
from kenjo_python_sdk.apis.paths.departments_id import DepartmentsId
from kenjo_python_sdk.apis.paths.teams import Teams
from kenjo_python_sdk.apis.paths.teams_id import TeamsId
from kenjo_python_sdk.apis.paths.areas import Areas
from kenjo_python_sdk.apis.paths.areas_id import AreasId
from kenjo_python_sdk.apis.paths.calendars import Calendars
from kenjo_python_sdk.apis.paths.calendars_id import CalendarsId
from kenjo_python_sdk.apis.paths.user_accounts import UserAccounts
from kenjo_python_sdk.apis.paths.employees import Employees
from kenjo_python_sdk.apis.paths.employees_employee_id import EmployeesEmployeeId
from kenjo_python_sdk.apis.paths.employees_accounts import EmployeesAccounts
from kenjo_python_sdk.apis.paths.employees_personals import EmployeesPersonals
from kenjo_python_sdk.apis.paths.employees_works import EmployeesWorks
from kenjo_python_sdk.apis.paths.employees_work_schedules import EmployeesWorkSchedules
from kenjo_python_sdk.apis.paths.employees_addresses import EmployeesAddresses
from kenjo_python_sdk.apis.paths.employees_financials import EmployeesFinancials
from kenjo_python_sdk.apis.paths.employees_homes import EmployeesHomes
from kenjo_python_sdk.apis.paths.employees_employee_id_accounts import EmployeesEmployeeIdAccounts
from kenjo_python_sdk.apis.paths.employees_employee_id_personals import EmployeesEmployeeIdPersonals
from kenjo_python_sdk.apis.paths.employees_employee_id_works import EmployeesEmployeeIdWorks
from kenjo_python_sdk.apis.paths.employees_employee_id_work_schedules import EmployeesEmployeeIdWorkSchedules
from kenjo_python_sdk.apis.paths.employees_employee_id_addresses import EmployeesEmployeeIdAddresses
from kenjo_python_sdk.apis.paths.employees_employee_id_financials import EmployeesEmployeeIdFinancials
from kenjo_python_sdk.apis.paths.employees_employee_id_homes import EmployeesEmployeeIdHomes
from kenjo_python_sdk.apis.paths.employees_employee_id_activate import EmployeesEmployeeIdActivate
from kenjo_python_sdk.apis.paths.employees_employee_id_deactivate import EmployeesEmployeeIdDeactivate
from kenjo_python_sdk.apis.paths.custom_fields import CustomFields
from kenjo_python_sdk.apis.paths.time_off_requests import TimeOffRequests
from kenjo_python_sdk.apis.paths.compensation_contracts import CompensationContracts
from kenjo_python_sdk.apis.paths.compensation_contract_types import CompensationContractTypes
from kenjo_python_sdk.apis.paths.compensation_salaries import CompensationSalaries
from kenjo_python_sdk.apis.paths.compensation_additional_payments import CompensationAdditionalPayments
from kenjo_python_sdk.apis.paths.compensation_additional_payment_types import CompensationAdditionalPaymentTypes

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_LOGIN: AuthLogin,
        PathValues.AUTH_LOGOUT: AuthLogout,
        PathValues.ATTENDANCES_ATTENDANCE_ID: AttendancesAttendanceId,
        PathValues.ATTENDANCES: Attendances,
        PathValues.ATTENDANCES_TRACKTIME: AttendancesTrackTime,
        PathValues.ATTENDANCES_CATEGORIES: AttendancesCategories,
        PathValues.ATTENDANCES_EXPECTEDTIME: AttendancesExpectedTime,
        PathValues.COMPANIES: Companies,
        PathValues.OFFICES: Offices,
        PathValues.OFFICES_ID: OfficesId,
        PathValues.DEPARTMENTS: Departments,
        PathValues.DEPARTMENTS_ID: DepartmentsId,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.AREAS: Areas,
        PathValues.AREAS_ID: AreasId,
        PathValues.CALENDARS: Calendars,
        PathValues.CALENDARS_ID: CalendarsId,
        PathValues.USERACCOUNTS: UserAccounts,
        PathValues.EMPLOYEES: Employees,
        PathValues.EMPLOYEES_EMPLOYEE_ID: EmployeesEmployeeId,
        PathValues.EMPLOYEES_ACCOUNTS: EmployeesAccounts,
        PathValues.EMPLOYEES_PERSONALS: EmployeesPersonals,
        PathValues.EMPLOYEES_WORKS: EmployeesWorks,
        PathValues.EMPLOYEES_WORKSCHEDULES: EmployeesWorkSchedules,
        PathValues.EMPLOYEES_ADDRESSES: EmployeesAddresses,
        PathValues.EMPLOYEES_FINANCIALS: EmployeesFinancials,
        PathValues.EMPLOYEES_HOMES: EmployeesHomes,
        PathValues.EMPLOYEES_EMPLOYEE_ID_ACCOUNTS: EmployeesEmployeeIdAccounts,
        PathValues.EMPLOYEES_EMPLOYEE_ID_PERSONALS: EmployeesEmployeeIdPersonals,
        PathValues.EMPLOYEES_EMPLOYEE_ID_WORKS: EmployeesEmployeeIdWorks,
        PathValues.EMPLOYEES_EMPLOYEE_ID_WORKSCHEDULES: EmployeesEmployeeIdWorkSchedules,
        PathValues.EMPLOYEES_EMPLOYEE_ID_ADDRESSES: EmployeesEmployeeIdAddresses,
        PathValues.EMPLOYEES_EMPLOYEE_ID_FINANCIALS: EmployeesEmployeeIdFinancials,
        PathValues.EMPLOYEES_EMPLOYEE_ID_HOMES: EmployeesEmployeeIdHomes,
        PathValues.EMPLOYEES_EMPLOYEE_ID_ACTIVATE: EmployeesEmployeeIdActivate,
        PathValues.EMPLOYEES_EMPLOYEE_ID_DEACTIVATE: EmployeesEmployeeIdDeactivate,
        PathValues.CUSTOMFIELDS: CustomFields,
        PathValues.TIMEOFF_REQUESTS: TimeOffRequests,
        PathValues.COMPENSATION_CONTRACTS: CompensationContracts,
        PathValues.COMPENSATION_CONTRACTTYPES: CompensationContractTypes,
        PathValues.COMPENSATION_SALARIES: CompensationSalaries,
        PathValues.COMPENSATION_ADDITIONALPAYMENTS: CompensationAdditionalPayments,
        PathValues.COMPENSATION_ADDITIONALPAYMENTTYPES: CompensationAdditionalPaymentTypes,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_LOGIN: AuthLogin,
        PathValues.AUTH_LOGOUT: AuthLogout,
        PathValues.ATTENDANCES_ATTENDANCE_ID: AttendancesAttendanceId,
        PathValues.ATTENDANCES: Attendances,
        PathValues.ATTENDANCES_TRACKTIME: AttendancesTrackTime,
        PathValues.ATTENDANCES_CATEGORIES: AttendancesCategories,
        PathValues.ATTENDANCES_EXPECTEDTIME: AttendancesExpectedTime,
        PathValues.COMPANIES: Companies,
        PathValues.OFFICES: Offices,
        PathValues.OFFICES_ID: OfficesId,
        PathValues.DEPARTMENTS: Departments,
        PathValues.DEPARTMENTS_ID: DepartmentsId,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.AREAS: Areas,
        PathValues.AREAS_ID: AreasId,
        PathValues.CALENDARS: Calendars,
        PathValues.CALENDARS_ID: CalendarsId,
        PathValues.USERACCOUNTS: UserAccounts,
        PathValues.EMPLOYEES: Employees,
        PathValues.EMPLOYEES_EMPLOYEE_ID: EmployeesEmployeeId,
        PathValues.EMPLOYEES_ACCOUNTS: EmployeesAccounts,
        PathValues.EMPLOYEES_PERSONALS: EmployeesPersonals,
        PathValues.EMPLOYEES_WORKS: EmployeesWorks,
        PathValues.EMPLOYEES_WORKSCHEDULES: EmployeesWorkSchedules,
        PathValues.EMPLOYEES_ADDRESSES: EmployeesAddresses,
        PathValues.EMPLOYEES_FINANCIALS: EmployeesFinancials,
        PathValues.EMPLOYEES_HOMES: EmployeesHomes,
        PathValues.EMPLOYEES_EMPLOYEE_ID_ACCOUNTS: EmployeesEmployeeIdAccounts,
        PathValues.EMPLOYEES_EMPLOYEE_ID_PERSONALS: EmployeesEmployeeIdPersonals,
        PathValues.EMPLOYEES_EMPLOYEE_ID_WORKS: EmployeesEmployeeIdWorks,
        PathValues.EMPLOYEES_EMPLOYEE_ID_WORKSCHEDULES: EmployeesEmployeeIdWorkSchedules,
        PathValues.EMPLOYEES_EMPLOYEE_ID_ADDRESSES: EmployeesEmployeeIdAddresses,
        PathValues.EMPLOYEES_EMPLOYEE_ID_FINANCIALS: EmployeesEmployeeIdFinancials,
        PathValues.EMPLOYEES_EMPLOYEE_ID_HOMES: EmployeesEmployeeIdHomes,
        PathValues.EMPLOYEES_EMPLOYEE_ID_ACTIVATE: EmployeesEmployeeIdActivate,
        PathValues.EMPLOYEES_EMPLOYEE_ID_DEACTIVATE: EmployeesEmployeeIdDeactivate,
        PathValues.CUSTOMFIELDS: CustomFields,
        PathValues.TIMEOFF_REQUESTS: TimeOffRequests,
        PathValues.COMPENSATION_CONTRACTS: CompensationContracts,
        PathValues.COMPENSATION_CONTRACTTYPES: CompensationContractTypes,
        PathValues.COMPENSATION_SALARIES: CompensationSalaries,
        PathValues.COMPENSATION_ADDITIONALPAYMENTS: CompensationAdditionalPayments,
        PathValues.COMPENSATION_ADDITIONALPAYMENTTYPES: CompensationAdditionalPaymentTypes,
    }
)
