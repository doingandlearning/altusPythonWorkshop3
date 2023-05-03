file = open("1-functional.py")
data = file.read()
print(data)
file.close() # garbage collector can be welcomed

# Context handler
with open("1-functional.py") as file:
  data = file.read()
  print(data)

# writing more 