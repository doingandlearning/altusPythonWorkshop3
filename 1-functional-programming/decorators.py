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