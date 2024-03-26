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

from kenjo_python_sdk.model.employees_list_homes_response import EmployeesListHomesResponse as EmployeesListHomesResponseSchema
from kenjo_python_sdk.model.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponseSchema

from kenjo_python_sdk.type.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response
from kenjo_python_sdk.type.employees_list_homes_response import EmployeesListHomesResponse

from ...api_client import Dictionary
from kenjo_python_sdk.pydantic.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponsePydantic
from kenjo_python_sdk.pydantic.employees_list_homes_response import EmployeesListHomesResponse as EmployeesListHomesResponsePydantic

from . import path

# Query params


class MaritalStatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "Divorced": "DIVORCED",
            "Domestic Partnership": "DOMESTIC_PARTNERSHIP",
            "Married": "MARRIED",
            "Separated": "SEPARATED",
            "Single": "SINGLE",
            "Widowed": "WIDOWED",
        }
    
    @schemas.classproperty
    def DIVORCED(cls):
        return cls("Divorced")
    
    @schemas.classproperty
    def DOMESTIC_PARTNERSHIP(cls):
        return cls("Domestic Partnership")
    
    @schemas.classproperty
    def MARRIED(cls):
        return cls("Married")
    
    @schemas.classproperty
    def SEPARATED(cls):
        return cls("Separated")
    
    @schemas.classproperty
    def SINGLE(cls):
        return cls("Single")
    
    @schemas.classproperty
    def WIDOWED(cls):
        return cls("Widowed")
SpouseFirstNameSchema = schemas.StrSchema
SpouseLastNameSchema = schemas.StrSchema
SpouseBirthdateSchema = schemas.StrSchema


class SpouseGenderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "Male": "MALE",
            "Female": "FEMALE",
            "Other": "OTHER",
        }
    
    @schemas.classproperty
    def MALE(cls):
        return cls("Male")
    
    @schemas.classproperty
    def FEMALE(cls):
        return cls("Female")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("Other")
PersonalEmailSchema = schemas.StrSchema
PersonalPhoneSchema = schemas.StrSchema
PersonalMobileSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'maritalStatus': typing.Union[MaritalStatusSchema, str, ],
        'spouseFirstName': typing.Union[SpouseFirstNameSchema, str, ],
        'spouseLastName': typing.Union[SpouseLastNameSchema, str, ],
        'spouseBirthdate': typing.Union[SpouseBirthdateSchema, str, ],
        'spouseGender': typing.Union[SpouseGenderSchema, str, ],
        'personalEmail': typing.Union[PersonalEmailSchema, str, ],
        'personalPhone': typing.Union[PersonalPhoneSchema, str, ],
        'personalMobile': typing.Union[PersonalMobileSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_marital_status = api_client.QueryParameter(
    name="maritalStatus",
    style=api_client.ParameterStyle.FORM,
    schema=MaritalStatusSchema,
    explode=True,
)
request_query_spouse_first_name = api_client.QueryParameter(
    name="spouseFirstName",
    style=api_client.ParameterStyle.FORM,
    schema=SpouseFirstNameSchema,
    explode=True,
)
request_query_spouse_last_name = api_client.QueryParameter(
    name="spouseLastName",
    style=api_client.ParameterStyle.FORM,
    schema=SpouseLastNameSchema,
    explode=True,
)
request_query_spouse_birthdate = api_client.QueryParameter(
    name="spouseBirthdate",
    style=api_client.ParameterStyle.FORM,
    schema=SpouseBirthdateSchema,
    explode=True,
)
request_query_spouse_gender = api_client.QueryParameter(
    name="spouseGender",
    style=api_client.ParameterStyle.FORM,
    schema=SpouseGenderSchema,
    explode=True,
)
request_query_personal_email = api_client.QueryParameter(
    name="personalEmail",
    style=api_client.ParameterStyle.FORM,
    schema=PersonalEmailSchema,
    explode=True,
)
request_query_personal_phone = api_client.QueryParameter(
    name="personalPhone",
    style=api_client.ParameterStyle.FORM,
    schema=PersonalPhoneSchema,
    explode=True,
)
request_query_personal_mobile = api_client.QueryParameter(
    name="personalMobile",
    style=api_client.ParameterStyle.FORM,
    schema=PersonalMobileSchema,
    explode=True,
)
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
SchemaFor200ResponseBodyApplicationJson = EmployeesListHomesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeesListHomesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeesListHomesResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_homes_mapped_args(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if marital_status is not None:
            _query_params["maritalStatus"] = marital_status
        if spouse_first_name is not None:
            _query_params["spouseFirstName"] = spouse_first_name
        if spouse_last_name is not None:
            _query_params["spouseLastName"] = spouse_last_name
        if spouse_birthdate is not None:
            _query_params["spouseBirthdate"] = spouse_birthdate
        if spouse_gender is not None:
            _query_params["spouseGender"] = spouse_gender
        if personal_email is not None:
            _query_params["personalEmail"] = personal_email
        if personal_phone is not None:
            _query_params["personalPhone"] = personal_phone
        if personal_mobile is not None:
            _query_params["personalMobile"] = personal_mobile
        if authorization is not None:
            _header_params["Authorization"] = authorization
        args.query = _query_params
        args.header = _header_params
        return args

    async def _alist_homes_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_marital_status,
            request_query_spouse_first_name,
            request_query_spouse_last_name,
            request_query_spouse_birthdate,
            request_query_spouse_gender,
            request_query_personal_email,
            request_query_personal_phone,
            request_query_personal_mobile,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/employees/homes',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_homes_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_marital_status,
            request_query_spouse_first_name,
            request_query_spouse_last_name,
            request_query_spouse_birthdate,
            request_query_spouse_gender,
            request_query_personal_email,
            request_query_personal_phone,
            request_query_personal_mobile,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/employees/homes',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListHomesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_homes(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_homes_mapped_args(
            authorization=authorization,
            marital_status=marital_status,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
            spouse_birthdate=spouse_birthdate,
            spouse_gender=spouse_gender,
            personal_email=personal_email,
            personal_phone=personal_phone,
            personal_mobile=personal_mobile,
        )
        return await self._alist_homes_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def list_homes(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_homes_mapped_args(
            authorization=authorization,
            marital_status=marital_status,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
            spouse_birthdate=spouse_birthdate,
            spouse_gender=spouse_gender,
            personal_email=personal_email,
            personal_phone=personal_phone,
            personal_mobile=personal_mobile,
        )
        return self._list_homes_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class ListHomes(BaseApi):

    async def alist_homes(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeesListHomesResponsePydantic:
        raw_response = await self.raw.alist_homes(
            authorization=authorization,
            marital_status=marital_status,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
            spouse_birthdate=spouse_birthdate,
            spouse_gender=spouse_gender,
            personal_email=personal_email,
            personal_phone=personal_phone,
            personal_mobile=personal_mobile,
            **kwargs,
        )
        if validate:
            return EmployeesListHomesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesListHomesResponsePydantic, raw_response.body)
    
    
    def list_homes(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmployeesListHomesResponsePydantic:
        raw_response = self.raw.list_homes(
            authorization=authorization,
            marital_status=marital_status,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
            spouse_birthdate=spouse_birthdate,
            spouse_gender=spouse_gender,
            personal_email=personal_email,
            personal_phone=personal_phone,
            personal_mobile=personal_mobile,
        )
        if validate:
            return EmployeesListHomesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesListHomesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_homes_mapped_args(
            authorization=authorization,
            marital_status=marital_status,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
            spouse_birthdate=spouse_birthdate,
            spouse_gender=spouse_gender,
            personal_email=personal_email,
            personal_phone=personal_phone,
            personal_mobile=personal_mobile,
        )
        return await self._alist_homes_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        authorization: str,
        marital_status: typing.Optional[str] = None,
        spouse_first_name: typing.Optional[str] = None,
        spouse_last_name: typing.Optional[str] = None,
        spouse_birthdate: typing.Optional[str] = None,
        spouse_gender: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_phone: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_homes_mapped_args(
            authorization=authorization,
            marital_status=marital_status,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
            spouse_birthdate=spouse_birthdate,
            spouse_gender=spouse_gender,
            personal_email=personal_email,
            personal_phone=personal_phone,
            personal_mobile=personal_mobile,
        )
        return self._list_homes_oapg(
            query_params=args.query,
            header_params=args.header,
        )

