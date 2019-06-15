l1 = [1,2,3,1,2,3,1,2,3]
l2 = [1,1,1,1,2,2]

def fun(l1,l2):
	nn = 0
	for i in l2:
		s = i
		while(s != 0):
			if s in l1:
				ind = l1.index(s)
				del l1[ind]
				nn += 1
				break
			s -= 1
	return nn

print(fun(l1,l2))

