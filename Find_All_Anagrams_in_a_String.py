class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        a=[0]*26
        b=[0]*26
        res=[]
        if len(s)<len(p):
            return res
        for i in range(0,len(p)):
            a[ord(p[i])-ord('a')]+=1
            b[ord(s[i])-ord('a')]+=1
        if a==b:
            res.append(0)
        for j in range(1,len(s)):
            if j+len(p)>len(s):
                break
            b[ord(s[j-1])-ord('a')]-=1
            b[ord(s[j+len(p)-1])-ord('a')]+=1
            if a==b:
                res.append(j)
        return res
    
s=Solution()
print s.findAnagrams("abab","ab")