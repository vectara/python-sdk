# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .data import Data
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Table(UniversalBaseModel):
    """
    A table in a document.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the table within the document.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the table.
    """

    data: typing.Optional[Data] = pydantic.Field(default=None)
    """
    The data of the table.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the table.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow