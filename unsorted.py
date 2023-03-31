import random

unsorted = []

for i in range (100):
    x = random.randint(0,500)
    unsorted.append(x)
print(unsorted)

unsorted.sort()
print(unsorted)
