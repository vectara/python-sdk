# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_history_span import QueryHistorySpan


class QueryHistory(UniversalBaseModel):
    """
    A complete record of a previously executed query, including the request parameters and response.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the query history.
    """

    query: typing.Optional[typing.Optional[typing.Any]] = None
    chat_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the chat the query is a part of.
    """

    latency_millis: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time taken to complete the query, measured in milliseconds.
    """

    started_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO date time indicating when the query was first received.
    """

    spans: typing.Optional[typing.List[QueryHistorySpan]] = pydantic.Field(default=None)
    """
    Parts of the query pipeline. Each span explains what happened during that stage of the query pipeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
