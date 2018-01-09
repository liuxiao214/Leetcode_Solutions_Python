import math
def constructRectangle(area):
    m = int(math.sqrt(area))
    while m>0:
        l =area/m
        if m*l==area:
            return [l,m]
        m=m-1
       
print constructRectangle(6)
        