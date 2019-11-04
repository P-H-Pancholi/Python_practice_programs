import string
size = int(input())
width = 4*(size-1) + 1
alpha = string.ascii_lowercase
for i in list(range(size))[::-1] + list(range(1, size)):
    print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))
