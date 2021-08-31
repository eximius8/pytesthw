import pytest


@pytest.fixture()
def write_log():
    with open('log.txt', 'w') as f:
        f.write('')