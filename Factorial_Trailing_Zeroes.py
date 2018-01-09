class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        while n>0:
            n=n/5
            c=c+n
        return c
 
class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        if n<5:
            return 0
        return n/5+self.trailingZeroes(n/5)
    
s=Solution1()
print s.trailingZeroes(25)