# coding: utf-8

"""
    Kenjo API

    Before starting to use the Kenjo API, you have to request the API activation for a sandbox or production environment to the Kenjo Customer Success team. After that, an admin user has to go to *Settings > Integrations > API keys*, to generate the **API Key**. Follow the steps described in the **Autentication section** of this document. <br>The API key is needed to request the bearer token. Each endpoint callout requires a valid bearer token in the Authorization header. Once the token is retrieved, it will be useful during the time limit indicated by the 'expiration date'.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from kenjo_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from kenjo_python_sdk.api_response import AsyncGeneratorResponse
from kenjo_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kenjo_python_sdk import schemas  # noqa: F401

from kenjo_python_sdk.model.employees_create_inactive_employee_request import EmployeesCreateInactiveEmployeeRequest as EmployeesCreateInactiveEmployeeRequestSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_work import EmployeesCreateInactiveEmployeeRequestWork as EmployeesCreateInactiveEmployeeRequestWorkSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_personal import EmployeesCreateInactiveEmployeeRequestPersonal as EmployeesCreateInactiveEmployeeRequestPersonalSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_response import EmployeesCreateInactiveEmployeeResponse as EmployeesCreateInactiveEmployeeResponseSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_home import EmployeesCreateInactiveEmployeeRequestHome as EmployeesCreateInactiveEmployeeRequestHomeSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_work_schedule import EmployeesCreateInactiveEmployeeRequestWorkSchedule as EmployeesCreateInactiveEmployeeRequestWorkScheduleSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_account import EmployeesCreateInactiveEmployeeRequestAccount as EmployeesCreateInactiveEmployeeRequestAccountSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_financial import EmployeesCreateInactiveEmployeeRequestFinancial as EmployeesCreateInactiveEmployeeRequestFinancialSchema
from kenjo_python_sdk.model.employees_create_inactive_employee_request_address import EmployeesCreateInactiveEmployeeRequestAddress as EmployeesCreateInactiveEmployeeRequestAddressSchema
from kenjo_python_sdk.model.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponseSchema

from kenjo_python_sdk.type.employees_create_inactive_employee_response import EmployeesCreateInactiveEmployeeResponse
from kenjo_python_sdk.type.employees_create_inactive_employee_request import EmployeesCreateInactiveEmployeeRequest
from kenjo_python_sdk.type.employees_create_inactive_employee_request_personal import EmployeesCreateInactiveEmployeeRequestPersonal
from kenjo_python_sdk.type.employees_create_inactive_employee_request_work_schedule import EmployeesCreateInactiveEmployeeRequestWorkSchedule
from kenjo_python_sdk.type.employees_create_inactive_employee_request_address import EmployeesCreateInactiveEmployeeRequestAddress
from kenjo_python_sdk.type.employees_create_inactive_employee_request_work import EmployeesCreateInactiveEmployeeRequestWork
from kenjo_python_sdk.type.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response
from kenjo_python_sdk.type.employees_create_inactive_employee_request_home import EmployeesCreateInactiveEmployeeRequestHome
from kenjo_python_sdk.type.employees_create_inactive_employee_request_account import EmployeesCreateInactiveEmployeeRequestAccount
from kenjo_python_sdk.type.employees_create_inactive_employee_request_financial import EmployeesCreateInactiveEmployeeRequestFinancial

from ...api_client import Dictionary
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request import EmployeesCreateInactiveEmployeeRequest as EmployeesCreateInactiveEmployeeRequestPydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_financial import EmployeesCreateInactiveEmployeeRequestFinancial as EmployeesCreateInactiveEmployeeRequestFinancialPydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_work import EmployeesCreateInactiveEmployeeRequestWork as EmployeesCreateInactiveEmployeeRequestWorkPydantic
from kenjo_python_sdk.pydantic.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponsePydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_home import EmployeesCreateInactiveEmployeeRequestHome as EmployeesCreateInactiveEmployeeRequestHomePydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_response import EmployeesCreateInactiveEmployeeResponse as EmployeesCreateInactiveEmployeeResponsePydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_work_schedule import EmployeesCreateInactiveEmployeeRequestWorkSchedule as EmployeesCreateInactiveEmployeeRequestWorkSchedulePydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_address import EmployeesCreateInactiveEmployeeRequestAddress as EmployeesCreateInactiveEmployeeRequestAddressPydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_account import EmployeesCreateInactiveEmployeeRequestAccount as EmployeesCreateInactiveEmployeeRequestAccountPydantic
from kenjo_python_sdk.pydantic.employees_create_inactive_employee_request_personal import EmployeesCreateInactiveEmployeeRequestPersonal as EmployeesCreateInactiveEmployeeRequestPersonalPydantic

# Header params
AuthorizationSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'Authorization': typing.Union[AuthorizationSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_authorization = api_client.HeaderParameter(
    name="Authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EmployeesCreateInactiveEmployeeRequestSchema


request_body_employees_create_inactive_employee_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = EmployeesCreateInactiveEmployeeResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: EmployeesCreateInactiveEmployeeResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: EmployeesCreateInactiveEmployeeResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = AuthenticationCreateBearerToken400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: AuthenticationCreateBearerToken400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AuthenticationCreateBearerToken400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_inactive_employee_mapped_args(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if account is not None:
            _body["account"] = account
        if personal is not None:
            _body["personal"] = personal
        if work is not None:
            _body["work"] = work
        if work_schedule is not None:
            _body["workSchedule"] = work_schedule
        if address is not None:
            _body["address"] = address
        if financial is not None:
            _body["financial"] = financial
        if home is not None:
            _body["home"] = home
        args.body = _body
        if authorization is not None:
            _header_params["Authorization"] = authorization
        args.header = _header_params
        return args

    async def _acreate_inactive_employee_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_authorization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/employees',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_employees_create_inactive_employee_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_inactive_employee_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_authorization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/employees',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_employees_create_inactive_employee_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateInactiveEmployeeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_inactive_employee(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_inactive_employee_mapped_args(
            authorization=authorization,
            account=account,
            personal=personal,
            work=work,
            work_schedule=work_schedule,
            address=address,
            financial=financial,
            home=home,
        )
        return await self._acreate_inactive_employee_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create_inactive_employee(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_inactive_employee_mapped_args(
            authorization=authorization,
            account=account,
            personal=personal,
            work=work,
            work_schedule=work_schedule,
            address=address,
            financial=financial,
            home=home,
        )
        return self._create_inactive_employee_oapg(
            body=args.body,
            header_params=args.header,
        )

class CreateInactiveEmployee(BaseApi):

    async def acreate_inactive_employee(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeesCreateInactiveEmployeeResponsePydantic:
        raw_response = await self.raw.acreate_inactive_employee(
            authorization=authorization,
            account=account,
            personal=personal,
            work=work,
            work_schedule=work_schedule,
            address=address,
            financial=financial,
            home=home,
            **kwargs,
        )
        if validate:
            return EmployeesCreateInactiveEmployeeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesCreateInactiveEmployeeResponsePydantic, raw_response.body)
    
    
    def create_inactive_employee(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
        validate: bool = False,
    ) -> EmployeesCreateInactiveEmployeeResponsePydantic:
        raw_response = self.raw.create_inactive_employee(
            authorization=authorization,
            account=account,
            personal=personal,
            work=work,
            work_schedule=work_schedule,
            address=address,
            financial=financial,
            home=home,
        )
        if validate:
            return EmployeesCreateInactiveEmployeeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesCreateInactiveEmployeeResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_inactive_employee_mapped_args(
            authorization=authorization,
            account=account,
            personal=personal,
            work=work,
            work_schedule=work_schedule,
            address=address,
            financial=financial,
            home=home,
        )
        return await self._acreate_inactive_employee_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        authorization: str,
        account: typing.Optional[EmployeesCreateInactiveEmployeeRequestAccount] = None,
        personal: typing.Optional[EmployeesCreateInactiveEmployeeRequestPersonal] = None,
        work: typing.Optional[EmployeesCreateInactiveEmployeeRequestWork] = None,
        work_schedule: typing.Optional[EmployeesCreateInactiveEmployeeRequestWorkSchedule] = None,
        address: typing.Optional[EmployeesCreateInactiveEmployeeRequestAddress] = None,
        financial: typing.Optional[EmployeesCreateInactiveEmployeeRequestFinancial] = None,
        home: typing.Optional[EmployeesCreateInactiveEmployeeRequestHome] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_inactive_employee_mapped_args(
            authorization=authorization,
            account=account,
            personal=personal,
            work=work,
            work_schedule=work_schedule,
            address=address,
            financial=financial,
            home=home,
        )
        return self._create_inactive_employee_oapg(
            body=args.body,
            header_params=args.header,
        )

