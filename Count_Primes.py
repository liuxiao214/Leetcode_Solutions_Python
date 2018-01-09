import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        a=[True]*n
        j=int(math.sqrt(n))
        count=1
        i=3
        while i<n:
            if a[i]==True:
                count+=1
                if i>j:
                    i+=2
                    continue
                k=i*i
                while k<n:
                    a[k]=False
                    k+=i
            i+=2
        return count
    
s=Solution()
print s.countPrimes(10)