import math
def encryption(s):
    temp = []
    s.replace(" ","")
    i = len(s)
    row = int(math.floor(math.sqrt(i)))
    column = int(math.ceil(math.sqrt(i)))
    for i in range(0,row+1):
        temp.append(s[i::column])
    temp_s = " ".join(temp)
    print(str(column) + str(row))
    print(temp_s)
    return temp_s

s = input()
encryption(s)
