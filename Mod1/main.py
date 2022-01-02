"""
time: O(n log(n)) since we use a sort algorithm | space: O(n) the length of
the array
"""


def sorted_squared_array(array):
    # start by initializing the array and it's index values
    array = [0 for i in array]
    lower_index = 0
    higher_index = len(array) - 1

    """
    traverse the array from start to end:
    1. initializing the indexes of the array
    2. if the abs(smaller_value)>abs(larger_value) then square it and increment
    3. else square the larger_value decrement index
    3. return the output
    """
    for i in reversed(range(len(array))):
        smaller_value = array[lower_index]
        larger_value = array[higher_index]

        if abs(smaller_value) > abs(larger_value):


