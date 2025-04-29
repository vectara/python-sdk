import os
import pytest

@pytest.fixture(autouse=True)
def load_env():
    """Ensure environment variables are loaded before each test."""
    if not os.getenv("VECTARA_API_KEY"):
        pytest.fail("VECTARA_API_KEY not found in environment variables. Make sure .env file exists and contains the key.") 