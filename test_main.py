
from main import is_email_valid


def test_is_email_valid(write_log) -> None:
    assert is_email_valid("dasdsa@dsadas.ru") == True


def test_is_email_invalid(write_log) -> None:
    assert is_email_valid("dasdsa@ru") == False


def test_is_email_empty(write_log) -> None:
    assert is_email_valid("") == False
