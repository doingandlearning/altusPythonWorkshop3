from functools import wraps

class CountCalls:
    _call_count = {}  # Initialize a dictionary to store the call count

    def __init__(self, func):
        self.func = func
        self._call_count[func.__name__] = 0

    def __call__(self, *args, **kwargs):
        self._call_count[self.func.__name__] += 1
        print(f"{self.func.__name__} has been called {self._call_count[self.func.__name__]} times.")
        return self.func(*args, **kwargs)

def count_calls(func):
    count = 0  # Initialize a variable to store the call count
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times.")
        return func(*args, **kwargs)
    return wrapper

import time 
def timefunction(message=""):
    def wrappedtimefunction(func):
        def wrapper(*args, **kwargs):
            if message:
                print(message)
            # start a timer
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            # end a timer
            print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
            return result
        return wrapper
    return wrappedtimefunction


@timefunction()
def time_me_please():
    time.sleep(0.5)
    print("I'm all done!")

time_me_please()