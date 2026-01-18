names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sorted_list = sorted(names, key=lambda name: len(name))

print("Unsorted list: ")
for name in names:
    print(name)

print()
print()
print("Sorted list: ")
for name in sorted_list:
    print(name)