"""
time: O(n log(n)) since we use a sort algorithm | space: O(n) the length of
the some_array
"""


def sorted_squared_array(array):
    # start by initializing the some_array and it's index values
    some_array = [0 for i in array]
    lower_index = 0
    higher_index = len(array) - 1

    """
    traverse the some_array from start to end:
    1. initializing the indexes of the some_array
    2. if the abs(smaller_value)>abs(larger_value) then square it and increment
    3. else square the larger_value decrement index
    3. return the output
    """
    for index in reversed(range(len(array))):
        """
        create the new index dependent on previously declared some_array index above
        """
        smaller_value = array[lower_index]
        larger_value = array[higher_index]

        if abs(smaller_value) > abs(larger_value):
            some_array[index] = smaller_value * smaller_value
            lower_index += 1
        else:
            some_array[index] = larger_value * larger_value
            higher_index -= 1

    return some_array


print(sorted_squared_array([1, 2]))



