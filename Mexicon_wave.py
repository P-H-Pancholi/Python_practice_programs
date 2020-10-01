def wave(str):
    temp_list = []
    n = len(str)
    for i in range(n):
        if str[i] == " ":
            continue
        s = str[0:i] + str[i].upper() + str[i+1:n]
        temp_list.append(s)
    return temp_list

s = input()
wave(s)
#def wave(str):
#    return [str[:i] + str[i].upper() + str[i+1:] for i in
#    range(len(str)) if str[i].isalpha()]
#    range
