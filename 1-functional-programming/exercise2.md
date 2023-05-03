# Exercise: Create a decorator

Write a decorator `count_calls` that counts the number of times a function is called and prints this information each time the decorated function is executed.

# Requirements

- The decorator should keep track of the number of times each decorated function is called.
- It should print the function name and the number of times it has been called each time the decorated function is executed.

# Possible steps
1. Create the `count_calls` decorator.
2. Decorate two different functions with `count_calls`.
3. Call the decorated functions multiple times and observe the printed output.


Here's a template to get you started:

```python
def count_calls(func):
    # TODO: Implement the decorator
    pass

@count_calls
def greet(name):
    print(f"Hello, {name}!")

@count_calls
def add(a, b):
    return a + b

# Call the decorated functions multiple times
greet("Alice")
greet("Bob")

result = add(1, 2)
result = add(3, 4)
```

# Tips

1. Define a variable `count` inside the `count_calls` function to store the number of times the decorated function is called.
2. Use a nested function, e.g., `increment_count`, inside the `count_calls` function to increment the `count` variable without exposing it.
3. In the `wrapper` function, call `increment_count` to update the count before or after calling the decorated function.
4. Print the function name and the updated count each time the decorated function is executed.

This might look like this:
```python
def count_calls(func):
    count = 0  # Initialize a variable to store the call count

    def increment_count():
        nonlocal count
        count += 1
        return count

    def wrapper(*args, **kwargs):
        # TODO: Implement the decorator logic
        pass

    return wrapper
```