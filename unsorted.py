import random
import time

unsorted = []
iterations = 0
print("** CREATING random list of numbers **")

for i in range (100):
    x = random.randint(0,500)
    unsorted.append(x)
print(unsorted)

#unsorted.sort()
print("** SORTING **")
time_start = time.time()
for i in range(len(unsorted)):
    for n in range(i+1, len(unsorted)):
        if i > n:
            unsorted[i], unsorted[n] = unsorted[n], unsorted[i]
        iterations += 1
print(unsorted)
time_finish = time.time()
print(f"*** Time Taken = {time_finish - time_start} seconds")
print(f"*** Iterations = {iterations}")


