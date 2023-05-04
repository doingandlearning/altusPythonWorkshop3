import functools
from decorators import timefunction


@functools.cache
def cached_fib(num):
    if num < 2:
        return num
    else:
        return cached_fib(num-1) + cached_fib(num-2)

def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)

@timefunction
def specific_fib(num):
  return fib(num)

@timefunction
def specific_cached_fib(num):
  return cached_fib(num)

print(specific_cached_fib(200))
print(specific_fib(40))


def add(a,b):
  return a + b

import operator
addFive = functools.partial(operator.mul, 5)

print(addFive(10))