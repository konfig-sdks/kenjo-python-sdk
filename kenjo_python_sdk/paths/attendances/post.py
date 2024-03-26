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

from kenjo_python_sdk.model.attendance_create_entry_response import AttendanceCreateEntryResponse as AttendanceCreateEntryResponseSchema
from kenjo_python_sdk.model.attendance_create_entry_request_breaks import AttendanceCreateEntryRequestBreaks as AttendanceCreateEntryRequestBreaksSchema
from kenjo_python_sdk.model.attendance_create_entry_request import AttendanceCreateEntryRequest as AttendanceCreateEntryRequestSchema
from kenjo_python_sdk.model.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponseSchema

from kenjo_python_sdk.type.attendance_create_entry_request_breaks import AttendanceCreateEntryRequestBreaks
from kenjo_python_sdk.type.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response
from kenjo_python_sdk.type.attendance_create_entry_response import AttendanceCreateEntryResponse
from kenjo_python_sdk.type.attendance_create_entry_request import AttendanceCreateEntryRequest

from ...api_client import Dictionary
from kenjo_python_sdk.pydantic.attendance_create_entry_response import AttendanceCreateEntryResponse as AttendanceCreateEntryResponsePydantic
from kenjo_python_sdk.pydantic.attendance_create_entry_request_breaks import AttendanceCreateEntryRequestBreaks as AttendanceCreateEntryRequestBreaksPydantic
from kenjo_python_sdk.pydantic.attendance_create_entry_request import AttendanceCreateEntryRequest as AttendanceCreateEntryRequestPydantic
from kenjo_python_sdk.pydantic.authentication_create_bearer_token400_response import AuthenticationCreateBearerToken400Response as AuthenticationCreateBearerToken400ResponsePydantic

from . import path

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
SchemaForRequestBodyApplicationJson = AttendanceCreateEntryRequestSchema


request_body_attendance_create_entry_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = AttendanceCreateEntryResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: AttendanceCreateEntryResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: AttendanceCreateEntryResponse


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
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_entry_mapped_args(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if user_id is not None:
            _body["userId"] = user_id
        if email is not None:
            _body["email"] = email
        if external_id is not None:
            _body["externalId"] = external_id
        if date is not None:
            _body["date"] = date
        if start_time is not None:
            _body["startTime"] = start_time
        if end_time is not None:
            _body["endTime"] = end_time
        if breaks is not None:
            _body["breaks"] = breaks
        if comment is not None:
            _body["comment"] = comment
        args.body = _body
        if authorization is not None:
            _header_params["Authorization"] = authorization
        args.header = _header_params
        return args

    async def _acreate_entry_oapg(
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
            path_template='/attendances',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_attendance_create_entry_request.serialize(body, content_type)
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


    def _create_entry_oapg(
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
            path_template='/attendances',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_attendance_create_entry_request.serialize(body, content_type)
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


class CreateEntryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_entry(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_entry_mapped_args(
            date=date,
            start_time=start_time,
            authorization=authorization,
            user_id=user_id,
            email=email,
            external_id=external_id,
            end_time=end_time,
            breaks=breaks,
            comment=comment,
        )
        return await self._acreate_entry_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create_entry(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_entry_mapped_args(
            date=date,
            start_time=start_time,
            authorization=authorization,
            user_id=user_id,
            email=email,
            external_id=external_id,
            end_time=end_time,
            breaks=breaks,
            comment=comment,
        )
        return self._create_entry_oapg(
            body=args.body,
            header_params=args.header,
        )

class CreateEntry(BaseApi):

    async def acreate_entry(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AttendanceCreateEntryResponsePydantic:
        raw_response = await self.raw.acreate_entry(
            date=date,
            start_time=start_time,
            authorization=authorization,
            user_id=user_id,
            email=email,
            external_id=external_id,
            end_time=end_time,
            breaks=breaks,
            comment=comment,
            **kwargs,
        )
        if validate:
            return AttendanceCreateEntryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AttendanceCreateEntryResponsePydantic, raw_response.body)
    
    
    def create_entry(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AttendanceCreateEntryResponsePydantic:
        raw_response = self.raw.create_entry(
            date=date,
            start_time=start_time,
            authorization=authorization,
            user_id=user_id,
            email=email,
            external_id=external_id,
            end_time=end_time,
            breaks=breaks,
            comment=comment,
        )
        if validate:
            return AttendanceCreateEntryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AttendanceCreateEntryResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_entry_mapped_args(
            date=date,
            start_time=start_time,
            authorization=authorization,
            user_id=user_id,
            email=email,
            external_id=external_id,
            end_time=end_time,
            breaks=breaks,
            comment=comment,
        )
        return await self._acreate_entry_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        date: str,
        start_time: str,
        authorization: str,
        user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        breaks: typing.Optional[AttendanceCreateEntryRequestBreaks] = None,
        comment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_entry_mapped_args(
            date=date,
            start_time=start_time,
            authorization=authorization,
            user_id=user_id,
            email=email,
            external_id=external_id,
            end_time=end_time,
            breaks=breaks,
            comment=comment,
        )
        return self._create_entry_oapg(
            body=args.body,
            header_params=args.header,
        )

