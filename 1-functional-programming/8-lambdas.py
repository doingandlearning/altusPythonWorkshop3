# () => 4

# () => { other statements; return; }

square_number = lambda x: x * x

print(square_number(4))

multiply_numbers = lambda x, y : x * y
print(multiply_numbers(1,2))

is_even = lambda x: x % 2 == 0

print(is_even(10))
print(is_even(11))

divide = lambda x,y: x / y

divide(1, 0)