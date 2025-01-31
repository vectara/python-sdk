# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class TableExtractionConfig(UniversalBaseModel):
    """
    (Optional) Configuration for table extraction from the document.
    """

    extract_tables: bool = pydantic.Field()
    """
    If set to true, the platform will attempt to extract tables from the document.
    The tables will be indexed as separate document parts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
