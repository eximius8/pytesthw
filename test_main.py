import pytest
from main import is_email_valid


@pytest.fixture()
def write_log():
    with open('log.txt', 'w') as f:
        f.write('')


def test_is_email_valid(write_log) -> None:
    assert is_email_valid("dasdsa@dsadas.ru") == True 