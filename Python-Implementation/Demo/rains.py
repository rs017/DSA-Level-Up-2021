def trapped_water(elevation_list):
    """Returns total amount of water trapped in between various levels mapped into the list elevation_list.
    We are given n non-negative integers representing an elevation map (elevation_list),
    where the width of each bar is 1 unit"""

    '''This problem can be better understood from the demo video of Prateek.
    We can solve this problem as water trapped would be equal sum of water trapped at each step horizontally.
    At each step water trapped would be equal to 1 * (minimum of the maximum heights from either sides - elevation at that step).
    Now for finding minimum of the maximum heights from either sides we can create two lists: 
    Representing maximum height encountered at each step from left side as well as from the right side.'''

    # calculate and store number of steps
    num_steps = len(elevation_list)

    # edge case
    if num_steps < 3:  # at-least 3 steps are required to trap water
        return 0

    # initialize lists for maximum elevations encountered from left and right side for a particular step
    max_elevation_on_left = [None] * num_steps
    max_elevation_on_right = [None] * num_steps

    # iterate and fill up the values
    max_elevation_on_left[0] = elevation_list[0]
    max_elevation_on_right[-1] = elevation_list[-1]

    for i in range(1, num_steps):
        max_elevation_on_left[i] = max(max_elevation_on_left[i - 1], elevation_list[i])
        max_elevation_on_right[num_steps - i - 1] = max(max_elevation_on_right[num_steps - i],
                                                        elevation_list[num_steps - i - 1])

    total_trapped_water = 0
    # iterate and calculate water trapped at each step
    for i in range(num_steps):
        total_trapped_water += min(max_elevation_on_left[i], max_elevation_on_right[i]) - elevation_list[i]

    return total_trapped_water

