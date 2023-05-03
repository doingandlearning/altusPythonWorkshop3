delta = 0

# 1. Pure function!
def add(a,b):
  global delta
  ## Reading from a db, making an API call -
  delta += 1
  return a + b + delta

# 1. It depends on nothing external which is not an argument
# 2. It impacts nothing beyond itself 

# print(add(1,2))
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))

# 2. Immutability
original_list = [1,2,3,4]
print(original_list[::-1])

# for i in range(0,4):
#   original_list[i] = original_list[i] + 1
new_list = [number + 1 for number in original_list]

print(original_list)
print(new_list)


# 3. First-class functions
# - passed as arguments
# - returned from other functions
# - assign to variables

def square(x):
  return x * x

def cube(x):
  return x * x * x

def execute_and_print(func, num):
  print(func(num))

execute_and_print(cube, 3)

def create_printable_version(func):
  def printable(*args, **kwargs):
    print(func(*args, **kwargs))
  return printable


printable_cube = create_printable_version(cube)

cube(4)
printable_cube(4)


# Easier to reason about
# Easier to predict
# Easier to be concurrent
# Cacheable





def factorial(n):
  # some expensive calculation 
  return n


factorial(10) # has this function been called with this input?
                # yes: return the old result
                # no: calculate the result and store it for next time
factorial(10)
factorial(10)
factorial(10)
factorial(10)
factorial(10)