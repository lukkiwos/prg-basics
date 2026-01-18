from functools import reduce
numbers = [2,4,6,3,7,5]

filtered = list(filter(lambda number: number % 2 == 0, numbers))

result = reduce(lambda x, y: x + y, filtered)

print(f"Sum of even numbers: {result}")