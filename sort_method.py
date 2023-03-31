def sort(input_list: list):
    """
    Sorts a list of integers from ascending order.

    Args:
        input_list (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    list_length = len(input_list)

    for counter in range(list_length):
        for index in range(0, list_length-counter-1):
            # Swap elements if they are in the wrong order.
            if input_list[index] > input_list[index+1]:
                input_list[index], input_list[index+1] = input_list[index+1], input_list[index]
    
    return input_list
        
        
