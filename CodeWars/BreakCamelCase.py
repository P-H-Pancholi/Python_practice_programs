def solution(s):
    s_list = []
    for char in s:
        if char.isupper():
            s_list.append(" ")
        s_list.append(char)
    return "".join(s_list)

s1 = "helloWorld"
s2 = "camelCase"
s3 = "breakCamelCase"
print(solution(s1))
print(solution(s2))
print(solution(s3))
