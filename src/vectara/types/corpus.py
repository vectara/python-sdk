# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .corpus_custom_dimension import CorpusCustomDimension
from .corpus_key import CorpusKey
from .corpus_limits import CorpusLimits
from .filter_attribute import FilterAttribute


class Corpus(pydantic_v1.BaseModel):
    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Vectara ID of the corpus.
    """

    key: typing.Optional[CorpusKey] = None
    name: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Name for the corpus. This value defaults to the key.
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Corpus description.
    """

    enabled: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Specifies whether the corpus is enabled or not.
    """

    chat_history_corpus: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Indicates that this corpus does not store documents amd stores chats instead.
    """

    queries_are_answers: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Queries made to this corpus are considered answers, and not questions.
    This swaps the semantics of the encoder used at query time.
    """

    documents_are_questions: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Documents inside this corpus are considered questions, and not answers.
    This swaps the semantics of the encoder used at indexing.
    """

    encoder_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The encoder used by the corpus.
    """

    filter_attributes: typing.Optional[typing.List[FilterAttribute]] = pydantic_v1.Field(default=None)
    """
    The new filter attributes of the corpus.
    """

    custom_dimensions: typing.Optional[typing.List[CorpusCustomDimension]] = pydantic_v1.Field(default=None)
    """
    The custom dimensions of all document parts inside the corpus.
    """

    limits: typing.Optional[CorpusLimits] = None
    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Indicates when the corpus was created.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}