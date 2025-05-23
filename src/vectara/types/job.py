# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .corpus_key import CorpusKey
from .job_state import JobState
from .job_type import JobType


class Job(UniversalBaseModel):
    """
    A background job for processing long-running operations on the platform.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the job.
    """

    type: typing.Optional[JobType] = pydantic.Field(default=None)
    """
    The type of job.
    """

    corpus_keys: typing.Optional[typing.List[CorpusKey]] = pydantic.Field(default=None)
    """
    The corpora that this job belongs to. It may not belong to any corpora.
    """

    state: typing.Optional[JobState] = None
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Specifies when the job was created.
    """

    started_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Specifies when the job was started.
    """

    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Specifies when the job was completed.
    """

    created_by_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The username of the user who created the job. This property may be missing, e.g., if the job was created by the system, not a user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
