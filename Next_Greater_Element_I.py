Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def nestGreatElement(findNums,nums):
	numss=[]
	for i in range(0,len(findNums)):
		for j in range(0,len(nums)):
			if findNums[i]==nums[j]:
				flag=0
				for k in range(j+1,len(nums)):
					if nums[k]>nums[j]:
						numss.append(nums[k])
						flag=1
						break
				if flag==0:
					nums.append(-1)
	return numss

>>> a=[4,1,2]
>>> b=[1,3,4,2]
>>> print findGreatElement(a,b)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print findGreatElement(a,b)
NameError: name 'findGreatElement' is not defined
>>> print nextGreatElement(a,b)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print nextGreatElement(a,b)
NameError: name 'nextGreatElement' is not defined
>>> def nextGreatElement(findNums,nums):
	numss=[]
	for i in range(0,len(findNums)):
		for j in range(0,len(nums)):
			if findNums[i]==nums[j]:
				flag=0
				for k in range(j+1,len(nums)):
					if nums[k]>nums[j]:
						numss.append(nums[k])
						flag=1
						break
				if flag==0:
					nums.append(-1)
	return numss

>>> print nextGreatElement(a,b)
[3]
>>> def nextGreatElement(findNums,nums):
	numss=[]
	for i in range(0,len(findNums)):
		for j in range(0,len(nums)):
			if findNums[i]==nums[j]:
				flag=0
				for k in range(j+1,len(nums)):
					if nums[k]>nums[j]:
						numss.append(nums[k])
						flag=1
						break
				if flag==0:
					numss.append(-1)
	return numss

>>> print nextGreatElement(a,b)
[-1, 3, -1]
>>> 
