# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .individual_search_result import IndividualSearchResult
from .language import Language
from .query_warning import QueryWarning
from .rewritten_query import RewrittenQuery


class QueryFullResponse(UniversalBaseModel):
    """
    The full response to a RAG query when the result is not streamed.
    """

    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    The summary of the search results.
    """

    response_language: typing.Optional[Language] = None
    search_results: typing.Optional[typing.List[IndividualSearchResult]] = pydantic.Field(default=None)
    """
    The ranked search results.
    """

    factual_consistency_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Indicates the probability that the summary is factually consistent with the results.
    The system excludes this property if it encounters excessively large outputs or search
    results.
    """

    rendered_prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rendered prompt sent to the LLM. Useful when creating customer `prompt_template` templates.
    """

    warnings: typing.Optional[typing.List[QueryWarning]] = pydantic.Field(default=None)
    """
    Non-fatal warnings that occurred during request processing
    """

    rewritten_queries: typing.Optional[typing.List[RewrittenQuery]] = pydantic.Field(default=None)
    """
    The rewritten queries for the corpora that were searched. Only populated when 
    intelligent_query_rewriting is enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
