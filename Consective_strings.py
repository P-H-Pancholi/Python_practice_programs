def longesr_consec(starr,k):
    len_list = []
    s = ""
    for e in starr:
        len_list.append(len(e))
    longest = max(len_list)
    i = len_list.index(longest)
    for j in range(i,i+k):
        s = s + starr[j]
    return s
