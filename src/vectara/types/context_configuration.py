# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContextConfiguration(UniversalBaseModel):
    """
    Configuration on the presentation of each document part in the result set.
    """

    characters_before: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of characters that are shown before the matching document part.
    This is useful to show the context of the document part in the wider document.
    Ignored if `sentences_before` is set.
    Vectara will capture the full sentence that contains the captured characters,
    to not lose the meaning caused by a truncated word or sentence.
    """

    characters_after: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of characters that are shown after the matching document part. 
    This is useful to show the context of the document part in the wider document.
    Ignored if `sentences_after` is set.
    Vectara will capture the full sentence that contains the captured characters,
    to not lose the meaning caused by a truncated word or sentence.
    """

    sentences_before: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of sentences that are shown before the matching document part.
    This is useful to show the context of the document part in the wider document.
    """

    sentences_after: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of sentences that are shown after the matching document part. 
    This is useful to show the context of the document part in the wider document.
    """

    start_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag that wraps the document part at the start. This is often used to 
    provide a start HTML/XML tag or some other delimiter you can use in an 
    application to understand where to provide highlighting in your UI and 
    understand where the context before ends and the document part begins.
    """

    end_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tag that wraps the document part at the end. This is often used to 
    provide a start HTML/XML tag or some other delimiter you can use in an 
    application to understand where to provide highlighting in your UI and 
    understand where the context before ends and the document part begins.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
