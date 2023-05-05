import pytest 
@pytest.fixture(scope="package")
def sample_list():
  return [1,2,3,4,5,6]

def pytest_runtest_setup(item):
  pass


@pytest.fixture(scope="session")
def db_connection():
  # before the test or scope starts
  connection = "something"
  yield connection
  # as the scope or test finishes
  del connection