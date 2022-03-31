# Standard function library

def len(input) -> int:
    """
    Function to calculate the length of an object.
    """

    length = 0
    
    for i in input:
        length += 1
    
    return length

def append(list: list, input) -> list:
    """
    Function to append an input to a list.
    """
    
    appendedList = list + [input]

    return appendedList

