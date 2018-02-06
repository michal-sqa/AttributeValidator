import pytest
import _environment

def pytest_addoption(parser):
    parser.addoption("--env", default='test')
    parser.addoption("--user", default='test')
    parser.addoption("--password", default='test')

@pytest.fixture
def environment(request):
    user_name = request.config.getoption('--user')
    user_password = request.config.getoption('--password')
    env = request.config.getoption('--env')
    environment = _environment.environments[env]
    environment._user = user_name
    environment._password = user_password
    return environment