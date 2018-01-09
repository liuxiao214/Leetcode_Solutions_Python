Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def findComplement(num):
	a=[]
	sum=0
	while(num>0):
		a.append(num%2)
		num=num/2
	for i in range(0,len(a)):
		sum=sum+(1-a[i])*(2**i)

	
>>> print findComplement(5)
None
>>> def findComplement(num):
	a=[]
	sum=0
	while(num>0):
		a.append(num%2)
		num=num/2
	for i in range(0,len(a)):
		sum=sum+(1-a[i])*(2**i)
	return num

>>> print findComplement(5)
0
>>> print 2 ** 3
8
>>> def findComplement(num):
	a=[]
	sum=0
	while(num>0):
		a.append(num%2)
		num=num/2
	for i in range(0,len(a)):
		sum=sum+(1-a[i])*(2**i)
	return sum

>>> print findComplement(5)
2
>>> 
