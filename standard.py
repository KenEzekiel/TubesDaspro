# Standard function library

def length(input) -> int:
    """
    Function to calculate the length of an object.
    """

    count = 0
    
    for i in input:
        count += 1
    
    return count

def append(list: list, input) -> list:
    """
    Function to append an input to a list.
    """
    
    appendedList = list + [input]

    return appendedList

def isupper(string: str) -> bool:
    """
    Function to check if a string consists entirely of uppercase letters.
    """
    
    if string == string.upper:
        return True
    else:
        return False

def islower(string: str) -> bool:
    """
    Function to check if a string consists entirely of lowercase letters.
    """
    
    if string == string.lower:
        return True
    else:
        return False
