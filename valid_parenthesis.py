def valid_parenthesis(strings):
    """ Assumes strings to be a string of valid_parenthesis
        returns true if the order of parenthesis is correct otherwise false
    """
    Count = 0
    for char in strings:
        if char == '(' and Count >= 0:
            Count += 1
        if char == ')':
            Count -= 1
    if Count == 0:
        return True
    else:
        return False

strings = input()
print(valid_parenthesis(strings))
