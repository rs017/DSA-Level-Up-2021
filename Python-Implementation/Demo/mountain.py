def highest_mountain(num_list):
    """Returns the length of highest mountain identified from a list of numbers where:
    1. A mountain is defined as a sequence of adjacent numbers
    that are strictly increasing until it reaches a peak
    and then it becomes strictly decreasing.
    2. At least three numbers are required to form a mountain"""

    '''We can approach this problem in following sequential steps:
    1. Identify peaks, i.e., number greater than its adjacent numbers.
    Also, first and last element can not be peaks.
    2. Calculating backward and forward lengths for all the peaks and keeping the highest one.'''

    # initializing maximum height to 0
    max_height = 0

    i = 1
    while i <= len(num_list) - 2:

        # initializing height to 0 for each potential peak
        height = 0

        # check for peak
        if num_list[i - 1] < num_list[i] and num_list[i] > num_list[i + 1]:
            height += 1

            # calculate backward length
            j = i
            while j >= 1 and num_list[j] > num_list[j - 1]:
                height += 1
                j -= 1

            # calculate forward length and at the same time increment scanning position for peak
            while i <= len(num_list) - 2 and num_list[i] > num_list[i + 1]:
                height += 1
                i += 1

            max_height = max(height, max_height)
        else:
            i += 1

    return max_height

