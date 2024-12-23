# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .header import Header
import pydantic
from .row import Row
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Data(UniversalBaseModel):
    """
    The data of a table.
    """

    headers: typing.Optional[typing.List[Header]] = pydantic.Field(default=None)
    """
    The headers of the table.
    """

    rows: typing.Optional[typing.List[Row]] = pydantic.Field(default=None)
    """
    The rows in the data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
