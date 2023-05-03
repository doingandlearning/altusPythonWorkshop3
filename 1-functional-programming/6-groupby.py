import itertools
from operator import itemgetter

data = [("apple", "fruit"), ("banana", "fruit"), ("tomato", "fruit"),
("carrot", "vegetable"), ("potato", "vegetable")]

# knowing a tomato is a fruit is intelligent
# knowing not to put it in a fruit salad is wise

def find_category(item):
  return item[1]

print(list(itertools.groupby(data, lambda item: item[1])))

for key, group in itertools.groupby(data, itemgetter(1)):
  print(f"{key}: {[item[0] for item in group]}")