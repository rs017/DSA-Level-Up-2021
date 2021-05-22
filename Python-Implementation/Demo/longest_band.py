def longest_chain(num_list):
    """Returns length of the longest chain found in the list of numbers num_list where:
    1. A chain is defined as a subsequence of the elements in the list
    which can be reordered in such a manner that we have sequence of consecutive numbers.
    2. Longest chain is defined by the maximum number of elements present in the chain."""

    '''We can use sorting here and then iterate over sorted list to find maximum length.
    But we can do better by using lookup.'''

    # creating a lookup set from the list provided
    num_set = set(num_list)

    # initializing maximum length to 0
    max_length = 0

    for each_num in num_set:  # we can even use num_list here

        # initializing length to 0 for each potential chain
        length = 0

        # calculate previous number
        prev_num = each_num - 1

        # if previous number does not exist in the lookup set then the given number will start the chain
        if prev_num not in num_set:
            length += 1
            next_num = each_num + 1
            while next_num in num_set:
                length += 1
                next_num += 1

        max_length = max(length, max_length)

    return max_length

