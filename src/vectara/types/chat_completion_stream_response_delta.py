# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionStreamResponseDelta(UniversalBaseModel):
    """
    A partial message update to be merged with previous chunks in a streaming response.
    """

    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    The role of the author of this message, typically 'assistant' for responses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
