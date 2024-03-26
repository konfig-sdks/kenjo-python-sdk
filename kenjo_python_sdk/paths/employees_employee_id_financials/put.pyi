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

from kenjo_python_sdk.model.employees_update_financials_request import EmployeesUpdateFinancialsRequest as EmployeesUpdateFinancialsRequestSchema
from kenjo_python_sdk.model.employees_update_financials_response import EmployeesUpdateFinancialsResponse as EmployeesUpdateFinancialsResponseSchema
from kenjo_python_sdk.model.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponseSchema

from kenjo_python_sdk.type.employees_update_financials_response import EmployeesUpdateFinancialsResponse
from kenjo_python_sdk.type.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response
from kenjo_python_sdk.type.employees_update_financials_request import EmployeesUpdateFinancialsRequest

from ...api_client import Dictionary
from kenjo_python_sdk.pydantic.employees_update_financials_request import EmployeesUpdateFinancialsRequest as EmployeesUpdateFinancialsRequestPydantic
from kenjo_python_sdk.pydantic.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponsePydantic
from kenjo_python_sdk.pydantic.employees_update_financials_response import EmployeesUpdateFinancialsResponse as EmployeesUpdateFinancialsResponsePydantic

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
# Path params
EmployeeIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_employee_id = api_client.PathParameter(
    name="employeeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EmployeesUpdateFinancialsRequestSchema


request_body_employees_update_financials_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = EmployeesUpdateFinancialsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeesUpdateFinancialsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeesUpdateFinancialsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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

    def _update_financials_mapped_args(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if account_holder_name is not None:
            _body["accountHolderName"] = account_holder_name
        if bank_name is not None:
            _body["bankName"] = bank_name
        if account_number is not None:
            _body["accountNumber"] = account_number
        if iban is not None:
            _body["iban"] = iban
        if swift_code is not None:
            _body["swiftCode"] = swift_code
        if national_id is not None:
            _body["nationalId"] = national_id
        if passport is not None:
            _body["passport"] = passport
        if national_insurance_number is not None:
            _body["nationalInsuranceNumber"] = national_insurance_number
        if tax_code is not None:
            _body["taxCode"] = tax_code
        if tax_identification_number is not None:
            _body["taxIdentificationNumber"] = tax_identification_number
        args.body = _body
        if authorization is not None:
            _header_params["Authorization"] = authorization
        if employee_id is not None:
            _path_params["employeeId"] = employee_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_financials_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        method = 'put'.upper()
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
            path_template='/employees/{employeeId}/financials',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_employees_update_financials_request.serialize(body, content_type)
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


    def _update_financials_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        method = 'put'.upper()
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
            path_template='/employees/{employeeId}/financials',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_employees_update_financials_request.serialize(body, content_type)
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


class UpdateFinancialsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_financials(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_financials_mapped_args(
            employee_id=employee_id,
            authorization=authorization,
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            account_number=account_number,
            iban=iban,
            swift_code=swift_code,
            national_id=national_id,
            passport=passport,
            national_insurance_number=national_insurance_number,
            tax_code=tax_code,
            tax_identification_number=tax_identification_number,
        )
        return await self._aupdate_financials_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_financials(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_financials_mapped_args(
            employee_id=employee_id,
            authorization=authorization,
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            account_number=account_number,
            iban=iban,
            swift_code=swift_code,
            national_id=national_id,
            passport=passport,
            national_insurance_number=national_insurance_number,
            tax_code=tax_code,
            tax_identification_number=tax_identification_number,
        )
        return self._update_financials_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateFinancials(BaseApi):

    async def aupdate_financials(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeesUpdateFinancialsResponsePydantic:
        raw_response = await self.raw.aupdate_financials(
            employee_id=employee_id,
            authorization=authorization,
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            account_number=account_number,
            iban=iban,
            swift_code=swift_code,
            national_id=national_id,
            passport=passport,
            national_insurance_number=national_insurance_number,
            tax_code=tax_code,
            tax_identification_number=tax_identification_number,
            **kwargs,
        )
        if validate:
            return EmployeesUpdateFinancialsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesUpdateFinancialsResponsePydantic, raw_response.body)
    
    
    def update_financials(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmployeesUpdateFinancialsResponsePydantic:
        raw_response = self.raw.update_financials(
            employee_id=employee_id,
            authorization=authorization,
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            account_number=account_number,
            iban=iban,
            swift_code=swift_code,
            national_id=national_id,
            passport=passport,
            national_insurance_number=national_insurance_number,
            tax_code=tax_code,
            tax_identification_number=tax_identification_number,
        )
        if validate:
            return EmployeesUpdateFinancialsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesUpdateFinancialsResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_financials_mapped_args(
            employee_id=employee_id,
            authorization=authorization,
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            account_number=account_number,
            iban=iban,
            swift_code=swift_code,
            national_id=national_id,
            passport=passport,
            national_insurance_number=national_insurance_number,
            tax_code=tax_code,
            tax_identification_number=tax_identification_number,
        )
        return await self._aupdate_financials_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        employee_id: str,
        authorization: str,
        account_holder_name: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        iban: typing.Optional[str] = None,
        swift_code: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        passport: typing.Optional[str] = None,
        national_insurance_number: typing.Optional[str] = None,
        tax_code: typing.Optional[str] = None,
        tax_identification_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_financials_mapped_args(
            employee_id=employee_id,
            authorization=authorization,
            account_holder_name=account_holder_name,
            bank_name=bank_name,
            account_number=account_number,
            iban=iban,
            swift_code=swift_code,
            national_id=national_id,
            passport=passport,
            national_insurance_number=national_insurance_number,
            tax_code=tax_code,
            tax_identification_number=tax_identification_number,
        )
        return self._update_financials_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

