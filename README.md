<div align="left">

[![Visit Kenjo](./header.png)](https://kenjo.io)

# Kenjo<a id="kenjo"></a>

Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`kenjo.areas.create_new_area`](#kenjoareascreate_new_area)
  * [`kenjo.areas.get_by_id`](#kenjoareasget_by_id)
  * [`kenjo.areas.get_list`](#kenjoareasget_list)
  * [`kenjo.areas.remove_by_id`](#kenjoareasremove_by_id)
  * [`kenjo.areas.update_area_by_id`](#kenjoareasupdate_area_by_id)
  * [`kenjo.attendance.create_entry`](#kenjoattendancecreate_entry)
  * [`kenjo.attendance.create_track_time`](#kenjoattendancecreate_track_time)
  * [`kenjo.attendance.get_by_id`](#kenjoattendanceget_by_id)
  * [`kenjo.attendance.get_categories`](#kenjoattendanceget_categories)
  * [`kenjo.attendance.get_expected_time_by_user`](#kenjoattendanceget_expected_time_by_user)
  * [`kenjo.attendance.get_list`](#kenjoattendanceget_list)
  * [`kenjo.attendance.remove_by_id`](#kenjoattendanceremove_by_id)
  * [`kenjo.attendance.update_entry`](#kenjoattendanceupdate_entry)
  * [`kenjo.authentication.create_bearer_token`](#kenjoauthenticationcreate_bearer_token)
  * [`kenjo.authentication.invalidate_token`](#kenjoauthenticationinvalidate_token)
  * [`kenjo.calendars.get_by_id`](#kenjocalendarsget_by_id)
  * [`kenjo.calendars.get_list`](#kenjocalendarsget_list)
  * [`kenjo.companies.get_list`](#kenjocompaniesget_list)
  * [`kenjo.compensation.get_contracts`](#kenjocompensationget_contracts)
  * [`kenjo.compensation.get_salaries_list`](#kenjocompensationget_salaries_list)
  * [`kenjo.compensation.list_additional_payment_types`](#kenjocompensationlist_additional_payment_types)
  * [`kenjo.compensation.list_additional_payments`](#kenjocompensationlist_additional_payments)
  * [`kenjo.compensation.list_contract_types`](#kenjocompensationlist_contract_types)
  * [`kenjo.custom_fields.get_list`](#kenjocustom_fieldsget_list)
  * [`kenjo.departments.create_new_department`](#kenjodepartmentscreate_new_department)
  * [`kenjo.departments.get_by_id`](#kenjodepartmentsget_by_id)
  * [`kenjo.departments.list_departments`](#kenjodepartmentslist_departments)
  * [`kenjo.departments.remove_by_id`](#kenjodepartmentsremove_by_id)
  * [`kenjo.departments.update_attributes`](#kenjodepartmentsupdate_attributes)
  * [`kenjo.employees.activate_employee`](#kenjoemployeesactivate_employee)
  * [`kenjo.employees.create_inactive_employee`](#kenjoemployeescreate_inactive_employee)
  * [`kenjo.employees.deactivate_employee_by_id`](#kenjoemployeesdeactivate_employee_by_id)
  * [`kenjo.employees.get_accounts`](#kenjoemployeesget_accounts)
  * [`kenjo.employees.get_employee_information`](#kenjoemployeesget_employee_information)
  * [`kenjo.employees.get_list`](#kenjoemployeesget_list)
  * [`kenjo.employees.get_work_schedules`](#kenjoemployeesget_work_schedules)
  * [`kenjo.employees.list_addresses`](#kenjoemployeeslist_addresses)
  * [`kenjo.employees.list_financials`](#kenjoemployeeslist_financials)
  * [`kenjo.employees.list_homes`](#kenjoemployeeslist_homes)
  * [`kenjo.employees.list_personals`](#kenjoemployeeslist_personals)
  * [`kenjo.employees.list_works`](#kenjoemployeeslist_works)
  * [`kenjo.employees.update_address`](#kenjoemployeesupdate_address)
  * [`kenjo.employees.update_employee_accounts`](#kenjoemployeesupdate_employee_accounts)
  * [`kenjo.employees.update_financials`](#kenjoemployeesupdate_financials)
  * [`kenjo.employees.update_home`](#kenjoemployeesupdate_home)
  * [`kenjo.employees.update_personals`](#kenjoemployeesupdate_personals)
  * [`kenjo.employees.update_work_schedule`](#kenjoemployeesupdate_work_schedule)
  * [`kenjo.employees.update_works`](#kenjoemployeesupdate_works)
  * [`kenjo.offices.create_new_office`](#kenjoofficescreate_new_office)
  * [`kenjo.offices.get_by_id`](#kenjoofficesget_by_id)
  * [`kenjo.offices.get_list`](#kenjoofficesget_list)
  * [`kenjo.offices.remove_by_id`](#kenjoofficesremove_by_id)
  * [`kenjo.offices.update_office_attributes`](#kenjoofficesupdate_office_attributes)
  * [`kenjo.teams.create_team`](#kenjoteamscreate_team)
  * [`kenjo.teams.get_by_id`](#kenjoteamsget_by_id)
  * [`kenjo.teams.get_list`](#kenjoteamsget_list)
  * [`kenjo.teams.remove_team`](#kenjoteamsremove_team)
  * [`kenjo.teams.update_team_attributes`](#kenjoteamsupdate_team_attributes)
  * [`kenjo.time_off.get_requests_by_date`](#kenjotime_offget_requests_by_date)
  * [`kenjo.user_accounts.list_employees`](#kenjouser_accountslist_employees)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Kenjo&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from kenjo_python_sdk import Kenjo, ApiException

kenjo = Kenjo()

try:
    create_new_area_response = kenjo.areas.create_new_area(
        authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
        name="Recruiting feature",
    )
    print(create_new_area_response)
except ApiException as e:
    print("Exception when calling AreasApi.create_new_area: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from kenjo_python_sdk import Kenjo, ApiException

kenjo = Kenjo()


async def main():
    try:
        create_new_area_response = await kenjo.areas.acreate_new_area(
            authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
            name="Recruiting feature",
        )
        print(create_new_area_response)
    except ApiException as e:
        print("Exception when calling AreasApi.create_new_area: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["code"])
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from kenjo_python_sdk import Kenjo, ApiException

kenjo = Kenjo()

try:
    create_new_area_response = kenjo.areas.raw.create_new_area(
        authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
        name="Recruiting feature",
    )
    pprint(create_new_area_response.body)
    pprint(create_new_area_response.body["id"])
    pprint(create_new_area_response.body["name"])
    pprint(create_new_area_response.headers)
    pprint(create_new_area_response.status)
    pprint(create_new_area_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AreasApi.create_new_area: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `kenjo.areas.create_new_area`<a id="kenjoareascreate_new_area"></a>

Creates a new area.<br>The *name* is the only required field.<br>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_area_response = kenjo.areas.create_new_area(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Recruiting feature",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the area to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AreasCreateNewAreaRequest`](./kenjo_python_sdk/type/areas_create_new_area_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AreasCreateNewAreaResponse`](./kenjo_python_sdk/pydantic/areas_create_new_area_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/areas` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.areas.get_by_id`<a id="kenjoareasget_by_id"></a>

Returns the area referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kenjo.areas.get_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the area entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`AreasGetByIdResponse`](./kenjo_python_sdk/pydantic/areas_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/areas/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.areas.get_list`<a id="kenjoareasget_list"></a>

Returns a list of the existing areas in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.areas.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`AreasGetListResponse`](./kenjo_python_sdk/pydantic/areas_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/areas` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.areas.remove_by_id`<a id="kenjoareasremove_by_id"></a>

Removes the area referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kenjo.areas.remove_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the area entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/areas/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.areas.update_area_by_id`<a id="kenjoareasupdate_area_by_id"></a>

Updates a area referenced by *id*. Only the attributes submitted are modified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_area_by_id_response = kenjo.areas.update_area_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Sales",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the area entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the area to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AreasUpdateAreaByIdRequest`](./kenjo_python_sdk/type/areas_update_area_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AreasUpdateAreaByIdResponse`](./kenjo_python_sdk/pydantic/areas_update_area_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/areas/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.create_entry`<a id="kenjoattendancecreate_entry"></a>

This endpoint creates an attendance entry for a one employee, so an user *identifier* is required to build this relationship. The following *identifiers* are the valid ones: **userId**, **email** or **externalId**. Also one **startTime** and one **date** are required.<br>The new entry will have an unique identifier **_id**. This value is returned in the body response.<br><br> A day accepts many attendance entries per employee but they cannot be overlapped. It means that if, for example, *there is an entry the 2021-06-10 between 09:00 and 10:00 for the user E-111, then the creation of an new entry for E-111 in the 2021-06-10 whose startDate or endDate is between 09:00 and 10:00 will become a BAD REQUEST*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_entry_response = kenjo.attendance.create_entry(
    date="2021-07-01",
    start_time="36000",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    user_id="50a2db290da29e126a18789a",
    email="john@acme.io",
    external_id="00001",
    end_time="46800",
    breaks=[
        {
            "start": "39600",
            "end": "41400",
        }
    ],
    comment="Morning working attendance tracking.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `str`<a id="date-str"></a>

The date of the entry. The valid format is *YYYY-MM-DD*. Required field.

##### start_time: `str`<a id="start_time-str"></a>

The start time of the entry. The valid format is *hh:mm:ss*. Required field.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### user_id: `str`<a id="user_id-str"></a>

The Kenjo employee *_id*.

##### email: `str`<a id="email-str"></a>

The Kenjo *email* for an employee.

##### external_id: `str`<a id="external_id-str"></a>

The *external id* for an employee for integrations.

##### end_time: `str`<a id="end_time-str"></a>

The end time of the entry. It is not a required field but cannot be less or equal than the *startTime*. The valid format is *hh:mm:ss*

##### breaks: [`AttendanceCreateEntryRequestBreaks`](./kenjo_python_sdk/type/attendance_create_entry_request_breaks.py)<a id="breaks-attendancecreateentryrequestbreakskenjo_python_sdktypeattendance_create_entry_request_breakspy"></a>

##### comment: `str`<a id="comment-str"></a>

Optional text to describe an attendance record (pair of startTime and endTime). The maximum number of characters is 150.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AttendanceCreateEntryRequest`](./kenjo_python_sdk/type/attendance_create_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceCreateEntryResponse`](./kenjo_python_sdk/pydantic/attendance_create_entry_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.create_track_time`<a id="kenjoattendancecreate_track_time"></a>

This endpoint tracks time only providing the following information: **employee identifier** and a **date time**. The following identifiers are the valid ones: **userId**, **email** or **externalId**, only one of them is required. This action abstracts and simplifies the entries tracking, ensuring internally the order and transforming each track action to a Kenjo user attendance format.<br><br>Example: Three calls for the employee E-111 to the */track-time* endpoint contains the following data:<br>T1: 2021-01-01T08:00:00<br>T2: 2021-01-01T09:00:00<br>T3: 2021-01-01T10:00:00<br>The three calls order is T1, T2, T3.<br><br>Then in Kenjo there will be 2 attendance pairs:<br>1: 08:00 / 09:00<br>2: 10:00 / --:--<br>The second pair is open, with no **endTime** info, until a new one comes. <br><br>If there is a new track: 2021-01-01T12:00:00, then the result will be:<br>1: 08:00 / 09:00<br>2: 10:00 / 12:00<br>If the track is 2021-01-01T07:00:00 instead, then the previous tracks are reordered to be consistent with concept of attendance pairs:<br>1: 07:00 / 08:00<br>2: 09:00 / 10:00

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_track_time_response = kenjo.attendance.create_track_time(
    date_time="2021-07-01T09:00:00",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    user_id="50a2db290da29e126a18789a",
    email="john@acme.io",
    external_id="00001",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date_time: `str`<a id="date_time-str"></a>

The date and the time of the Kenjo employee in format YYYY-MM-DDThh:mm:ss.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### user_id: `str`<a id="user_id-str"></a>

The Kenjo employee *_id*.

##### email: `str`<a id="email-str"></a>

The Kenjo *email* for an employee.

##### external_id: `str`<a id="external_id-str"></a>

The *external id* for an employee for integrations.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AttendanceCreateTrackTimeRequest`](./kenjo_python_sdk/type/attendance_create_track_time_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceCreateTrackTimeResponse`](./kenjo_python_sdk/pydantic/attendance_create_track_time_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances/track-time` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.get_by_id`<a id="kenjoattendanceget_by_id"></a>

This endpoint returns one attendance entry specified by  **attendanceId**.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kenjo.attendance.get_by_id(
    attendance_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attendance_id: `str`<a id="attendance_id-str"></a>

The _id of the attendance entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceGetByIdResponse`](./kenjo_python_sdk/pydantic/attendance_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances/{attendanceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.get_categories`<a id="kenjoattendanceget_categories"></a>

This endpoint returns an array of objects. Every object contains an attendance category.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_categories_response = kenjo.attendance.get_categories(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceGetCategoriesResponse`](./kenjo_python_sdk/pydantic/attendance_get_categories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.get_expected_time_by_user`<a id="kenjoattendanceget_expected_time_by_user"></a>

This endpoint returns a paginated list of expected time by user for a given date range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_expected_time_by_user_response = kenjo.attendance.get_expected_time_by_user(
    _from="2020-01-01",
    to="2020-01-10",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    company_id="80a2db290da29e126a18789a",
    office_id="80a2db290da29e126a18789d",
    department_id="80a2db290da29e126a18789c",
    user_id="80a2db290da29e126a18789c",
    offset=1,
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

A date in format YYYY-MM-DD to indicate the starting point.

##### to: `str`<a id="to-str"></a>

A date in format YYYY-MM-DD to indicate the ending point.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### company_id: `str`<a id="company_id-str"></a>

Optional filter. The company id of the Kenjo employee.

##### office_id: `str`<a id="office_id-str"></a>

Optional filter. The office id of the Kenjo employee.

##### department_id: `str`<a id="department_id-str"></a>

Optional filter. The department id of the Kenjo employee.

##### user_id: `str`<a id="user_id-str"></a>

Optional filter. The id of the Kenjo employee. It accepts 2 formats:<br><br> 1. An unique string with the Kenjo employee id. <br>Example: *userId=80a2db290da29e126a18789c* <br><br> 2. A string with more than one Kenjo employee ids separated by commas (until 15 ids as maximum). <br>Example: *userId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

Optional filter for pagination proposals. Determines the number of pages to skip when pagination is being used. If this value is not provided, by default the offset will be 1.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Optional filter for pagination proposals. The maximum number of rows to retrieve which determines the size of the page. If this value is not provided then the limit will be 50 users. The maximum value of the limit is 100 users per page. Only are valid the following limit values: 25, 50 and 100.

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceGetExpectedTimeByUserResponse`](./kenjo_python_sdk/pydantic/attendance_get_expected_time_by_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances/expected-time` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.get_list`<a id="kenjoattendanceget_list"></a>

This endpoint returns an array of objects with all the existing attendance entries within Kenjo for a maximum of 31 days, defined by the required params **from** and **to**. Every object contains an attendance entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.attendance.get_list(
    _from="2021-02-01",
    to="2021-02-04",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

A date in format YYYY-MM-DD to indicate the starting point.

##### to: `str`<a id="to-str"></a>

A date in format YYYY-MM-DD to indicate the ending point.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceGetListResponse`](./kenjo_python_sdk/pydantic/attendance_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.remove_by_id`<a id="kenjoattendanceremove_by_id"></a>

This endpoint delete the attendance entry specified by **attendanceId**.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kenjo.attendance.remove_by_id(
    attendance_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attendance_id: `str`<a id="attendance_id-str"></a>

The Kenjo _id of the attendance entry to remove.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances/{attendanceId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.attendance.update_entry`<a id="kenjoattendanceupdate_entry"></a>

This endpoint updates the attendance entry specified by **attendanceId**. Only the fields submitted in the body will be updated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_entry_response = kenjo.attendance.update_entry(
    attendance_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    start_time="36000",
    end_time="36000",
    breaks=[
        {
            "start": "39600",
            "end": "41400",
        }
    ],
    comment="Morning working attendance tracking.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attendance_id: `str`<a id="attendance_id-str"></a>

The _id of the attendance entry to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### start_time: `str`<a id="start_time-str"></a>

The new start time of the attendance entry to update. The valid format is *hh:mm:ss*

##### end_time: `str`<a id="end_time-str"></a>

The new end time of the attendance entry to update. The valid format is *hh:mm:ss*

##### breaks: [`AttendanceUpdateEntryRequestBreaks`](./kenjo_python_sdk/type/attendance_update_entry_request_breaks.py)<a id="breaks-attendanceupdateentryrequestbreakskenjo_python_sdktypeattendance_update_entry_request_breakspy"></a>

##### comment: `str`<a id="comment-str"></a>

Optional text to describe an attendance record (pair of startTime and endTime). The maximum number of characters is 150.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AttendanceUpdateEntryRequest`](./kenjo_python_sdk/type/attendance_update_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceUpdateEntryResponse`](./kenjo_python_sdk/pydantic/attendance_update_entry_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendances/{attendanceId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.authentication.create_bearer_token`<a id="kenjoauthenticationcreate_bearer_token"></a>

Create a bearer token to allow connecting the API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bearer_token_response = kenjo.authentication.create_bearer_token(
    api_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

The API key generated in Settings.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationCreateBearerTokenRequest`](./kenjo_python_sdk/type/authentication_create_bearer_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationCreateBearerTokenResponse`](./kenjo_python_sdk/pydantic/authentication_create_bearer_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/login` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.authentication.invalidate_token`<a id="kenjoauthenticationinvalidate_token"></a>

Invalidates a Bearer token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kenjo.authentication.invalidate_token()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/logout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.calendars.get_by_id`<a id="kenjocalendarsget_by_id"></a>

Returns the calendar referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kenjo.calendars.get_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the calendar entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`CalendarsGetByIdResponse`](./kenjo_python_sdk/pydantic/calendars_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/calendars/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.calendars.get_list`<a id="kenjocalendarsget_list"></a>

Returns a list of the existing calendars in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.calendars.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Madrid Calendar",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The calendar name.

#### 🔄 Return<a id="🔄-return"></a>

[`CalendarsGetListResponse`](./kenjo_python_sdk/pydantic/calendars_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/calendars` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.companies.get_list`<a id="kenjocompaniesget_list"></a>

Returns a list of the existing companies in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.companies.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="ACME Ltd",
    city="Madrid",
    country="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The name of the company.

##### city: `str`<a id="city-str"></a>

The city of the company.

##### country: `str`<a id="country-str"></a>

The country code of the company in ISO 3166-1 alpha-2.

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetListResponse`](./kenjo_python_sdk/pydantic/companies_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.compensation.get_contracts`<a id="kenjocompensationget_contracts"></a>

This endpoint returns a paginated list of employment contracts. The URL params help to return more accurate results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contracts_response = kenjo.compensation.get_contracts(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    contract_type_id="60a2db290da29e126a18789e",
    user_id="60a2db290da29e126a18789b",
    company_id="90a2db290da29e126a187891",
    offset=1,
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### contract_type_id: `str`<a id="contract_type_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *contractTypeId*. It can accept two formats:<br><br> 1. A single *contractTypeId* as a unique string. <br>Example: *contractTypeId=80a2db290da29e126a18789c* <br><br> 2. Multiple *contractTypeId* values separated by commas (up to a maximum of 15 values). <br>Example: *contractTypeId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### user_id: `str`<a id="user_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *_userId*. It can accept two formats:<br><br> 1. A single *_userId* as a unique string. <br>Example: *_userId=80a2db290da29e126a18789c* <br><br> 2. Multiple *_userId* values separated by commas (up to a maximum of 15 values). <br>Example: *_userId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### company_id: `str`<a id="company_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *_companyId*. It can accept two formats:<br><br> 1. A single *_companyId* as a unique string. <br>Example: *_companyId=80a2db290da29e126a18789c* <br><br> 2. Multiple *_companyId* values separated by commas (up to a maximum of 15 values). <br>Example: *_companyId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

Optional filter for pagination proposals. Determines the number of pages to skip when pagination is being used. If this value is not provided, by default the offset will be 1.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Optional filter for pagination proposals. The maximum number of rows to retrieve which determines the size of the page. If this value is not provided then the limit will be 50 users. The maximum value of the limit is 100 users per page. Only are valid the following limit values: 25, 50 and 100.

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationGetContractsResponse`](./kenjo_python_sdk/pydantic/compensation_get_contracts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/contracts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.compensation.get_salaries_list`<a id="kenjocompensationget_salaries_list"></a>

This endpoint returns a paginated list of employment salaries. The URL params help to return more accurate results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_salaries_list_response = kenjo.compensation.get_salaries_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    user_id="60a2db290da29e126a18789b",
    company_id="90a2db290da29e126a187891",
    payment_period="Annual",
    currency="EUR",
    offset=1,
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### user_id: `str`<a id="user_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *_userId*. It can accept two formats:<br><br> 1. A single *_userId* as a unique string. <br>Example: *_userId=80a2db290da29e126a18789c* <br><br> 2. Multiple *_userId* values separated by commas (up to a maximum of 15 values). <br>Example: *_userId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### company_id: `str`<a id="company_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *_companyId*. It can accept two formats:<br><br> 1. A single *_companyId* as a unique string. <br>Example: *_companyId=80a2db290da29e126a18789c* <br><br> 2. Multiple *_companyId* values separated by commas (up to a maximum of 15 values). <br>Example: *_companyId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### payment_period: `str`<a id="payment_period-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *paymentPeriod*. Accepted values: 'Annual', 'Monthly' and 'Hourly'. It can accept two formats:<br><br> 1. A single *paymentPeriod* as a unique string. <br>Example: *paymentPeriod=Annual* <br><br> 2. Multiple *paymentPeriod* values separated by commas (up to a maximum of 15 values). <br>Example: *paymentPeriod=Annual,Monthly*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### currency: `str`<a id="currency-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *currency* (ISO 4217). It can accept two formats:<br><br> 1. A single *currency* as a unique string. <br>Example: *currency=EUR* <br><br> 2. Multiple *currency* values separated by commas (up to a maximum of 15 values). <br>Example: *currency=EUR,USD*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

Optional filter for pagination proposals. Determines the number of pages to skip when pagination is being used. If this value is not provided, by default the offset will be 1.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Optional filter for pagination proposals. The maximum number of rows to retrieve which determines the size of the page. If this value is not provided then the limit will be 50 users. The maximum value of the limit is 100 users per page. Only are valid the following limit values: 25, 50 and 100.

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationGetSalariesListResponse`](./kenjo_python_sdk/pydantic/compensation_get_salaries_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/salaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.compensation.list_additional_payment_types`<a id="kenjocompensationlist_additional_payment_types"></a>

This endpoint returns a paginated list of additional payment types. The URL params help to return more accurate results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_additional_payment_types_response = kenjo.compensation.list_additional_payment_types(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    offset=1,
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

Optional filter for pagination proposals. Determines the number of pages to skip when pagination is being used. If this value is not provided, by default the offset will be 1.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Optional filter for pagination proposals. The maximum number of rows to retrieve which determines the size of the page. If this value is not provided then the limit will be 50 users. The maximum value of the limit is 100 users per page. Only are valid the following limit values: 25, 50 and 100.

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationListAdditionalPaymentTypesResponse`](./kenjo_python_sdk/pydantic/compensation_list_additional_payment_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/additional-payment-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.compensation.list_additional_payments`<a id="kenjocompensationlist_additional_payments"></a>

This endpoint returns a paginated list of additional payments. The URL params help to return more accurate results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_additional_payments_response = kenjo.compensation.list_additional_payments(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    user_id="60a2db290da29e126a18789b",
    company_id="90a2db290da29e126a187891",
    currency="EUR",
    offset=1,
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### user_id: `str`<a id="user_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *_userId*. It can accept two formats:<br><br> 1. A single *_userId* as a unique string. <br>Example: *_userId=80a2db290da29e126a18789c* <br><br> 2. Multiple *_userId* values separated by commas (up to a maximum of 15 values). <br>Example: *_userId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### company_id: `str`<a id="company_id-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *_companyId*. It can accept two formats:<br><br> 1. A single *_companyId* as a unique string. <br>Example: *_companyId=80a2db290da29e126a18789c* <br><br> 2. Multiple *_companyId* values separated by commas (up to a maximum of 15 values). <br>Example: *_companyId=80a2db290da29e126a18789c,80a2db290da29e126a18789b,80a2db290da29e126a187891*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### currency: `str`<a id="currency-str"></a>

Optional filter. This field allows you to retrieve contracts based on their *currency* (ISO 4217). It can accept two formats:<br><br> 1. A single *currency* as a unique string. <br>Example: *currency=EUR* <br><br> 2. Multiple *currency* values separated by commas (up to a maximum of 15 values). <br>Example: *currency=EUR,USD*. These options provide flexibility in filtering contracts by their type, making it easier to retrieve the specific data you need.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

Optional filter for pagination proposals. Determines the number of pages to skip when pagination is being used. If this value is not provided, by default the offset will be 1.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Optional filter for pagination proposals. The maximum number of rows to retrieve which determines the size of the page. If this value is not provided then the limit will be 50 users. The maximum value of the limit is 100 users per page. Only are valid the following limit values: 25, 50 and 100.

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationListAdditionalPaymentsResponse`](./kenjo_python_sdk/pydantic/compensation_list_additional_payments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/additional-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.compensation.list_contract_types`<a id="kenjocompensationlist_contract_types"></a>

This endpoint returns a paginated list of contract types. The URL params help to return more accurate results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_contract_types_response = kenjo.compensation.list_contract_types(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### is_active: `bool`<a id="is_active-bool"></a>

This field allows to return only the active contract types.

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationListContractTypesResponse`](./kenjo_python_sdk/pydantic/compensation_list_contract_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/compensation/contract-types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.custom_fields.get_list`<a id="kenjocustom_fieldsget_list"></a>

Returns a list of the existing custom fields in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.custom_fields.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    section="personal",
    label="Blood type",
    api_name="c_Bloodtype",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### section: `str`<a id="section-str"></a>

The name of custom field section.

##### label: `str`<a id="label-str"></a>

The name of the custom field label.

##### api_name: `str`<a id="api_name-str"></a>

The api name is a required identifier to perform POST and PUT operations with employees.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetListResponse`](./kenjo_python_sdk/pydantic/custom_fields_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom-fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.departments.create_new_department`<a id="kenjodepartmentscreate_new_department"></a>

Creates a new department.<br>The *name* is the only required field.<br>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_department_response = kenjo.departments.create_new_department(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Sales",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the department to update. Required field.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsCreateNewDepartmentRequest`](./kenjo_python_sdk/type/departments_create_new_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsCreateNewDepartmentResponse`](./kenjo_python_sdk/pydantic/departments_create_new_department_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.departments.get_by_id`<a id="kenjodepartmentsget_by_id"></a>

Returns the department referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kenjo.departments.get_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the department entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsGetByIdResponse`](./kenjo_python_sdk/pydantic/departments_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/departments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.departments.list_departments`<a id="kenjodepartmentslist_departments"></a>

Returns a list of the existing departments in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_departments_response = kenjo.departments.list_departments(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Happiness dept.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The department name.

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsListDepartmentsResponse`](./kenjo_python_sdk/pydantic/departments_list_departments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.departments.remove_by_id`<a id="kenjodepartmentsremove_by_id"></a>

Removes the department referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kenjo.departments.remove_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the department entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/departments/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.departments.update_attributes`<a id="kenjodepartmentsupdate_attributes"></a>

Updates a deparment referenced by *id*. Only the attributes submitted are modified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_attributes_response = kenjo.departments.update_attributes(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Sales",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the deparment entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the department to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsUpdateAttributesRequest`](./kenjo_python_sdk/type/departments_update_attributes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsUpdateAttributesResponse`](./kenjo_python_sdk/pydantic/departments_update_attributes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/departments/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.activate_employee`<a id="kenjoemployeesactivate_employee"></a>

This endpoint activates a Kenjo employee given by the employeeId. It sends an email to the recipient of the employee email to start the onboarding process. Once the password is filled, the employee changes to 'active' ('isActive' = TRUE). While the employee is not active it is possible to send activation emails.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_employee_response = kenjo.employees.activate_employee(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to send the activation email.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/activate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.create_inactive_employee`<a id="kenjoemployeescreate_inactive_employee"></a>

This endpoint creates a deactivated employee in Kenjo, the 'isActive' field set to false. To activate an employee use the put /activate method. This method will send an activation message to the employee email to complete the activation through the onboarding wizard.
<br><br>The field *email* is required and must be unique. Also *firstName*, *lastName* and *companyId* are required fields. If the work schedule is not provided then all the days of the week except Saturdays and Sundays are set to true. If the *language* is not specified, the assigned company language will be set by default.
<br><br>**Custom fields** information can be provided in this operation for the **personal**, **work**, **address**, **financial** and **home** sections. The *API name* of the custom field is required and the data format has to match with the type defined for the custom field in Kenjo.
API names start with 'c_' and the rest is composed by the trimmed name (spaces are removed).
<br><br>
Example:
<br>
*The custom field 'Activity type' belongs to the section 'work'*:
  ```
...
{
  ...
    "work": {
      "c_Activitytype": "1",
      ...
    },
  ...
}
```
*'Activity type' is a field type 'List' (Strings list) with the possible values: "1", "2" and "3". It means that if a different value or type is provided then the request will return an error.*
<br><br>If the operation get success then an inactive employee is created and the response will include the provided information and the Kenjo id for the new employee.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_inactive_employee_response = kenjo.employees.create_inactive_employee(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    account={
        "email": "john@acme.io",
        "language": "es",
        "external_id": "E-000001",
    },
    personal={
        "first_name": "John",
        "last_name": "Doe",
        "display_name": "John Doe",
        "gender": "Male",
        "birthdate": "1980-01-28T00:00:00.000Z",
    },
    work={
        "company_id": "50a2db290da29e126a187894",
        "office_id": "50a2db290da29e126a187895",
        "department_id": "50a2db290da29e126a187896",
        "start_date": "2022-01-01T00:00:00.000Z",
        "job_title": "Actor",
        "work_phone": "+34 666 70 90 32",
        "work_mobile": "+34 680 70 90 32",
        "is_assistant": False,
        "probation_period_end": "2022-06-01T00:00:00.000Z",
        "reports_to_id": "50a2db290da29e126a1878523",
        "weekly_hours": 40,
    },
    work_schedule={
        "monday_working_day": True,
        "tuesday_working_day": True,
        "wednesday_working_day": True,
        "thursday_working_day": True,
        "friday_working_day": True,
        "saturday_working_day": True,
        "sunday_working_day": True,
        "track_attendance": True,
    },
    address={
        "street": "Calle Enrique San Francisco 13",
        "postal_code": "28080",
        "city": "Madrid",
        "country": "ES",
    },
    financial={
        "account_holder_name": "Michael Corleone",
        "bank_name": "Bank of Sicily",
        "account_number": "0093 344 2132221 3304 00",
        "iban": "DE32120222391919191911",
        "swift_code": "12321234",
        "national_id": "04123547X",
        "passport": "FA1234098",
        "national_insurance_number": "23123312321",
        "tax_code": "323451R",
        "tax_identification_number": "T4312345",
    },
    home={
        "marital_status": "Widowed",
        "spouse_first_name": "Catherine",
        "spouse_last_name": "Tramell",
        "spouse_birthdate": "2060-01-26T00:00:00.000Z",
        "spouse_gender": "Female",
        "personal_email": "john@acme.io",
        "personal_phone": "4567092323",
        "personal_mobile": "3567092310",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### account: [`EmployeesCreateInactiveEmployeeRequestAccount`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_account.py)<a id="account-employeescreateinactiveemployeerequestaccountkenjo_python_sdktypeemployees_create_inactive_employee_request_accountpy"></a>


##### personal: [`EmployeesCreateInactiveEmployeeRequestPersonal`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_personal.py)<a id="personal-employeescreateinactiveemployeerequestpersonalkenjo_python_sdktypeemployees_create_inactive_employee_request_personalpy"></a>


##### work: [`EmployeesCreateInactiveEmployeeRequestWork`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_work.py)<a id="work-employeescreateinactiveemployeerequestworkkenjo_python_sdktypeemployees_create_inactive_employee_request_workpy"></a>


##### work_schedule: [`EmployeesCreateInactiveEmployeeRequestWorkSchedule`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_work_schedule.py)<a id="work_schedule-employeescreateinactiveemployeerequestworkschedulekenjo_python_sdktypeemployees_create_inactive_employee_request_work_schedulepy"></a>


##### address: [`EmployeesCreateInactiveEmployeeRequestAddress`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_address.py)<a id="address-employeescreateinactiveemployeerequestaddresskenjo_python_sdktypeemployees_create_inactive_employee_request_addresspy"></a>


##### financial: [`EmployeesCreateInactiveEmployeeRequestFinancial`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_financial.py)<a id="financial-employeescreateinactiveemployeerequestfinancialkenjo_python_sdktypeemployees_create_inactive_employee_request_financialpy"></a>


##### home: [`EmployeesCreateInactiveEmployeeRequestHome`](./kenjo_python_sdk/type/employees_create_inactive_employee_request_home.py)<a id="home-employeescreateinactiveemployeerequesthomekenjo_python_sdktypeemployees_create_inactive_employee_request_homepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesCreateInactiveEmployeeRequest`](./kenjo_python_sdk/type/employees_create_inactive_employee_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesCreateInactiveEmployeeResponse`](./kenjo_python_sdk/pydantic/employees_create_inactive_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.deactivate_employee_by_id`<a id="kenjoemployeesdeactivate_employee_by_id"></a>

This endpoint deactivates a Kenjo employee given by the employeeId. It sets the isActive field to FALSE and invalidate the access Kenjo for the employee. While the employee is not active it is possible to send activation emails.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deactivate_employee_by_id_response = kenjo.employees.deactivate_employee_by_id(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/deactivate` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.get_accounts`<a id="kenjoemployeesget_accounts"></a>

This endpoint returns a list with the **account** sections of the existing employees. The account section contains information such as *email*, *external Id*, *language* and *activation status*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_accounts_response = kenjo.employees.get_accounts(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    email="john.doe@acme.com",
    language="es",
    external_id="USER-123456",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### email: `str`<a id="email-str"></a>

The Kenjo email of the employee.

##### language: `str`<a id="language-str"></a>

The employee language.

##### external_id: `str`<a id="external_id-str"></a>

The external id of the employee.

##### is_active: `bool`<a id="is_active-bool"></a>

The employee activation status.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetAccountsResponse`](./kenjo_python_sdk/pydantic/employees_get_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.get_employee_information`<a id="kenjoemployeesget_employee_information"></a>

This endpoint returns information about the **account**, **personal**, **work**, **work schedule**, **address**, **financial** and **home** sections for a given employee id. The *employeeId* param represents a Kenjo employee id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_information_response = kenjo.employees.get_employee_information(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    employee_id="50a2db290da29e126a187843",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to request.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetEmployeeInformationResponse`](./kenjo_python_sdk/pydantic/employees_get_employee_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.get_list`<a id="kenjoemployeesget_list"></a>

This endpoint returns the list of employee accounts existing in Kenjo. It is similar to the */employees/accounts* endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.employees.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetListResponse`](./kenjo_python_sdk/pydantic/employees_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.get_work_schedules`<a id="kenjoemployeesget_work_schedules"></a>

This endpoint returns a list with the **work schedule** sections of the existing employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_schedules_response = kenjo.employees.get_work_schedules(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    track_attendance=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### track_attendance: `bool`<a id="track_attendance-bool"></a>

The activation status of attendance tracking for the employee.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesGetWorkSchedulesResponse`](./kenjo_python_sdk/pydantic/employees_get_work_schedules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/work-schedules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.list_addresses`<a id="kenjoemployeeslist_addresses"></a>

This endpoint returns a list with the **address** sections of the existing employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_addresses_response = kenjo.employees.list_addresses(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    street=" Calle Enrique San Francisco 13",
    postal_code="28080",
    city="Madrid",
    country="ES",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### street: `str`<a id="street-str"></a>

The name of the street.

##### postal_code: `str`<a id="postal_code-str"></a>

The postal code.

##### city: `str`<a id="city-str"></a>

The city.

##### country: `str`<a id="country-str"></a>

The country code in ISO 3166-1 alpha-2.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesListAddressesResponse`](./kenjo_python_sdk/pydantic/employees_list_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.list_financials`<a id="kenjoemployeeslist_financials"></a>

This endpoint returns a list with the **financial** sections of the existing employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_financials_response = kenjo.employees.list_financials(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    account_holder_name="Michael Corleone",
    bank_name="Bank of Sicily",
    account_number="0093 344 2132221 3304 00",
    iban="DE32120222391919191911",
    swift_code="12321234",
    national_id="04123547X",
    passport="FA1234098",
    national_insurance_number="23123312321",
    tax_code="323451R",
    tax_identification_number="T4312345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### account_holder_name: `str`<a id="account_holder_name-str"></a>

The accounts holder's name.

##### bank_name: `str`<a id="bank_name-str"></a>

The bank name.

##### account_number: `str`<a id="account_number-str"></a>

The account number.

##### iban: `str`<a id="iban-str"></a>

The IBAN.

##### swift_code: `str`<a id="swift_code-str"></a>

The SWIFT code.

##### national_id: `str`<a id="national_id-str"></a>

The national id document

##### passport: `str`<a id="passport-str"></a>

The passport number.

##### national_insurance_number: `str`<a id="national_insurance_number-str"></a>

The national insurance number.

##### tax_code: `str`<a id="tax_code-str"></a>

The tax number.

##### tax_identification_number: `str`<a id="tax_identification_number-str"></a>

The tax identification number.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesListFinancialsResponse`](./kenjo_python_sdk/pydantic/employees_list_financials_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/financials` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.list_homes`<a id="kenjoemployeeslist_homes"></a>

This endpoint returns a list with the **home** sections of the existing employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_homes_response = kenjo.employees.list_homes(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    marital_status="Widowed",
    spouse_first_name="Catherine",
    spouse_last_name="Tramell",
    spouse_birthdate="2060-01-26T00:00:00.000Z",
    spouse_gender="Female",
    personal_email="john.doe@acme.com",
    personal_phone="4567092323",
    personal_mobile="3567092310",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### marital_status: `str`<a id="marital_status-str"></a>

The marital status. Only is valid one of the following values \"Divorced\", \"Domestic Partnership\", \"Married\", \"Separated\", \"Single\", \"Widowed\".

##### spouse_first_name: `str`<a id="spouse_first_name-str"></a>

The first name of the employee's spouse.

##### spouse_last_name: `str`<a id="spouse_last_name-str"></a>

The last name of the employee's spouse.

##### spouse_birthdate: `str`<a id="spouse_birthdate-str"></a>

The birth date of the employee's spouse. Format YYYY-MM-DDThh:mm:ss.000Z.

##### spouse_gender: `str`<a id="spouse_gender-str"></a>

The employee's spouse gender. Only is valid one of the following values 'Male' (male), 'Female' (female) or 'Other' (other).

##### personal_email: `str`<a id="personal_email-str"></a>

The employee personal email.

##### personal_phone: `str`<a id="personal_phone-str"></a>

The employee personal phone.

##### personal_mobile: `str`<a id="personal_mobile-str"></a>

The employee personal mobile.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesListHomesResponse`](./kenjo_python_sdk/pydantic/employees_list_homes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/homes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.list_personals`<a id="kenjoemployeeslist_personals"></a>

This endpoint returns a list with the **personal** sections of the existing employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_personals_response = kenjo.employees.list_personals(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    first_name="John",
    last_name="Doe",
    display_name="John Doe",
    gender="es",
    birthdate="1980-01-28T00:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### first_name: `str`<a id="first_name-str"></a>

The name of the Kenjo employee. This field is required.

##### last_name: `str`<a id="last_name-str"></a>

The surname of the Kenjo employee. This field is required.

##### display_name: `str`<a id="display_name-str"></a>

The composition of firstName and lastName of the Kenjo employee.

##### gender: `str`<a id="gender-str"></a>

The employee gender. Only is valid one of the following values 'Male' (male), 'Female' (female) or 'Other' (other).

##### birthdate: `str`<a id="birthdate-str"></a>

The employee birth date. Format YYYY-MM-DDThh:00:00.000Z.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesListPersonalsResponse`](./kenjo_python_sdk/pydantic/employees_list_personals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/personals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.list_works`<a id="kenjoemployeeslist_works"></a>

This endpoint returns a list with the **work** sections of the existing employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_works_response = kenjo.employees.list_works(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    company_id="80a2db290da29e126a18789a",
    office_id="80a2db290da29e126a18789d",
    department_id="80a2db290da29e126a18789c",
    start_date="2022-06-01T00:00:00.000Z",
    job_title="Actor",
    work_phone="34 666 70 90 32",
    work_mobile="34 680 70 90 32",
    is_assistant=True,
    probation_period_end="2022-06-01T00:00:00.000Z",
    reports_to_id="80a2db290da29e126a187891",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### company_id: `str`<a id="company_id-str"></a>

The company id of the Kenjo employee.

##### office_id: `str`<a id="office_id-str"></a>

The office id of the Kenjo employee.

##### department_id: `str`<a id="department_id-str"></a>

The department id of the Kenjo employee.

##### start_date: `str`<a id="start_date-str"></a>

The starting date of the Kenjo employee in format YYYY-MM-DDThh:mm:ss.

##### job_title: `str`<a id="job_title-str"></a>

The job title of the employee.

##### work_phone: `str`<a id="work_phone-str"></a>

The work phone of the employee.

##### work_mobile: `str`<a id="work_mobile-str"></a>

The work mobile of the employee.

##### is_assistant: `bool`<a id="is_assistant-bool"></a>

Allow to indicate if the employee has or not the assistant role.

##### probation_period_end: `str`<a id="probation_period_end-str"></a>

The probation period of the employee. Format YYYY-MM-DDThh:mm:ss.000Z.

##### reports_to_id: `str`<a id="reports_to_id-str"></a>

The Kenjo employee id of the user to whom the employee reports. The employee id to assign can be an active or inactive user. Trying to assign the own employee id or the id of someone who is already reporting will arise an error.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesListWorksResponse`](./kenjo_python_sdk/pydantic/employees_list_works_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/works` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_address`<a id="kenjoemployeesupdate_address"></a>

This endpoint updates the employee **address** section for a given employee id. The operation only updates the fields provided in the body.
<br><br>**Custom fields** information can be provided in this operation. The *API name* of the custom field is required and the data format has to match with the type defined for the custom field in Kenjo.
API names start with 'c_' and the rest is composed by the trimmed name (spaces are removed).
<br><br>
Example:
<br>
*The custom field 'province' belongs to the 'address' section*:
  ```
  {
    ...,
    "country": "ES",
    "c_province": "MD",
    ...
  }
```
*'province' is a field type 'String'. It means that if a different type of data (number or boolean) is provided then the request will return an error.*


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_address_response = kenjo.employees.update_address(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    street="string_example",
    postal_code="string_example",
    city="string_example",
    country="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### street: `str`<a id="street-str"></a>

The name of the street.

##### postal_code: `str`<a id="postal_code-str"></a>

The postal code.

##### city: `str`<a id="city-str"></a>

The city.

##### country: `str`<a id="country-str"></a>

The country code in ISO 3166-1 alpha-2.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateAddressRequest`](./kenjo_python_sdk/type/employees_update_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdateAddressResponse`](./kenjo_python_sdk/pydantic/employees_update_address_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/addresses` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_employee_accounts`<a id="kenjoemployeesupdate_employee_accounts"></a>

This endpoint updates the employee **account** section for a given employee id. The operation only updates the fields provided in the body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_accounts_response = kenjo.employees.update_employee_accounts(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    email="john@acme.io",
    external_id="E-000001",
    language="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### email: `str`<a id="email-str"></a>

The employee email in Kenjo. This is an unique identifier and required.

##### external_id: `str`<a id="external_id-str"></a>

The employee external id for integration proposals. This value must be unique.

##### language: `str`<a id="language-str"></a>

The employee language. Only is valid one of the following values 'en' (english), 'es' (spanish) or 'de' (german).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateEmployeeAccountsRequest`](./kenjo_python_sdk/type/employees_update_employee_accounts_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdateEmployeeAccountsResponse`](./kenjo_python_sdk/pydantic/employees_update_employee_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/accounts` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_financials`<a id="kenjoemployeesupdate_financials"></a>

This endpoint updates the employee **financial** section for a given employee id. The operation only updates the fields provided in the body.
<br><br>**Custom fields** information can be provided in this operation. The *API name* of the custom field is required and the data format has to match with the type defined for the custom field in Kenjo.
API names start with 'c_' and the rest is composed by the trimmed name (spaces are removed).
<br><br>
Example:
<br>
*The custom field 'special tax' belongs to the 'financial' section*:
  ```
  {
    ...,
    "iban": "ES2345123456789077",
    "c_specialtax": 1500,
    ...
  }
```
*'special tax' is a field type 'Number'. It means that if a different type of data (string or boolean) is provided then the request will return an error.*


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_financials_response = kenjo.employees.update_financials(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    account_holder_name="Michael Corleone",
    bank_name="Bank of Sicily",
    account_number="0093 344 2132221 3304 00",
    iban="DE32120222391919191911",
    swift_code="12321234",
    national_id="04123547X",
    passport="FA1234098",
    national_insurance_number="23123312321",
    tax_code="323451R",
    tax_identification_number="T4312345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### account_holder_name: `str`<a id="account_holder_name-str"></a>

The accounts holder's name.

##### bank_name: `str`<a id="bank_name-str"></a>

The bank name.

##### account_number: `str`<a id="account_number-str"></a>

The account number.

##### iban: `str`<a id="iban-str"></a>

The IBAN.

##### swift_code: `str`<a id="swift_code-str"></a>

The SWIFT code.

##### national_id: `str`<a id="national_id-str"></a>

The national id document.

##### passport: `str`<a id="passport-str"></a>

The passport number.

##### national_insurance_number: `str`<a id="national_insurance_number-str"></a>

The national insurance number

##### tax_code: `str`<a id="tax_code-str"></a>

The tax number.

##### tax_identification_number: `str`<a id="tax_identification_number-str"></a>

The tax identification number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateFinancialsRequest`](./kenjo_python_sdk/type/employees_update_financials_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdateFinancialsResponse`](./kenjo_python_sdk/pydantic/employees_update_financials_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/financials` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_home`<a id="kenjoemployeesupdate_home"></a>

This endpoint updates the employee **home** section for a given employee id. The operation only updates the fields provided in the body.
<br><br>**Custom fields** information can be provided in this operation. The *API name* of the custom field is required and the data format has to match with the type defined for the custom field in Kenjo.
API names start with 'c_' and the rest is composed by the trimmed name (spaces are removed).
<br><br>
Example:
<br>
*The custom field 'pet name' belongs to the 'home' section*:
  ```
  {
    ...,
    "maritalStatus": "Divorced",
    "c_petname": "Boliche",
    ...
  }
```
*'pet name' is a field type 'String'. It means that if a different type of data (number or boolean) is provided then the request will return an error.*


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_home_response = kenjo.employees.update_home(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    marital_status="Widowed",
    spouse_first_name="Catherine",
    spouse_last_name="Tramell",
    spouse_birthdate="2060-01-26T00:00:00.000Z",
    spouse_gender="Female",
    personal_email="john@acme.io",
    personal_phone="4567092323",
    personal_mobile="3567092310",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### marital_status: `str`<a id="marital_status-str"></a>

The marital status. Only is valid one of the following values \\\"Divorced\\\", \\\"Domestic Partnership\\\", \\\"Married\\\", \\\"Separated\\\", \\\"Single\\\", \\\"Widowed\\\".

##### spouse_first_name: `str`<a id="spouse_first_name-str"></a>

The first name of the employee's spouse.

##### spouse_last_name: `str`<a id="spouse_last_name-str"></a>

The last name of the employee's spouse.

##### spouse_birthdate: `str`<a id="spouse_birthdate-str"></a>

The birth date of the employee's spouse. Format YYYY-MM-DDThh:mm:ss.000Z.

##### spouse_gender: `str`<a id="spouse_gender-str"></a>

The employee's spouse gender. Only is valid one of the following values 'Male' (male), 'Female' (female) or 'Other' (other).

##### personal_email: `str`<a id="personal_email-str"></a>

The employee personal email.

##### personal_phone: `str`<a id="personal_phone-str"></a>

The employee personal phone.

##### personal_mobile: `str`<a id="personal_mobile-str"></a>

The employee personal phone

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateHomeRequest`](./kenjo_python_sdk/type/employees_update_home_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdateHomeResponse`](./kenjo_python_sdk/pydantic/employees_update_home_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/homes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_personals`<a id="kenjoemployeesupdate_personals"></a>

This endpoint updates the employee **personal** section for a given employee id. The operation only updates the fields provided in the body.
<br><br>**Custom fields** information can be provided in this operation. The *API name* of the custom field is required and the data format has to match with the type defined for the custom field in Kenjo.
API names start with 'c_' and the rest is composed by the trimmed name (spaces are removed).
<br><br>
Example:
<br>
*The custom field 'category' belongs to the 'personal' section*:
  ```
  {
    ...,
    "lastName": "Nadie",
    "c_category": "Good",
    ...
  }
```
*'category' is a field type 'List' (Strings list) with the possible values: "Good" and "Bad". It means that if a different value or type is provided then the request will return an error.*


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_personals_response = kenjo.employees.update_personals(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    first_name="Juanito",
    last_name="Nadie",
    display_name="Juanito Nadie",
    gender="Male",
    birthdate="1980-01-28T00:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### first_name: `str`<a id="first_name-str"></a>

The name of the Kenjo employee. This field is required.

##### last_name: `str`<a id="last_name-str"></a>

The surname of the Kenjo employee. This field is required.

##### display_name: `str`<a id="display_name-str"></a>

The composition of firstName and lastName of the Kenjo employee.

##### gender: `str`<a id="gender-str"></a>

The gender of the Kenjo employee. Only is valid one of the following values 'Male' (male), 'Female' (female) or 'Other' (other).

##### birthdate: `str`<a id="birthdate-str"></a>

The employee birth date. Format YYYY-MM-DDThh:mm:ss.000Z.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdatePersonalsRequest`](./kenjo_python_sdk/type/employees_update_personals_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdatePersonalsResponse`](./kenjo_python_sdk/pydantic/employees_update_personals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/personals` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_work_schedule`<a id="kenjoemployeesupdate_work_schedule"></a>

This endpoint updates the employee **work schedule** section for a given employee id. The operation only updates the fields provided in the body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_work_schedule_response = kenjo.employees.update_work_schedule(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    monday_working_day=True,
    tuesday_working_day=True,
    wednesday_working_day=True,
    thursday_working_day=True,
    friday_working_day=False,
    saturday_working_day=False,
    sunday_working_day=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### monday_working_day: `bool`<a id="monday_working_day-bool"></a>

Allow to indicate if mondays are working days for the employee.

##### tuesday_working_day: `bool`<a id="tuesday_working_day-bool"></a>

Allow to indicate if tuesdays are working days for the employee.

##### wednesday_working_day: `bool`<a id="wednesday_working_day-bool"></a>

Allow to indicate if wednesdays are working days for the employee.

##### thursday_working_day: `bool`<a id="thursday_working_day-bool"></a>

Allow to indicate if thursdays are working days for the employee.

##### friday_working_day: `bool`<a id="friday_working_day-bool"></a>

Allow to indicate if fridays are working days for the employee.

##### saturday_working_day: `bool`<a id="saturday_working_day-bool"></a>

Allow to indicate if saturdays are working days for the employee.

##### sunday_working_day: `bool`<a id="sunday_working_day-bool"></a>

Allow to indicate if sundays are working days for the employee.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateWorkScheduleRequest`](./kenjo_python_sdk/type/employees_update_work_schedule_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdateWorkScheduleResponse`](./kenjo_python_sdk/pydantic/employees_update_work_schedule_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/work-schedules` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.employees.update_works`<a id="kenjoemployeesupdate_works"></a>

This endpoint updates the employee **work** section for a given employee id. The operation only updates the fields provided in the body.
<br><br>**Custom fields** information can be provided in this operation. The *API name* of the custom field is required and the data format has to match with the type defined for the custom field in Kenjo.
API names start with 'c_' and the rest is composed by the trimmed name (spaces are removed).
<br><br>
Example:
<br>
*The custom field 'activity type' belongs to the 'personal' section*:
  ```
  {
    ...,
    "companyId": "61d874aef37c05cfba4f1b38",
    "c_activityType": "1",
    ...
  }
```
*'activity Type' is a field type 'List' (Strings list) with the possible values: "1" and "2". It means that if a different value or type is provided then the request will return an error.*


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_works_response = kenjo.employees.update_works(
    employee_id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    company_id="50a2db290da29e126a187894",
    office_id="50a2db290da29e126a187895",
    department_id="50a2db290da29e126a187896",
    start_date="2021-07-01T00:00:00.000Z",
    job_title="Actor",
    work_phone="+34 666 70 90 32",
    work_mobile="+34 680 70 90 32",
    is_assistant=False,
    probation_period_end="2022-06-01T00:00:00.000Z",
    reports_to_id="50a2db290da29e126a1878523",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

The _id of the employee to update.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### company_id: `str`<a id="company_id-str"></a>

The company id of the Kenjo employee.

##### office_id: `str`<a id="office_id-str"></a>

The office id of the Kenjo employee.

##### department_id: `str`<a id="department_id-str"></a>

The department id of the Kenjo employee.

##### start_date: `str`<a id="start_date-str"></a>

The starting date of the Kenjo employee in format YYYY-MM-DDThh:mm:ss.

##### job_title: `str`<a id="job_title-str"></a>

The job title of the employee.

##### work_phone: `str`<a id="work_phone-str"></a>

The work phone of the employee.

##### work_mobile: `str`<a id="work_mobile-str"></a>

The work mobile of the employee.

##### is_assistant: `bool`<a id="is_assistant-bool"></a>

Allow to indicate if the employee has or not the assistant role.

##### probation_period_end: `str`<a id="probation_period_end-str"></a>

The probation period of the employee. Format YYYY-MM-DDThh:mm:ss.000Z.

##### reports_to_id: `str`<a id="reports_to_id-str"></a>

The Kenjo employee id of the user to whom the employee reports. The employee id to assign can be an active or inactive user. Trying to assign the own employee id or the id of someone who is already reporting will arise an error.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeesUpdateWorksRequest`](./kenjo_python_sdk/type/employees_update_works_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeesUpdateWorksResponse`](./kenjo_python_sdk/pydantic/employees_update_works_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{employeeId}/works` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.offices.create_new_office`<a id="kenjoofficescreate_new_office"></a>

Creates a new office.<br><br>The required fields are *name*, *companyId*, *calendarId*.<br>Optional fields are *street*, *postalCode*, *city* and *country*. <br> The *country* field has to be a valid ISO country code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_office_response = kenjo.offices.create_new_office(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Spain office",
    company_id="60dadb6362702d057f8fb486",
    calendar_id="60f808f727ad58fe791bae91",
    country="ES",
    postal_code="28030",
    city="ES",
    street="Paseo Castellana, 13",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the office to create. Required field.

##### company_id: `str`<a id="company_id-str"></a>

The company id of the office to create. Required field.

##### calendar_id: `str`<a id="calendar_id-str"></a>

The calendar id of the office to create. Required field.

##### country: `str`<a id="country-str"></a>

The country of the office to create in ISO code.

##### postal_code: `str`<a id="postal_code-str"></a>

The postal code of the office to create.

##### city: `str`<a id="city-str"></a>

The city of the office to create.

##### street: `str`<a id="street-str"></a>

The street of the office to create.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OfficesCreateNewOfficeRequest`](./kenjo_python_sdk/type/offices_create_new_office_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OfficesCreateNewOfficeResponse`](./kenjo_python_sdk/pydantic/offices_create_new_office_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/offices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.offices.get_by_id`<a id="kenjoofficesget_by_id"></a>

Returns the office referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kenjo.offices.get_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the office entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`OfficesGetByIdResponse`](./kenjo_python_sdk/pydantic/offices_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/offices/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.offices.get_list`<a id="kenjoofficesget_list"></a>

Returns a list of the existing offices in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.offices.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Berlin office",
    company_id="40a2db290da29e126a187895",
    calendar_id="40a2db290da29e126a187895",
    street="Urbanstrasse, 71",
    postal_code="34213",
    city="Berlin",
    country="DE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The name of the office.

##### company_id: `str`<a id="company_id-str"></a>

The Kenjo id of the company.

##### calendar_id: `str`<a id="calendar_id-str"></a>

The Kenjo id of the calendar.

##### street: `str`<a id="street-str"></a>

The street of the office.

##### postal_code: `str`<a id="postal_code-str"></a>

The postal code of the office.

##### city: `str`<a id="city-str"></a>

The city of the office.

##### country: `str`<a id="country-str"></a>

The country of the office in ISO code.

#### 🔄 Return<a id="🔄-return"></a>

[`OfficesGetListResponse`](./kenjo_python_sdk/pydantic/offices_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/offices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.offices.remove_by_id`<a id="kenjoofficesremove_by_id"></a>

Removes the office referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kenjo.offices.remove_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the office entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/offices/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.offices.update_office_attributes`<a id="kenjoofficesupdate_office_attributes"></a>

Updates an office referenced by *id*. Only the attributes submitted are modified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_office_attributes_response = kenjo.offices.update_office_attributes(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Madrid office",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the office entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the office to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OfficesUpdateOfficeAttributesRequest`](./kenjo_python_sdk/type/offices_update_office_attributes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OfficesUpdateOfficeAttributesResponse`](./kenjo_python_sdk/pydantic/offices_update_office_attributes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/offices/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.teams.create_team`<a id="kenjoteamscreate_team"></a>

Creates a new team.<br>The *name* is the only required field.<br>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_response = kenjo.teams.create_team(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Tech devOps",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the team to update. Required field.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsCreateTeamRequest`](./kenjo_python_sdk/type/teams_create_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TeamsCreateTeamResponse`](./kenjo_python_sdk/pydantic/teams_create_team_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.teams.get_by_id`<a id="kenjoteamsget_by_id"></a>

Returns the team referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kenjo.teams.get_by_id(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the team entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsGetByIdResponse`](./kenjo_python_sdk/pydantic/teams_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.teams.get_list`<a id="kenjoteamsget_list"></a>

Returns a list of the existing teams in Kenjo.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kenjo.teams.get_list(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Developers",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The team name.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsGetListResponse`](./kenjo_python_sdk/pydantic/teams_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.teams.remove_team`<a id="kenjoteamsremove_team"></a>

Removes the team referenced by *id*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
kenjo.teams.remove_team(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the team entry to request.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.teams.update_team_attributes`<a id="kenjoteamsupdate_team_attributes"></a>

Updates a team referenced by *id*. Only the attributes submitted are modified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_team_attributes_response = kenjo.teams.update_team_attributes(
    id="60a2db290da29e126a18789a",
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    name="Sales",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The _id of the team entry to request. Required field.

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### name: `str`<a id="name-str"></a>

The new name of the team to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateTeamAttributesRequest`](./kenjo_python_sdk/type/teams_update_team_attributes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TeamsUpdateTeamAttributesResponse`](./kenjo_python_sdk/pydantic/teams_update_team_attributes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.time_off.get_requests_by_date`<a id="kenjotime_offget_requests_by_date"></a>

This endpoint returns a paginated list of time off requests for a given date range.The maximum number of time off requests to retrieve once is 92 days, so the URL params *from* and *to* are mandatory. The URL params help to return more accurate results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_requests_by_date_response = kenjo.time_off.get_requests_by_date(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
    _from="2020-01-01",
    to="2020-01-10",
    user_id="60a2db290da29e126a18789b",
    time_off_type_id="90a2db290da29e126a187891",
    status="Approved",
    offset=1,
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

##### _from: `str`<a id="_from-str"></a>

A date in format YYYY-MM-DD to indicate the starting point. It needs to be equals or less than the *to* param.

##### to: `str`<a id="to-str"></a>

A date in format YYYY-MM-DD to indicate the ending point. It needs to be equals or greater than the *from* param.

##### user_id: `str`<a id="user_id-str"></a>

This field allows to return only the time off requests for a given *_userId*.

##### time_off_type_id: `str`<a id="time_off_type_id-str"></a>

This field allows to filter by time-off type Id.

##### status: `str`<a id="status-str"></a>

This field allows to filter by the time-off request status.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

Optional filter for pagination proposals. Determines the number of pages to skip when pagination is being used. If this value is not provided, by default the offset will be 1.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Optional filter for pagination proposals. The maximum number of rows to retrieve which determines the size of the page. If this value is not provided then the limit will be 50 users. The maximum value of the limit is 100 users per page. Only are valid the following limit values: 25, 50 and 100.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetRequestsByDateResponse`](./kenjo_python_sdk/pydantic/time_off_get_requests_by_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time-off/requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kenjo.user_accounts.list_employees`<a id="kenjouser_accountslist_employees"></a>

This endpoint returns an array of objects with the existing employees in Kenjo. Every object contains the basic employee information from **account**, **personal** and **work** sections per each existing employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employees_response = kenjo.user_accounts.list_employees(
    authorization="Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5rZW5qby5pbyIsInN1YiI6IjYwZjBhOTE2MjE0OTg3MjU2YmU5YzhmZiIsImF1ZCI6Imh0dHBzOi8vYXBpLmtlbmpvLmlvIiwiaWF0IjoxNjI2Mzg1MTE1LCJuYmYiOjE2MjYzODUxMTUsImV4cCI6MTYyNjU1NzkxNSwiYWNjZXNzVHlwZSI6IkFwaUFjY2VzcyIsInNfb3JnSWQiOiI2MGYwNGVhN2RmN2JhMjFlY2U0YmYzYzIifQ.cxG_7dIS-VbmDXdJuLkekoyuyCIzQG2fMcgc0nkfbWE8cihhcb5FnALbQkjU9b5-qVcEoMHZlSuUA-jMEBMMVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

A valid bearer token.

#### 🔄 Return<a id="🔄-return"></a>

[`UserAccountsListEmployeesResponse`](./kenjo_python_sdk/pydantic/user_accounts_list_employees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user-accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
