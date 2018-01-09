class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        count=1
        while n>=count:
            n=n-count
            count=count+1
        return count-1
 
 
class Solution1(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        return int((sqrt(1+8*n)-1)/2)
        
s=Solution1()
print s.arrangeCoins(8)