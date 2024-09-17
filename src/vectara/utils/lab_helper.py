from vectara.managers import CreateCorpusRequest, CorpusManager
from vectara.corpora.client import CorporaClient
from vectara.config import ClientConfig, HomeConfigLoader, ApiKeyAuthConfig, OAuth2AuthConfig
from vectara.types import Corpus
from typing import Union, Optional
import logging
import os
import re
import getpass



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

    #def cleanup_labs(self, name: ):

    def valid_bool(self, user_input: str):
        if user_input == 'y' or user_input == 'n':
            return True
        else:
            print("Invalid value, must be [y] or [n].")
            return False

    def valid_int(self, value: str, min_value=None, max_value=None) -> bool:
        value_int: int = -1
        try:
            value_int = int(value)
        except ValueError as e:
            self.logger.error(f"Not a number [{value}]")
            return False

        if (min_value and value_int < min_value) or (max_value and value_int > max_value):
            return False
        else:
            self.logger.info(f"Value [{value}] is between min_value [{min_value}] and [{max_value}]")
            return True

    def setup_authentication(self, profile="lab"):
        """
        Sets up the .vec_auth.yaml file in the users home directory in the "lab" profile.
        """

        #from vectara.config import ClientConfig, HomeConfigLoader, ApiKeyAuthConfig

        loader = HomeConfigLoader(profile)
        if loader.has_profile():
            self.logger.info(f"We already have a configuration for [{profile}]")
            self.logger.info("If you proceed, THIS WILL BE OVERWRITTEN!!")
            valid_choice = False
            user_input = None
            while not valid_choice:
                user_input = str(input("Do you want to update existing profile? y/[n]").strip() or "n").lower()
                valid_choice = self.valid_bool(user_input)
            if user_input == 'n':
                self.logger.info("Exiting")
                return
        else:
            self.logger.info("No existing profile found")

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
                    self.logger.error(f"Not a valid {field_name}: [{field_value}]")

            return field_value

        # Get a valid customer Id.
        customer_id = get_non_blank("Customer Id")

        auth_question = "Please select authentication type:\n\t1. API Key (Default)\n\t 2. OAuth2\nEnter 1 or 2:"
        valid_choice = False
        user_input: str = ""
        while not valid_choice:
            user_input = input(auth_question).strip()
            valid_choice = self.valid_int(user_input, min_value=1, max_value=2)
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

        self.logger.info(f"Saving configuration for profile [{profile}]")
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
