Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fizzBuzz(n):
	newlist=[]
	for i in range(1,n):
		if i%3 != 0 and i%5 != 0:
			j=i
			temp=""
			while(j>0):
				temp= j%10 + '0' + temp
				j=j/10
			newlist.append(temp)
		elif i%3 == 0 and i%5 !=0:
			newlist.append("Fizz")
		elif i%3 != 0 and i%5 == 0:
			newlist.append("Buzz")
		else:
			newlist.append("FizzBuzz")
	return newlist

>>> print fizzBuzz(15)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print fizzBuzz(15)
  File "<pyshell#12>", line 8, in fizzBuzz
    temp= j%10 + '0' + temp
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def fizzBuzz(n):
	newlist=[]
	for i in range(1,n):
		if i%3 != 0 and i%5 != 0:
			temp=str(i)
			newlist.append(temp)
		elif i%3 == 0 and i%5 !=0:
			newlist.append("Fizz")
		elif i%3 != 0 and i%5 == 0:
			newlist.append("Buzz")
		else:
			newlist.append("FizzBuzz")
	return newlist

>>> print fizzBuzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14']
>>> def fizzBuzz(n):
	newlist=[]
	for i in range(1,n+1):
		if i%3 != 0 and i%5 != 0:
			temp=str(i)
			newlist.append(temp)
		elif i%3 == 0 and i%5 !=0:
			newlist.append("Fizz")
		elif i%3 != 0 and i%5 == 0:
			newlist.append("Buzz")
		else:
			newlist.append("FizzBuzz")
	return newlist

>>> print fizzBuzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
>>> 
