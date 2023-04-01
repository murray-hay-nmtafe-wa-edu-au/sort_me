import sort_method
import random

unsorted = []

for i in range (100):
    x = random.randint(0,500)
    unsorted.append(x)
print(f"UNSORTED: {unsorted} \n")

sort_method.sort(unsorted)
print(f"SORTED: {unsorted}")
