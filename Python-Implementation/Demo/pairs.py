def pair_sum(num_list, target_sum):
    """Returns a tuple of pair of numbers
    from a list of unsorted numbers
    that sums to target_sum in linear time.
    Had the list been sorted,
    we could have even used two pointer method."""

    # initializing lookup set
    complement_lookup = set()

    for num in num_list:
        # Look up additive inverse/complement of the number from the set
        # If found, return the pair, else add the number to the lookup set
        complement = target_sum-num
        if complement in complement_lookup:
            return complement, num
        else:
            complement_lookup.add(num)

    # If no such pair is found, return -1
    return -1
