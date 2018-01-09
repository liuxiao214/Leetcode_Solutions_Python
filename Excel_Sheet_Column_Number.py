class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        i=len(s)-1
        while(i>=0):
            sum=sum+(ord(s[i])-64)*(26**(len(s)-i-1))
            i=i-1
        return sum
class Solution1(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y:x*26+y,[ord(c)-64 for c in list(s)])
s=Solution()
print ord('A')-ord('B')
print s.titleToNumber("AB")
