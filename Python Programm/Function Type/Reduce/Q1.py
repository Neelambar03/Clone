# reduce
from functools import reduce

numbers = [-2, 3, -5, 6, 7, 8]
oi = reduce(lambda x, y: x if x > y else y, numbers)
print(oi)
