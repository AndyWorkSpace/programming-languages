'''def FD(n):
	if n<=2:
		return n
	else:
		return FD(n-2)+FD(n-1)'''

def FD(n):
	return n if (n<=2) else FD(n-2)+FD(n-1)

print(FD(5))