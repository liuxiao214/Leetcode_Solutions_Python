def addDigits1(num):
    while num/10 >0:
        temp = num/10
        num = temp + num%10
    return num
print addDigits(38)

def addDigits(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9
print addDigits(38)

'''
num = a *10000 + b *1000 + c *100 + d *10 + e
num = (a+b+c+d+e) + (a*9999 + b*999 + c*99 + d*9)
w = (a+b+c+d+e)
H = (a*9999 + b*999 + c*99 + d*9)
num = W + H
num % 9 == W % 9
W = U + N

(x + y) % z == (x % z + y % z) % z
x % z % z == x % z

U = num % 9
'''