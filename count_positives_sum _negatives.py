def count_positives_sum_negatives(arr):
    """ Assumes arr to be list of positive and negative numbers
        returns list of no of postive int and sum of negative int
    """
    Count = [0,0]
    for e in arr:
        if e > 0:
            Count[1] += 1
        else:
            Count[2] += e
    return Count
