def NA(n):
	if n<100:
		return False
	else:
		if n%1000==666:
			return True
		else:
			return NA(n//10)

print(NA(123666123))