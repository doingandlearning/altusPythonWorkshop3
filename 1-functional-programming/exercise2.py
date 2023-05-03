
call_count = {}
def count_calls(func):
    def wrapper(*args, **kwargs):
        if func.__name__ not in call_count:
            call_count[func.__name__] = 0
        call_count[func.__name__] += 1
        print(f"{func.__name__} has been called {call_count[func.__name__]} times.")
        return func(*args, **kwargs)
    return wrapper



from decorators import CountCalls, count_calls

@count_calls
def greet(name):
    print(f"Hello, {name}!")

@CountCalls
def add(a: int, b: int):
    return a + b

# Call the decorated functions multiple times
greet("Alice")
greet("Bob")

result = add(1, 2)
result = add(3, 4)