# hof


# receives a function as an argument
# and/or returns a function

# readability
# the *one* way to do it!

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def square(x = 1):
  return x * x 

squared_numbers = list(map(lambda x: x * x, numbers))
squared_numbers_comp = [square(x) for x in numbers]

print(numbers)
print(squared_numbers)
print(squared_numbers_comp)


def is_even(x):
  return x % 2 == 0

even_numbers = list(filter(lambda x: x%2==0, numbers))
even_numbers_comp = [x for x in numbers if is_even(x)]

print(numbers)
print(even_numbers)
print(even_numbers_comp)

# reduce
from functools import reduce
import functools

def multiply(x,y):
  return x * y

print(reduce(lambda x,y: x * y, numbers))

def multiply(x,y):
  return x * y['likes']

array_dict_numbers = [
    {"likes":10},
    {"likes":13},
    {"likes":12},
    {"likes":11},
    {"likes":16},
    {"likes":16},
    ]
print(reduce(multiply, array_dict_numbers, 1))

# map, filter, reduce

# hof

# decorator

def multiply(x,y):
  return x * y

import time
# Closure

def timefunction(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    # start a timer
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    # end a timer
    print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
    return result
  return wrapper


@timefunction
def multiply_numbers(*args):
  return reduce(multiply, args)


# start timer
print(multiply_numbers(1,2,3))
print(multiply_numbers(4,5,6))
print(multiply_numbers(1,2,3,123,123,12,312,3,42,6,24,123,5,13,661,2))
# end and print timer here

print(multiply_numbers.__name__)