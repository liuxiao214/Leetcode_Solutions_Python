class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=[-1]*256
        count=0
        first=-1
        for i in range(len(s)):
            if a[ord(s[i])]>first:
                first=a[ord(s[i])]
            a[ord(s[i])]=i
            count=max(count,(i-first))
        return count

class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        count=1
        temp=1
        sub=""+s[0]
        f=0
        for i in range(1,len(s)):
            if sub.find(s[i])==-1:
                sub=sub+s[i]
                temp+=1
            else:
                f=sub.find(s[i])+1
                sub=sub[f::]+s[i]
                temp=temp-f+1
            if temp>count:
                count=temp
        return count
    
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={}
        count=0
        first=-1
        for i in range(len(s)):
            if s[i] in a and a[s[i]]>first:
                first=a[s[i]]
            a[s[i]]=i
            count=max(count,(i-first))
        return count
    
s=Solution2()
ss="pwwkew"
print s.lengthOfLongestSubstring(ss)