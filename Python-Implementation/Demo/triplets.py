def triplet_sum(num_list, target_sum):
    """Returns tuple of lists of three numbers from an unsorted list of number that sums to a target sum efficiently.
    The returned tuple of list must be sorted as well as triplets should be sorted."""

    '''Since we need sorted output, we will sort the input and scan from left to right.'''

    num_list.sort()

    '''Now as we have sorted list of number, we can approach this problem as: 
    Pair sum problem using two pointer approach for each number except last two.
    We can even use lookup approach for pair sum and that wouldn't impact our time complexity.'''

    # initializing empty list which will be returned as tuple
    result = []

    for i in range(len(num_list) - 2):
        remainder = target_sum - num_list[i]

        # solving pair sum problem considering target sum as remainder.
        left = i + 1
        right = len(num_list) - 1
        while left < right:
            if (num_list[left] + num_list[right]) == remainder:
                result.append([num_list[i], num_list[left], num_list[right]])

            elif (num_list[left] + num_list[right]) < remainder:
                left += 1
            else:
                right -= 1

    return result
