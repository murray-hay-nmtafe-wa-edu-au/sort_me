import random

unsorted = []

for i in range (100):
    x = random.randint(0,500)
    unsorted.append(x)
print(unsorted)

#unsorted.sort()
#print(unsorted)
for num in range(len(unsorted)):
    for rnum in range(len(unsorted)- 1):
        if unsorted[num] > unsorted[rnum]:
            x = unsorted[num] 
            y = unsorted[rnum] 
            unsorted[num] = y
            unsorted[rnum] = x
print(unsorted)
