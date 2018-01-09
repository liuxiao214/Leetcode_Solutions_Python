class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=""
        if n<1:
            return s
        while n>0:
            d=n%26
            n=n/26
            if d==0:
                n-=1
                d=26
            s=chr(64+d)+s
        return s

class Solution1(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=""
        if n<1:
            return s
        while n>0:
            n=n-1
            d=n%26
            n=n/26
            s=chr(65+d)+s
        return s

s=Solution1()
print s.convertToTitle(52)
        