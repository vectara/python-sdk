from vectara.core.pydantic_utilities import IS_PYDANTIC_V2
from vectara.errors.not_found_error import NotFoundError
from vectara.corpora.client import CorporaClient
from vectara.types import (Corpus, FilterAttribute, CorpusCustomDimension, CorpusLimits, FilterAttributeType,
                           FilterAttributeLevel)
from typing import List, Union, Optional, ClassVar, Dict
from pydantic import Field, Extra, BaseModel, ConfigDict
import logging
import time

class CreateCorpusRequest(BaseModel):
    """
    Created temporarily as we don't have wrapper around parameters for Corpus Creation.
    """

    key: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    """
    Name for the corpus. This value defaults to the key.
    """

    description: Optional[str] = Field(default=None)
    """
    Corpus description.
    """

    queries_are_answers: Optional[bool] = Field(default=None)
    """
    Queries made to this corpus are considered answers, and not questions.
    This swaps the semantics of the encoder used at query time.
    """

    documents_are_questions: Optional[bool] = Field(default=None)
    """
    Documents inside this corpus are considered questions, and not answers.
    This swaps the semantics of the encoder used at indexing.
    """

    encoder_id: Optional[str] = Field(default=None)
    """
    The encoder used by the corpus.
    """

    filter_attributes: Optional[List[FilterAttribute]] = Field(default=None)
    """
    The new filter attributes of the corpus.
    """

    custom_dimensions: Optional[List[CorpusCustomDimension]] = Field(default=None)
    """
    The custom dimensions of all document parts inside the corpus.
    """

    if IS_PYDANTIC_V2:
        model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow", frozen=False)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = False
            smart_union = True
            extra = Extra.allow

class CorpusBuilder:

    corpus: Corpus

    def __init__(self, name: str):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.corpus = Corpus.model_validate({
            'name': name
        })

    def name(self, name: str):
        self.corpus.name = name
        return self

    def description(self, description: str):
        self.corpus.description = description
        return self

    def add_attribute(self, name: str, description: str, indexed: bool = True, attr_type: str = "text",
                      level: FilterAttributeLevel = "document"):
        """
        Adds a filter attribute to the given corpus.

        :param name: The name of this corpus.
        :param description: Description for this filter attribute.
        :param indexed: Whether this attribute is indexed (defaults to True)
        :param attr_type: the type is taken from the FilterAttributeType and defaults to "text".
        :param level: Whether this is document (default) or part
        :return: ourselves
        """

        attribute_dict = {
            "name": name,
            "description": description,
            "indexed": indexed,
            "type": attr_type,
            "level": level
        }
        attribute = FilterAttribute.model_validate(attribute_dict)

        if not self.corpus.filter_attributes:
            self.corpus.filter_attributes = []
        self.corpus.filter_attributes.append(attribute)
        return self

    def add_dimension(self, name: str, indexing_default: Union[int, float] = 0,
                      querying_default: Union[int, float] = 0):

        dimension = CorpusCustomDimension.model_validate({
            "name": name,
            "indexing_default": indexing_default,
            "querying_default": querying_default
        })

        if not self.corpus.custom_dimensions:
            self.corpus.custom_dimensions = []
        self.corpus.custom_dimensions.append(dimension)

        return self

    def build(self):
        return self.corpus


class CorpusManager:
    """
    Provides a layer of intelligence over the operations regarding corpus lifecycle.
    """

    def __init__(self, corpora_client: CorporaClient):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.corpora_client = corpora_client

    def find_corpora_with_filter(self, name_filter: Optional[str] = "", limit: Optional[int] = None) -> List[Corpus]:
        if not name_filter:
            name_filter = ""

        def list_corpora_gen():
            response = self.corpora_client.list(filter=name_filter, limit=100)
            for item in response:
                yield item

        corpora = []

        for corpus in list_corpora_gen():
            corpora.append(corpus)
            if limit and len(corpora) >= limit:
                break

        return corpora

    def find_corpora_by_name(self, name: str) -> List[Corpus]:
        """
        Searches for a corpus by an exact name, using the filter specified. This is more reliable than using
        the existing filter which will match on "contains" and may also return duplicates.

        :param name: The name of the corpus we want.
        :return: A list of zero or more matching corpora with the same name.
        """

        corpora = self.find_corpora_with_filter(name)
        found: List[Corpus] = []
        for potential in corpora:
            if potential.name == name:
                self.logger.info(f"Found corpus with name [{potential.name}] and key [{potential.key}]")
                found.append(potential)

        return found

    def find_corpus_by_name(self, name: str, fail_if_not_exist=True) -> Union[Corpus, None]:
        corpora = self.find_corpora_with_filter(name)

        found = None
        for potential in corpora:
            self.logger.info(f"Checking corpus with name [{potential.name}]")
            if potential.name == name:
                if found:
                    raise Exception(f"We found multiple matching corpus with name [{name}]")
                else:
                    found = potential

        if not found:
            if fail_if_not_exist:
                raise Exception(f"We did not find a corpus matching [{name}]")
            else:
                self.logger.info("No corpus with name [" + name + "] can be found")
                return None
        else:
            self.logger.info(f"Our corpus id is [{found.id}]")
            return found

    def find_corpus_by_key(self, key: str) -> Union[Corpus, None]:
        try:
            return self.corpora_client.get(key)
        except NotFoundError as e:
            self.logger.info(f"No corpus found with key [{key}]")
            return None

    def delete_corpus_by_name(self, name: str) -> bool:
        self.logger.info(f"Deleting existing corpus named [{name}]")

        # The filter below will match any corpus with "verified-corpus" anywhere in the name, so we need a
        # client side check to validate equivalence.
        existing_corpora = self.find_corpora_with_filter(name)
        self.logger.info(f"We found [{len(existing_corpora)}] potential matches")
        found = False
        for existing_corpus in existing_corpora:
            if existing_corpus.name == name:
                # The following code will delete the corpus
                if not existing_corpus.key:
                    raise Exception(f"Corpus result from list has returned a corpus {existing_corpus.name} without "
                                    "a key")
                self.logger.info(f"Deleting existing corpus with key [{existing_corpus.key}]")
                self.corpora_client.delete(existing_corpus.key)
                found = True
            else:
                self.logger.info(
                    f"Ignoring corpus with key [{existing_corpus.key}] as it doesn't match our target name exactly")
        return found

    def create_corpus(self, corpus: Union[CreateCorpusRequest, Dict], delete_existing=False, unique=True) -> Corpus:
        """
        Creates a new corpus with sensible defaults. Look at CorpusBuilder for a simplified notation
        to create a corpus.

        :param corpus: the new corpus to create.
        :param delete_existing: whether we delete an existing corpus with the same name.
        :param unique: whether we fail if there is an existing corpus of the same name.
        :return: the key of the new corpus.

        """
        if isinstance(corpus, Dict):
            corpus = CreateCorpusRequest.model_validate(corpus)

        if not corpus.name:
            raise Exception("You must supply a corpus name")
        self.logger.info(f"Performing account checks before corpus creation for name [{corpus.name}]")
        existing_keys: List[Optional[str]] = []
        if corpus.key:
            existing_corpus = self.find_corpus_by_key(corpus.key)
            if existing_corpus:
                self.logger.info(f"We found existing corpus with key [{existing_corpus.key}]")
                existing_keys.append(existing_corpus.key)
        else:
            existing_keys = [x.key for x in self.find_corpora_by_name(corpus.name)]
            if len(existing_keys) > 0:
                self.logger.info(f"We found existing corpus with name [{corpus.name}]")

        has_existing = len(existing_keys) > 0
        if has_existing:
            if delete_existing:
                for key in existing_keys:
                    # MyPy has a problem that the key below is optional even though we validated it present above.
                    if key:
                        self.corpora_client.delete(key)
            elif unique:
                raise Exception(f"Unable to create a corpus with the name [{corpus.name}] as there were existing ones and "
                                f"the flag \"delete_existing\" is \"False\".")
            else:
                self.logger.warning(f"There is a potential for confusion as there is already a corpus with name [{corpus.name}]")
        self.logger.info("Account checks complete, creating the new corpus")

        result =  self.corpora_client.create(
            **corpus.__dict__
        )
        return result

    def delete(self, key: Optional[str]):
        if not key:
            # We put this in because a "key" returned from a corpus listing
            # Is "optional" on the domain structure. Even if it will never be "None".
            raise TypeError("You must supply a key")

        self.logger.info(f"Deleting corpus with key [{key}]")
        self.corpora_client.delete(key)
        self.logger.info(f"Corpus [{key}] deleted")

