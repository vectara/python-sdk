# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CorpusCustomDimension(UniversalBaseModel):
    """
    Custom dimensions attached to all document parts in a corpus. Allows arbitrary
    modification of the score for many purposes.
    """

    name: str = pydantic.Field()
    """
    The name of the custom dimension.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the custom dimension.
    """

    indexing_default: typing.Optional[float] = pydantic.Field(default=None)
    """
    Default value of a custom dimension on a document part if the custom
    dimension value is not specified when the document part is indexed.
    
    A value of 0 means that custom dimension is not considered.
    """

    querying_default: typing.Optional[float] = pydantic.Field(default=None)
    """
    Default value of a custom dimension for a query if the value
    of the custom dimension is not specified when querying the corpus.
    
    A value of 0 means that custom dimension is not considered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
