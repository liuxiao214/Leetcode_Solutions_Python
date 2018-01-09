class Solution(object):#time limited
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 9
        max=10**n-1
        min=10**(n-1)
        def buildPalindrome(x):
            s=str(x)[::-1]
            a=long(str(x)+s)
            return a
        i=max
        while i>=min:
            mix=buildPalindrome(i)
            j=max
            while j*j>=mix:
                if mix%j==0 and mix/j<=max:
                    return mix%1337
                j-=1
            i-=1
        return -1
    
s=Solution()
print s.largestPalindrome(2)