import pytest
from pathlib import Path

def add(a,b):
  return a + b


@pytest.mark.parametrize("input_value, expected_result", [
  ((1,2), 3),
  ((-2, 0), -2),
  ((2, -2), 0)
])
def test_adding_integers_works(sample_list, input_value, expected_result):
  assert len(sample_list) == 6
  assert add(input_value[0], input_value[1]) == expected_result

def test_sample_list(sample_list):
  assert len(sample_list) == 6


@pytest.mark.parametrize("input_value, expected_result", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
    (-2, 4),
    (0.5, 0.25)
])
def test_square(input_value, expected_result):
    assert input_value ** 2 == expected_result


def divide(a,b):
  if b == 0:
    raise ZeroDivisionError("division by zero")
  return a / b

def test_divide_by_zero_exception():
  with pytest.raises(ZeroDivisionError) as exc_info:
    divide(2,0)
  assert str(exc_info.value) == "division by zero"

def get_home_directory():
  return Path.home()

def test_get_home_directory(monkeypatch):
  monkeypatch.setattr(Path, "home", lambda: Path("/abc"))
  x = get_home_directory()
  assert x == Path("/abc")