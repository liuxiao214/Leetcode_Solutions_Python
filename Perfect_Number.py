import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<6:
            return False
        temp=num-1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                temp=temp-i-num/i
        if (int(math.sqrt(num))) ** 2==num:
            temp=temp+-int(math.sqrt(num))
        if temp==0:
            return True
        else:
            return False
 
 
class Solution1(object):#³¬Ê±
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """ 
        if num<6:
            return False
        temp=num-1
        n=num
        i=2
        while i<n:
            if num%i == 0:
                temp=temp-i-num/i
                n=num/i
                i=i+1
        if temp==0:
            return True
        else:
            return False
        
class Solution2(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """   
        a=[ 6, 28, 496, 8128, 33550336]
        if num in a:
            return True
        else:
            return False
        
s=Solution1()
print s.checkPerfectNumber(6)