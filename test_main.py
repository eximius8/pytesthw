import pytest
from main import is_email_valid


@pytest.mark.parametrize(
    "email, result",
    [
        ("test@test.ru", True),
        ("w@w.com", True),
        ("123QWE@mmm.mmm", True),
        ("test@test.", False),
        ("w@", False),
        ("@tt", False),
        ("", False),
    ],
)
def test_is_email_valid(email, result, write_log) -> None:
    assert is_email_valid(email) == result, f"{email} is wrongly interpreted."
