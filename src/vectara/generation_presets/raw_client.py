# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pagination import AsyncPager, SyncPager
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..types.error import Error
from ..types.generation_preset import GenerationPreset
from ..types.list_generation_presets_response import ListGenerationPresetsResponse


class RawGenerationPresetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        llm_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_key: typing.Optional[str] = None,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SyncPager[GenerationPreset]]:
        """
        List generation presets used for query or chat requests. Generation presets are
        the build of properties used to configure generation for a request. This includes
        the template that renders the prompt, and various generation settings like
        `temperature`.

        Parameters
        ----------
        llm_name : typing.Optional[str]
            Filter presets by the LLM name.

        limit : typing.Optional[int]
            The maximum number of results to return in the list.

        page_key : typing.Optional[str]
            Used to retrieve the next page of generation presets after the limit has been reached.
            This parameter is not needed for the first page of results.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SyncPager[GenerationPreset]]
            List of Generation Presets.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/generation_presets",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            params={
                "llm_name": llm_name,
                "limit": limit,
                "page_key": page_key,
            },
            headers={
                "Request-Timeout": str(request_timeout) if request_timeout is not None else None,
                "Request-Timeout-Millis": str(request_timeout_millis) if request_timeout_millis is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListGenerationPresetsResponse,
                    parse_obj_as(
                        type_=ListGenerationPresetsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = False
                _get_next = None
                if _parsed_response.metadata is not None:
                    _parsed_next = _parsed_response.metadata.page_key
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        llm_name=llm_name,
                        limit=limit,
                        page_key=_parsed_next,
                        request_timeout=request_timeout,
                        request_timeout_millis=request_timeout_millis,
                        request_options=request_options,
                    )
                _items = _parsed_response.generation_presets
                return HttpResponse(
                    response=_response, data=SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawGenerationPresetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        llm_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_key: typing.Optional[str] = None,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsyncPager[GenerationPreset]]:
        """
        List generation presets used for query or chat requests. Generation presets are
        the build of properties used to configure generation for a request. This includes
        the template that renders the prompt, and various generation settings like
        `temperature`.

        Parameters
        ----------
        llm_name : typing.Optional[str]
            Filter presets by the LLM name.

        limit : typing.Optional[int]
            The maximum number of results to return in the list.

        page_key : typing.Optional[str]
            Used to retrieve the next page of generation presets after the limit has been reached.
            This parameter is not needed for the first page of results.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncPager[GenerationPreset]]
            List of Generation Presets.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/generation_presets",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            params={
                "llm_name": llm_name,
                "limit": limit,
                "page_key": page_key,
            },
            headers={
                "Request-Timeout": str(request_timeout) if request_timeout is not None else None,
                "Request-Timeout-Millis": str(request_timeout_millis) if request_timeout_millis is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListGenerationPresetsResponse,
                    parse_obj_as(
                        type_=ListGenerationPresetsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = False
                _get_next = None
                if _parsed_response.metadata is not None:
                    _parsed_next = _parsed_response.metadata.page_key
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        llm_name=llm_name,
                        limit=limit,
                        page_key=_parsed_next,
                        request_timeout=request_timeout,
                        request_timeout_millis=request_timeout_millis,
                        request_options=request_options,
                    )
                _items = _parsed_response.generation_presets
                return AsyncHttpResponse(
                    response=_response, data=AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
