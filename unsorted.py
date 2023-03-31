import random

unsorted = []

for i in range (4):
    x = random.randint(0,500)
    unsorted.append(x)
print(unsorted)


def sortList(lst):
    """Takes in a list of unsorted numbers and orders them from smallest to biggest

    Args:
        lst (list): a list of numbers (int)
        
    Return:
        lst (list): prints a sorted list
    """
    listLength = len(lst)
    
    for i in range(listLength):
        for b in range(listLength - i - 1): #j is the total amount of comparisons made
            if lst[b] > lst[b + 1]:
                lst[b], lst[b+1] = lst[b+1], lst[b]
    print(lst)

sortList(unsorted)
