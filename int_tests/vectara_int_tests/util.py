

import logging
import os

class TestUtil:

    logger = logging.getLogger(__name__ + ".TestUtil")

    def create_unique_key(cls, test_name: str, username_prefix=True):
        if not test_name:
            raise TypeError("You must supply a test name")
        elif len(test_name) < 10:
            raise TypeError("Please use a descriptive name of at least 10 characters")

        username = os.getlogin()
        # Use maximum 10 characters from username
        user_part = username.split("@")[0][:10]
        cls.logger.info(f"User prefix for test: {user_part}")

        full_test_name = f"{user_part}-{test_name}"
        return full_test_name