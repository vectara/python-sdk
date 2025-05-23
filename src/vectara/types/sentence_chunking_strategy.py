# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SentenceChunkingStrategy(UniversalBaseModel):
    """
    Sets a chunking strategy that creates one chunk per sentence.
    This is the default strategy used when no chunking strategy is specified.
    """

    type: typing.Literal["sentence_chunking_strategy"] = "sentence_chunking_strategy"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
