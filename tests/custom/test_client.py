import pytest


# Get started with writing tests with pytest at https://docs.pytest.org
# Must have 1 file in package "custom" or build will break!!
@pytest.mark.skip(reason="Unimplemented")
def test_client() -> None:
    assert True == True