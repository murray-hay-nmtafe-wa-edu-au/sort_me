import random
import time

unsorted = []

for i in range (100):
    x = random.randint(0,500)
    unsorted.append(x)
print(unsorted)

############################## BUBBLE SORT ##############################################################################

def bubbleSortList(lst):
    start_time = time.time_ns()/1000
    """Takes in a list of unsorted numbers and orders them from smallest to biggest

    Args:
        lst (list): a list of numbers (int)
        
    Return:
        lst (list): prints a sorted list
    """
    listLength = len(lst)
    
    for i in range(listLength):
        for b in range(listLength - i - 1): #b is the total amount of comparisons made
            if lst[b] > lst[b + 1]:
                lst[b], lst[b+1] = lst[b+1], lst[b]
    print(lst)
    end_time = time.time_ns()/1000
    elapsed_time = (end_time - start_time)
    print(f"Bubble sort elapsed time: {elapsed_time}ms")
    
##bubbleSortList(unsorted)

############################## QUICK SORT #######################################################################

def quickSortList(lst):
    listLength = len(lst)
    
    pivot = lst[listLength]
    
    