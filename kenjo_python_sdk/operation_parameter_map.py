operation_parameter_map = {
    '/areas-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/areas/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/areas-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/areas/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/areas/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/attendances-POST': {
        'parameters': [
            {
                'name': 'date'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'breaks'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/attendances/track-time-POST': {
        'parameters': [
            {
                'name': 'dateTime'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'externalId'
            },
        ]
    },
    '/attendances/{attendanceId}-GET': {
        'parameters': [
            {
                'name': 'attendanceId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/attendances/categories-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/attendances/expected-time-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/attendances-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/attendances/{attendanceId}-DELETE': {
        'parameters': [
            {
                'name': 'attendanceId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/attendances/{attendanceId}-PUT': {
        'parameters': [
            {
                'name': 'attendanceId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'startTime'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'breaks'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/auth/login-POST': {
        'parameters': [
            {
                'name': 'apiKey'
            },
        ]
    },
    '/auth/logout-POST': {
        'parameters': [
        ]
    },
    '/calendars/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/calendars-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/companies-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/compensation/contracts-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'contractTypeId'
            },
            {
                'name': '_userId'
            },
            {
                'name': '_companyId'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/compensation/salaries-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': '_userId'
            },
            {
                'name': '_companyId'
            },
            {
                'name': 'paymentPeriod'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/compensation/additional-payment-types-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/compensation/additional-payments-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': '_userId'
            },
            {
                'name': '_companyId'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/compensation/contract-types-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/custom-fields-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'section'
            },
            {
                'name': 'label'
            },
            {
                'name': 'apiName'
            },
        ]
    },
    '/departments-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/departments/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/departments-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/departments/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/departments/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/employees/{employeeId}/activate-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/employees-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'account'
            },
            {
                'name': 'personal'
            },
            {
                'name': 'work'
            },
            {
                'name': 'workSchedule'
            },
            {
                'name': 'address'
            },
            {
                'name': 'financial'
            },
            {
                'name': 'home'
            },
        ]
    },
    '/employees/{employeeId}/deactivate-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/employees/accounts-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'email'
            },
            {
                'name': 'language'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/employees/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/employees-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/employees/work-schedules-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'trackAttendance'
            },
        ]
    },
    '/employees/addresses-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'street'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/employees/financials-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'accountHolderName'
            },
            {
                'name': 'bankName'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'iban'
            },
            {
                'name': 'swiftCode'
            },
            {
                'name': 'nationalId'
            },
            {
                'name': 'passport'
            },
            {
                'name': 'nationalInsuranceNumber'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'taxIdentificationNumber'
            },
        ]
    },
    '/employees/homes-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'spouseFirstName'
            },
            {
                'name': 'spouseLastName'
            },
            {
                'name': 'spouseBirthdate'
            },
            {
                'name': 'spouseGender'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'personalPhone'
            },
            {
                'name': 'personalMobile'
            },
        ]
    },
    '/employees/personals-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'birthdate'
            },
        ]
    },
    '/employees/works-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'workMobile'
            },
            {
                'name': 'isAssistant'
            },
            {
                'name': 'probationPeriodEnd'
            },
            {
                'name': 'reportsToId'
            },
        ]
    },
    '/employees/{employeeId}/addresses-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'street'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/employees/{employeeId}/accounts-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'email'
            },
            {
                'name': 'externalId'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/employees/{employeeId}/financials-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'accountHolderName'
            },
            {
                'name': 'bankName'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'iban'
            },
            {
                'name': 'swiftCode'
            },
            {
                'name': 'nationalId'
            },
            {
                'name': 'passport'
            },
            {
                'name': 'nationalInsuranceNumber'
            },
            {
                'name': 'taxCode'
            },
            {
                'name': 'taxIdentificationNumber'
            },
        ]
    },
    '/employees/{employeeId}/homes-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'spouseFirstName'
            },
            {
                'name': 'spouseLastName'
            },
            {
                'name': 'spouseBirthdate'
            },
            {
                'name': 'spouseGender'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'personalPhone'
            },
            {
                'name': 'personalMobile'
            },
        ]
    },
    '/employees/{employeeId}/personals-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'birthdate'
            },
        ]
    },
    '/employees/{employeeId}/work-schedules-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'mondayWorkingDay'
            },
            {
                'name': 'tuesdayWorkingDay'
            },
            {
                'name': 'wednesdayWorkingDay'
            },
            {
                'name': 'thursdayWorkingDay'
            },
            {
                'name': 'fridayWorkingDay'
            },
            {
                'name': 'saturdayWorkingDay'
            },
            {
                'name': 'sundayWorkingDay'
            },
        ]
    },
    '/employees/{employeeId}/works-PUT': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'workMobile'
            },
            {
                'name': 'isAssistant'
            },
            {
                'name': 'probationPeriodEnd'
            },
            {
                'name': 'reportsToId'
            },
        ]
    },
    '/offices-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'calendarId'
            },
            {
                'name': 'country'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'street'
            },
        ]
    },
    '/offices/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/offices-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'calendarId'
            },
            {
                'name': 'street'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/offices/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/offices/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/teams-POST': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/teams/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/teams/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
        ]
    },
    '/teams/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Authorization'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/time-off/requests-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': '_userId'
            },
            {
                'name': '_timeOffTypeId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/user-accounts-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
};