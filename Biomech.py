import numpy as np


def zero_crossing(curve, reference_value, start, stop):
    """Finds all locations where the values in curve[] 
    cross or are equal to the reference value.

    Args:
        curve (ndarray): numpy array
        reference_value (float): value to search for in array curve[]
        start (int): first point to begin searching for reference value in curve[]
        stop (int): last point to end the search for reference value in curve[].

    Returns:
        zlist: a list containing the indexes to the locations in curve[]
        where the values cross or are equal to the reference_value.
        rise_or_fall: a list containing the direction 'rising' or 'falling'
        for each index point found in the input array curve[].
        
            example:
    x = np.array([0, -1.1, .2, 3.2, 2.9, .8, 0.0, -.7, -.2, 0])
    crosspoints = zero_crossing(x, 0, 0, 9)  # find all 0.0's
    returns:
    zlist = [0, 1, 6, 9] 

    x = np.array([0, -1.1, .2, 3.2, 2.9, .8, 0.0, -.7, -.2, 0])
    crosspoints = zero_crossing(x, 0.2, 0, 9)  # find all 0.2's
    returns:
    zlist = [2, 5]
    """
    zlist = []  # list to hold the indexes of curve[i] = reference_value
    rise_or_fall = []  # store if index is falling or rising as it passes reference_value
    for i in range(start + 1, stop):
        if curve[i] > reference_value and curve[i-1] <= reference_value:
            zlist.append(i-1)
            rise_or_fall.append('rising')
        elif curve[i] < reference_value and curve[i-1] >= reference_value:
            zlist.append(i-1)
            rise_or_fall.append('falling')
    if curve[stop] == reference_value:
        zlist.append(stop)
        if curve[i-1] < reference_value:
            rise_or_fall.append('rising')
        else:
            rise_or_fall.append('falling')
    return zlist, rise_or_fall


x = np.array([0, -1.1, .2, 3.2, 2.9, .8, 0.0, -.7, -.2, 0])
crosspoints, rise_fall = zero_crossing(x, 0, 0, 9)
print(crosspoints)
print(rise_fall)
