def pair_sum(num_list, target_sum):
    """Returns a tuple of pair of numbers from a list of unsorted numbers that sums to target_sum in linear time"""

    # initializing lookup set
    complement_lookup = set()

    for num in num_list:
        complement = target_sum-num
        if complement in complement_lookup:
            return complement, num
        else:
            complement_lookup.add(num)

    return -1
