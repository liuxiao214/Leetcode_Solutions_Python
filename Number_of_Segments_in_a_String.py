class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s+' '
        count=0
        for i in range(1,len(s)):
            if s[i]==' ' and s[i-1]!=' ':
                count+=1
        return count

class Solution1(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.split(' ')
        count=0
        for i in a:
            if '' != i:
                count+=1
        return count

class Solution2(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        
s=Solution2()
ss="aan asf   a"
print ss.split()
print s.countSegments("aan asf   a")