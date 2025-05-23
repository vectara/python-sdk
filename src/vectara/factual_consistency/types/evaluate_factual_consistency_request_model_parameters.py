# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EvaluateFactualConsistencyRequestModelParameters(UniversalBaseModel):
    """
    The model parameters for the evaluation.
    """

    model_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the model to use for evaluation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
