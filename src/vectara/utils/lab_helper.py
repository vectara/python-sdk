from vectara.managers import CreateCorpusRequest, CorpusManager
from vectara.corpora.client import CorporaClient
from vectara.config import ClientConfig, HomeConfigLoader, ApiKeyAuthConfig, OAuth2AuthConfig
from vectara.types import Corpus, QueryFullResponse
from typing import Union, Optional, List, Dict
from abc import ABC
import logging
import os
import re
import getpass
import json


class LabHelper:

    MAX_CORPUS_KEY: int = 50
    MAX_USERNAME_LENGTH: int = 20

    def __init__(self, corpus_manager: CorpusManager):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.corpus_manager = corpus_manager

    # Define a function to convert a string to camel case
    def _camel_case(self, s: str):
        # Use regular expression substitution to replace underscores and hyphens with spaces,
        # then title case the string (capitalize the first letter of each word), and remove spaces
        s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")

        # Join the string, ensuring the first letter is lowercase
        return ''.join([s[0].lower(), s[1:]])

    def _discover_user(self) -> str:
        username = os.environ.get("USERNAME")
        if not username:
            raise Exception("Could not extract username from environment prefix")
        else:
            return username

    def _build_lab_name_and_key(self, name: Optional[str], key: Optional[str] = None, user_prefix: bool = True,
                                username=None):
        if not name:
            raise Exception("You must specify a corpus name for the lab")

        if not key:
            key = re.sub('[^0-9a-zA-Z]+', '_', name).lower()

        # First create the lab name which we will use as a filter.
        if user_prefix:
            if not username:
                username = self._discover_user()
            self.logger.info(f"Found username from environment [{username}]")
            # Replace domain
            username = re.sub('@.*', '', username)

            # Replace non-alpha numeric letters with an underscore

            username = re.sub('[^0-9a-zA-Z]+', '_', username)
            if username.endswith("_"):
                username = username[0:(self.MAX_USERNAME_LENGTH - 1)]

            username = self._camel_case(username)[0:self.MAX_USERNAME_LENGTH]

            self.logger.info(f"Converted username is [{username}]")
            name = (username + " - " + name)
            # corpus.key will be validated and set by this point so we can ignore mypy
            key = username + "_" + key[0:self.MAX_CORPUS_KEY] # type: ignore

        self.logger.info(f"Lab corpus name will be [{name}]")
        self.logger.info(f"Lab corpus key will be [{key}]")
        return name, key


    def create_lab_corpus(self, corpus: CreateCorpusRequest, user_prefix=True, username=None) -> Corpus:
        """
        This will create a unique lab based based on the corpus in the request, however it will
        ensure the lab has a unique name and corpus key. This is important as the create/delete cycle
        with a re-used key can cause a race condition - so instead we make sure to create a new unique corpus
        which will have a unique name and corpus_key.

        the corpus in the request should have:
        * A name which is not longer than 50 characters.
        * A corpus key of the format lab_(id), where id is < 10 characters and all lower case / underscore

        This method will modify those properties, adding a user_prefix (if True) and adding a unique postfix
        based on existing labs with the same name.

        :param corpus:
        :param user_prefix:
        :return:
        """

        corpus_clone = corpus.copy()

        name, key = self._build_lab_name_and_key(corpus.name, corpus.key)
        corpus_clone.name = name
        corpus_clone.key = key


        self.logger.info("Creating lab corpus")
        response = self.corpus_manager.create_corpus(corpus_clone, delete_existing=True) # type: ignore
        return response

    @classmethod
    def valid_bool(cls, user_input: str):
        if user_input == 'y' or user_input == 'n':
            return True
        else:
            print("Invalid value, must be [y] or [n].")
            return False

    @classmethod
    def valid_int(cls, value: str, min_value=None, max_value=None) -> bool:
        logger = logging.getLogger(cls.__class__.__name__)

        value_int: int = -1
        try:
            value_int = int(value)
        except ValueError as e:
            logger.error(f"Not a number [{value}]")
            return False

        if (min_value and value_int < min_value) or (max_value and value_int > max_value):
            return False
        else:
            logger.info(f"Value [{value}] is between min_value [{min_value}] and [{max_value}]")
            return True

    @classmethod
    def setup_authentication(cls, profile="lab"):
        """
        Sets up the .vec_auth.yaml file in the users home directory in the "lab" profile.
        """
        logger = logging.getLogger(cls.__class__.__name__)

        loader = HomeConfigLoader(profile)
        if loader.has_profile():
            logger.info(f"We already have a configuration for [{profile}]")
            logger.info("If you proceed, THIS WILL BE OVERWRITTEN!!")
            valid_choice = False
            user_input = None
            while not valid_choice:
                user_input = str(input("Do you want to update existing profile? y/[n]").strip() or "n").lower()
                valid_choice = cls.valid_bool(user_input)
            if user_input == 'n':
                logger.info("Exiting")
                return
        else:
            logger.info("No existing profile found")

        def get_non_blank(field_name: str, sensitive=False) -> str:
            valid_field = False
            field_value = ""
            while not valid_field:
                message = f"Please enter the {field_name}:"
                if sensitive:
                    field_value = getpass.getpass(message)
                else:
                    field_value = str(input(message).strip())
                valid_field = len(field_value) > 0
                if not valid_field:
                    logger.error(f"Not a valid {field_name}: [{field_value}]")

            return field_value

        # Get a valid customerId.
        customer_id = get_non_blank("Customer Id")

        auth_question = "Please select authentication type:\n\t1. API Key (Default)\n\t 2. OAuth2\nEnter 1 or 2:"
        valid_choice = False
        user_input: str = ""
        while not valid_choice:
            user_input = input(auth_question).strip()
            valid_choice = cls.valid_int(user_input, min_value=1, max_value=2)
        choice = int(user_input)

        config: ClientConfig

        if choice == 1:
            api_key = get_non_blank("API Key", sensitive=True)
            api_key_auth_config = ApiKeyAuthConfig(api_key=api_key)
            config = ClientConfig(customer_id=customer_id, auth=api_key_auth_config)
        elif choice == 2:
            app_client_id = get_non_blank("Application Client Id")
            app_client_secret = get_non_blank("Application Client Secret", sensitive=True)
            oauth2_auth_config = OAuth2AuthConfig(app_client_id=app_client_id, app_client_secret=app_client_secret)
            config = ClientConfig(customer_id=customer_id, auth=oauth2_auth_config)
        else:
            raise Exception(f"Unexpected value: [{choice}]")

        logger.info(f"Saving configuration for profile [{profile}]")
        loader.save(config)

    def delete_labs(self, group_name:str, user_prefix=True):
        """
        Deletes all the labs with the given name match. We use the implicit username.
        :param group_name:
        :param user_prefix: Whether we should add the user prefix
        :return:
        """

        name, key = self._build_lab_name_and_key(group_name, user_prefix=user_prefix)
        self.logger.info(f"Deleting all lab corpora with matching name [{name}]")

        # Find all the corpora with group name, e.g. "getting-started" with user prefix.
        corpora = self.corpus_manager.find_corpora_with_filter(name)
        for corpus in corpora:
            self.logger.info(f"Deleting corpus [{corpus.name}] with key [{corpus.key}]")
            self.corpus_manager.delete(corpus.key)


class BaseFormatter(ABC):

    def __init__(self):
        pass

    def heading(self, heading: str, level: int = 1):
        raise Exception("Implement in subclass")

    def sentence(self, sentence: str):
        raise Exception("Implement in subclass")

    def link(self, text: str, url: str):
        raise Exception("Implement in subclass")

    def paragraph(self, paragraph: str):
        raise Exception("Implement in subclass")

    def bold(self, text: str):
        raise Exception("Implement in subclass")

    def italic(self, text: str):
        raise Exception("Implement in subclass")

    def list(self, items: List[str], level: int = 1):
        raise Exception("Implement in subclass")

    def rtl(self, text: str):
        raise Exception("Implement in subclass")

    def code(self, text: str, language=None):
        raise Exception("Implement in subclass")

class MarkdownFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()

    def heading(self, heading: str, level: int = 1):
        indent = "#" * level
        return f'\n{indent} {heading}'

    def sentence(self, sentence: str):
        return sentence

    def link(self, text, url):
        return f"[{text}]({url})"

    def paragraph(self, paragraph: str):
        return f"\n\n{paragraph}\n"

    def bold(self, text: str):
        return f"**{text}**"

    def italic(self, text: str):
        return f"*{text}*"

    def list(self, items: List[str], level: int = 1):
        if level < 1:
            raise TypeError("List level must be greater than 0")
        indent = " " * (level - 1)
        results = [f"{indent} {idx + 1}. {item}" for idx, item in enumerate(items)]
        return "\n" + "\n".join(results) + "\n"

    def rtl(self, text):
        return '<div dir="rtl">\n' + text + '</div>'

    def code(self, text: str, language=None):
        result = "\n```"
        if language:
            result += language
        result += str(text)
        result += "\n```\n"
        return result

class CitationUtil:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def streamline(self, search_response: QueryFullResponse):
        """
        Streamlines a vectara response (starting with a specific response under the outer array)

        :param search_response: the first response inside the array response
        :return: a dict containing a "summary" with citations streamlined and a list of results used with ordering preserved
        """

        # TODO 1. Create a list of search results
        # TODO 2. Iterate through the summary, and record which search result is used at which index

        summary_text = search_response.summary

        if not summary_text:
            raise Exception("You should only call streamline for responses with a summary")
        find_result = re.finditer(r"\[(\d)\]", summary_text)

        index = 1
        dict_map: Dict[str, int] = {}

        # The end index of the last match.
        last_end = None

        results = []

        result_index = []

        for match_obj in find_result:
            match = match_obj.group(1)
            self.logger.debug(f"At {index} we found {match}")
            start = match_obj.start()
            end = match_obj.end()

            if match in dict_map:
                self.logger.debug(f"We already have result [{match}] at position [{dict_map[match]}]")
                pass
            else:
                self.logger.debug(f"Recording result [{match}] at position [{index}]")
                dict_map[match] = index
                result_index.append(int(match))
                index += 1

            if last_end:
                self.logger.debug("Using end of the last match to get last text chunk")
                results.append(summary_text[last_end:start])
            else:
                self.logger.debug("First iteration, use everything from beginning to start")
                if start > 0:
                    results.append(summary_text[0:start])

            results.append("[" + str(dict_map[match]) + "]")

            last_end = end

        if last_end and last_end < len(summary_text):
            results.append(summary_text[last_end:])

        result_summary = "".join(results)

        self.logger.debug(f"After transformation, we have the following summary:\n{result_summary}")

        self.logger.debug(f"The mapping to the result summary is as follows:\n{result_index}")

        streamline_response = {
            "summary": result_summary,
            "result_indexes": result_index
        }
        return streamline_response

class ResponseSetRenderer:

    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter
        self.logger = logging.getLogger(self.__class__.__name__)

    def render(self, query: str, response: QueryFullResponse, rtl=False, show_search_results=True, heading_level=1,
               expect_summary=True):
        f = self.formatter
        results = []

        # Build Heading
        results.append(f.heading(f"Query: {query}", level=heading_level))



        summary_text = None

        results_included = False

        # Build Summary
        if expect_summary:
            if response.summary:
                citation_util = CitationUtil()
                streamlined_response = citation_util.streamline(response)
                results.append(f.paragraph(streamlined_response["summary"]))

                if show_search_results:
                    docs = []
                    for id in streamlined_response["result_indexes"]:
                        if not response.search_results:
                            self.logger.warning(f"Search results are empty, can not reference result [{id}]")
                            continue
                        result = response.search_results[id]
                        doc_id = result.document_id
                        item = f.sentence(result.text) + " " + f.italic("score: " + str(result.score) + ", doc-id: " + doc_id)
                        docs.append(item)
                    list_text = f.list(docs)
                    results.append(list_text)
                    results_included = True
            else:
                summary_text = "We did not receive a summary, there are insufficient results returned from the corpus"
                results.append(f.paragraph(summary_text))

        # Build items
        if show_search_results and not results_included:
            docs = []
            if not response.search_results:
                self.logger.warning("Search results are empty, can not create final results")
            else:
                for index, result in enumerate(response.search_results):
                    doc_id = result.document_id

                    item = f.sentence(result.text) + " " + f.italic("score: " + str(result.score) + ", doc-id: " + doc_id)
                    docs.append(item)

            list_text = f.list(docs)
            results.append(list_text)

        results_text = "".join(results)

        if rtl:
            return f.rtl(results_text)
        else:
            return results_text


def render_markdown(query: str, response: QueryFullResponse, rtl=False, show_search_results=True, heading_level=1,
                    expect_summary=True):
    formatter = MarkdownFormatter()
    renderer = ResponseSetRenderer(formatter)
    return renderer.render(query, response, rtl, show_search_results, heading_level, expect_summary=expect_summary)

def render_markdown_req(request:dict):
    formatter = MarkdownFormatter()

    result = formatter.heading(f"Request Operation [{request['operation']}] with payload:", level=3)
    result += formatter.code(json.dumps(request, indent=4), "json")

    return result
