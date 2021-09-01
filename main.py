import re


def is_email_valid(email: str) -> bool:
    """Checks if parameter email is a valid email."""

    email_rgx = r'[^@]+@[^@]+\.[^@]+'
    return bool(re.match(email_rgx, email))
