def swap_case(s):
	result = ''
	for char in s:
		if ord(char) < 97 and ord(char) >= 65:
			result += char.lower()
		elif ord(char) >= 97 and ord(char) < 123:
			result += char.upper()
		else:
			result += char
	return(result)

s = input()
print(swap_case(s))
