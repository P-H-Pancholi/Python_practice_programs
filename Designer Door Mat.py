n,m = map(int,input().split())
message = 'WELCOME'
pattern = '.|.'
for i in range(n):
	if i < n//2:
		print('-'*((m-(3 * (2*i + 1)))//2),pattern*(2*i + 1),'-'*((m-(3 * (2*i + 1)))//2),sep ="")
	elif i == n//2:
		print('-'*((m-7)//2),message,'-'*((m-7)//2),sep = "")
	else:
		print('-'*((m - 3*((2*(n-1-i) + 1)))//2),pattern*(2*(n-1-i) + 1),'-'*((m - 3*((2*(n-1-i) + 1)))//2),sep ="")
