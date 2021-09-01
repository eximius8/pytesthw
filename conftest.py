import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--log",
        action="store",
        default="log.txt",
        help="log: Укажите файл для сохранения логов.",
    )


@pytest.fixture
def write_log(request):
    return request.config.getoption("--log")
