# Standard function library

def length(input) -> int:
    """
    Function to calculate the length of an object.
    """

    count = 0

    for i in input:
        count += 1

    return count


def append(list_: list, input) -> list:
    """
    Function to append an input to a list.
    """

    list_ = list_ + [input]

    return list_


def is_upper(string: str) -> bool:
    """
    Function to check if a string consists entirely of uppercase letters.
    """

    if string == string.upper():
        return True
    else:
        return False


def is_lower(string: str) -> bool:
    """
    Function to check if a string consists entirely of lowercase letters.
    """

    if string == string.lower():
        return True
    else:
        return False


def enum(list_: list, start=0):
    """
    Works the same way as the built-in function enumerate(). Returns an enumerate object. 
    """
    n = start

    for elem in list_:
        yield n, elem
        n += 1


# def join_list(string: str, iterable) -> str:
#     """
#     Returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.
#     Made as an alternative of the string method str.join().
#     """

#     output = ''

#     for i in iterable:
#         output += f"{i}{string}"

#     return output
