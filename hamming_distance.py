Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> python

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> import math
>>> print 2 ** 3
8
>>> def solution(x,y)
SyntaxError: invalid syntax
>>> def solution(x,y):
	a=[]
	b=[]
	while(x>0)
	
SyntaxError: invalid syntax
>>> def solution(x,y):
	a=[]
	b=[]
	len1=0
	l2n2=0
	sum=0
	flag=0
	while(x>0):
		a.append(x%2)
		x=x/2
	while(y>0):
		b.append(y%2)
		y=y/2
	alen=len(a)
	blen=len(b)
	if alen>blen:
		for i in range(0,blen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(blen,alen):
			if a[j]==1:
				sum=sum+1
	else:
		for i in range(0,alen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(alen,blen):
			if a[j]==1:
				sum=sum+1
	return sum
print solution(4,7)
SyntaxError: invalid syntax
>>> def solution(x,y):
	a=[]
	b=[]
	len1=0
	l2n2=0
	sum=0
	flag=0
	while(x>0):
		a.append(x%2)
		x=x/2
	while(y>0):
		b.append(y%2)
		y=y/2
	alen=len(a)
	blen=len(b)
	if alen>blen:
		for i in range(0,blen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(blen,alen):
			if a[j]==1:
				sum=sum+1
	else:
		for i in range(0,alen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(alen,blen):
			if a[j]==1:
				sum=sum+1
	return sum
    print solution(1,4)
    
  File "<pyshell#31>", line 32
    print solution(1,4)
                      ^
IndentationError: unindent does not match any outer indentation level
>>>  def solution(x,y):
	a=[]
	b=[]
	len1=0
	l2n2=0
	sum=0
	flag=0
	while(x>0):
		a.append(x%2)
		x=x/2
	while(y>0):
		b.append(y%2)
		y=y/2
	alen=len(a)
	blen=len(b)
	if alen>blen:
		for i in range(0,blen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(blen,alen):
			if a[j]==1:
				sum=sum+1
	else:
		for i in range(0,alen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(alen,blen):
			if a[j]==1:
				sum=sum+1
	return sum
  File "<pyshell#32>", line 2
    def solution(x,y):
    ^
IndentationError: unexpected indent
>>> def solution(x,y):
	a=[]
	b=[]
	len1=0
	l2n2=0
	sum=0
	flag=0
	while(x>0):
		a.append(x%2)
		x=x/2
	while(y>0):
		b.append(y%2)
		y=y/2
	alen=len(a)
	blen=len(b)
	if alen>blen:
		for i in range(0,blen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(blen,alen):
			if a[j]==1:
				sum=sum+1
	else:
		for i in range(0,alen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(alen,blen):
			if a[j]==1:
				sum=sum+1
	return sum

>>> print solution(1,4)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print solution(1,4)
  File "<pyshell#34>", line 28, in solution
    if a[j]==1:
IndexError: list index out of range
>>> def solution(x,y):
	a=[]
	b=[]
	len1=0
	l2n2=0
	sum=0
	flag=0
	while(x>0):
		a.append(x%2)
		x=x/2
	while(y>0):
		b.append(y%2)
		y=y/2
	alen=len(a)
	blen=len(b)
	if alen>blen:
		for i in range(0,blen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(blen,alen):
			if a[j]==1:
				sum=sum+1
	else:
		for i in range(0,alen):
			if a[i]!=b[i]:
				sum=sum+1
		for j in range(alen,blen):
			if b[j]==1:
				sum=sum+1
	return sum

>>> print solution(1,4)
2
>>> 
