def generate_hashtag(s):
    """Takes string as input
        returns a string with prefix '#' ,removing spaces
        ,capitalizing first letter and rest of string
        uncaptilized
    """
    if s == "":
        return False
    temp = s.split(' ')
    l_temp = []
    for e in temp:
        if e != "":
            temp_s = e[0].upper() + e[1:].lower()
            l_temp.append(temp_s)
    p = "".join(l_temp)
    q = "#" + p
    if len(q) > 140:
        return False
    return q
