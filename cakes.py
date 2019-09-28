def cakes(recipe, available):
    """ Assumes recipe and available to be dictionary
        returns no of cakes that can be made from given data
    """
    temp = []
    for e in recipe.keys():
        if e not in available.keys():
            return 0
        temp.append(available[e]//recipe[e])
    return min(temp)
