class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        f1=1
        f2=2
        fn=0
        for i in range(3,n+1):
            fn=f1+f2
            f1=f2
            f2=fn
        return fn

class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2 
        return self.climbStairs(n-1)+self.climbStairs(n-2)


s=Solution()
print s.climbStairs(6)