def And(a,b):
	if a == 1 and b == 1:
		return 1
	else:
		return 0

def Or(a,b):
	if a == 0 and b == 0:
		return 0
	else:
		return 1

def Not(a):
	if a == 1:
		return 0
	else:
		return 1

def Xor(a,b):
	if a == b:
		return 0
	else:
		return 1
		
def half_add(a,b,):
	d = Xor(a,b)
	c = And(a,b)
	return c,d 
	
def add(b,c,a=0):
	mid,sum = half_add(a,b)
	all = half_add(mid,c)
	return sum , all
	
c,d = add(0,1)
print(c,d)


	
	
