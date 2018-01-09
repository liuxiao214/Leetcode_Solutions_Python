class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def sub(s,t):
            m={}
            for i in range(len(s)):
                if s[i] not in m.keys():
                    m[s[i]]=t[i]
                else:
                    if m[s[i]]!=t[i]:
                        return False
            return True
        return sub(s, t) and sub(t,s)

class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a1=[-1]*256
        a2=[-1]*256
        for i in range(len(s)):
            if a1[ord(s[i])] != a2[ord(t[i])]:
                return False
            a1[ord(s[i])]=i
            a2[ord(t[i])]=i
        return True
        
        
        
s=Solution1()
s1="wbb"
s2="twc"
print s.isIsomorphic(s1,s2)