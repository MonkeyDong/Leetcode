def move(n,a,bb,c):
	if(n == 1):
		print(a,'->',c)
		return
	move(n-1,a,c,bb)
	move(1,a,bb,c)
	move(n-1,bb,a,c)

move(5,'a','b','c')
