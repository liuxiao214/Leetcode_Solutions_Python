Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  def findWords(words):
	 
  File "<pyshell#0>", line 2
    def findWords(words):
    ^
IndentationError: unexpected indent
>>> def findWords(words)£º
SyntaxError: invalid syntax
>>> def findWords(words):
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words
	
SyntaxError: invalid syntax
>>> aList = [123, 'xyz', 'zara', 'abc', 123]


>>> print "Count for 123 : ", aList.count(1)
Count for 123 :  0
>>> def findWords(words):
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		else if count1==0 and count2!=0 and count3==0:
			
SyntaxError: invalid syntax
>>> def findWords(words):
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		else if count1==0 and count2!=0 and count3==0:
			
SyntaxError: invalid syntax
>>> def findWords(words):
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		else if count1==0 and count2!=0 and count3==0:
			
SyntaxError: invalid syntax
>>> def findWords(words):
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		else if (count1==0 and count2!=0 and count3==0):
			
SyntaxError: invalid syntax
>>> def findWords(words):
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		flag2=0
		flag3=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		elif count1==0 and count2!=0 and count3==0:
			flag1=2
		else:
			flag1=3
		for i in range(1,len(item)):
			count11=a.count(item[0])
			count22=b.count(item[0])
			count33=c.count(item[0])
			if count11!=0 and count22==0 and count33==0:
				flag2=1
			elif count11==0 and count22!=0 and count33==0:
				flag2=2
			else:
				flag2=3
			if flag1==flag2:
				flag3=1
				continue
			else
			
SyntaxError: invalid syntax
>>> def findWords(words):
	newwords=[]
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		flag2=0
		flag3=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		elif count1==0 and count2!=0 and count3==0:
			flag1=2
		else:
			flag1=3
		for i in range(1,len(item)):
			count11=a.count(item[0])
			count22=b.count(item[0])
			count33=c.count(item[0])
			if count11!=0 and count22==0 and count33==0:
				flag2=1
			elif count11==0 and count22!=0 and count33==0:
				flag2=2
			else:
				flag2=3
			if flag1==flag2:
				flag3=1
				continue
			else:
				flag3=0
				break
			if flag3==1 or len(item):
				newwords.append(item)
	return newwords

>>> a=["Hello", "Alaska", "Dad", "Peace","a","b"]
>>> print findWords(a)
[]
>>> def findWords(words):
	newwords=[]
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		flag2=0
		flag3=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		elif count1==0 and count2!=0 and count3==0:
			flag1=2
		else:
			flag1=3
		for i in range(1,len(item)):
			count11=a.count(item[i])
			count22=b.count(item[i])
			count33=c.count(item[i])
			if count11!=0 and count22==0 and count33==0:
				flag2=1
			elif count11==0 and count22!=0 and count33==0:
				flag2=2
			else:
				flag2=3
			if flag1==flag2:
				flag3=1
				continue
			else:
				flag3=0
				break
			if flag3==1 or len(item):
				newwords.append(item)
	return newwords

>>> print findWords(a)
[]
>>> def findWords(words):
	newwords=[]
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		flag2=0
		flag3=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		elif count1==0 and count2!=0 and count3==0:
			flag1=2
		else:
			flag1=3
		for i in range(1,len(item)):
			count11=a.count(item[i])
			count22=b.count(item[i])
			count33=c.count(item[i])
			if count11!=0 and count22==0 and count33==0:
				flag2=1
			elif count11==0 and count22!=0 and count33==0:
				flag2=2
			else:
				flag2=3
			if flag1==flag2:
				flag3=1
				continue
			else:
				flag3=0
				break
		if flag3==1 or len(item):
			newwords.append(item)
	return newwords

>>> print findWords(a)
['Hello', 'Alaska', 'Dad', 'Peace', 'a', 'b']
>>> print a
['Hello', 'Alaska', 'Dad', 'Peace', 'a', 'b']
>>> def findWords(words):
	newwords=[]
	a=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
	   'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
	b=['a','s','d','f','g','h','j','k','l',
	   'A','S','D','F','G','H','J','K','L']
	c=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
	for item in words:
		flag1=0
		flag2=0
		flag3=0
		count1=a.count(item[0])
		count2=b.count(item[0])
		count3=c.count(item[0])
		if count1!=0 and count2==0 and count3==0:
			flag1=1
		elif count1==0 and count2!=0 and count3==0:
			flag1=2
		else:
			flag1=3
		for i in range(1,len(item)):
			count11=a.count(item[i])
			count22=b.count(item[i])
			count33=c.count(item[i])
			if count11!=0 and count22==0 and count33==0:
				flag2=1
			elif count11==0 and count22!=0 and count33==0:
				flag2=2
			else:
				flag2=3
			if flag1==flag2:
				flag3=1
				continue
			else:
				flag3=0
				break
		if flag3==1 or len(item)==1:
			newwords.append(item)
	return newwords

>>>  print findWords(a)
 
  File "<pyshell#56>", line 2
    print findWords(a)
    ^
IndentationError: unexpected indent
>>> print findWords(a)
['Alaska', 'Dad', 'a', 'b']
>>> 
