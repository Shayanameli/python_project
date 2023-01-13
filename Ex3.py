def Collatz(number):
	c= 0
	if number > 0:
		while number != 1:
			if number % 2 == 0:
				number=number/2
			else:
				number=number*3+1
			c=c+1
	else:
		return (f'enter positive number')
	return c
Collatz(3)

def Max_Adjacent(list):
    l = []
    for i in range (0,len(list)-1):
        a= list[i] * list[i + 1]
        l.append(a)
        b=max(l)
    return b
Max_Adjacent([0,-1,1,24,1,-4,8,10])

def Robot(list):
	s=0
	w=0
	e=0
	n=0
	# robot is designed for only two destination:
	#1:e,n,e,e,n
	#2:w,n,w,n,w,w,n
	e_1=3
	n_1=2
	n_2=3
	w_2=4
	for i in list:
		if i=='n':
			n+=1
		elif i=='s':
			s+=1
		elif i=='w':
			w+=1
		elif i=='e':
			e+=1
	if (n ==n_1 and e ==e_1) or (w==w_2 and n==n_2):
		return True
	else:
		return False
Robot(['s','e','e','n','n','e'])



def Multi_division(a,b,c):
	for i in range(b):
		a=a*2
	if c%a==0:
		return True
	else:
		return False

Multi_division(42,5,10)


def Marathon(list):
	l= 0
	for i in list:
		if i < 0:
			i=i*-1
		l+= i
	if l== 25:
		return True
	else:
		return False
Marathon([-6, 15, 4])

def Face(list) :
	a = max(list) - min(list)
	if len(list) == 0:
		Face=':/'
	else:
		for i in list:
			if i==a:
				Face = ':)'
			else:
				Face = ':('
	return Face


Face([2, 32, 1, 6, 31])

		




        





 






