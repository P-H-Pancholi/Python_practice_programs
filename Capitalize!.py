str = list(input())
length = len(str)
if str[0].isalpha() == True and str[0].islower() == True:
        str[0] = str[0].upper()
for i in range(length - 1):
	if str[i] == " ":
		if str[i + 1].isalpha() == True and str[i + 1].islower() == True:
			str[i + 1] = str[i + 1].upper()


print("".join(str))
