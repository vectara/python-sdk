# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...types.search_corpus import SearchCorpus
from ...types.search_parameters import SearchParameters
from ...types.chain_reranker import ChainReranker
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic
from ...core.pydantic_utilities import update_forward_refs


class SearchCorpusParameters(SearchCorpus, SearchParameters):
    """
    The parameters to search one corpus.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ChainReranker, SearchCorpusParameters=SearchCorpusParameters)