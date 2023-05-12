import random
import time

unsorted = []

for i in range(100):
    unsorted_list = random.randint(0, 500)
    append = unsorted.append(unsorted_list)
print(unsorted)


def bubble_sort_list(lst):
    start_time = time.time_ns() / 1000
    """Takes in a list of unsorted numbers and orders them from smallest to biggest

    Args:
          lst (list): a list of numbers (int)

    Return:
        lst (list): prints a sorted list
    """
    list_length = len(lst)

    for bitter in range(list_length):
        for b in range(list_length - bitter - 1):  # b is the total amount of comparisons made
            if lst[b] > lst[b + 1]:
                lst[b], lst[b + 1] = lst[b + 1], lst[b]
    print(lst)
    end_time = time.time_ns() / 1000
    elapsed_time = (end_time - start_time)
    print(f"Bubble sort elapsed time: {elapsed_time}ms")


bubble_sort_list(unsorted)
