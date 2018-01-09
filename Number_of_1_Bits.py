class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        while(n>0):
            sum=sum+n%2
            n=n/2
        return sum

class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        while(n>0):
            n=n&(n-1)
            sum=sum+1
        return sum    
s1=Solution()
s2=Solution1()
print s1.hammingWeight(13)
print s2.hammingWeight(13)