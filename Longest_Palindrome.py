import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=[0]*52
        for i in range(len(s)):
            if ord(s[i])>90:
                a[ord(s[i])-97]+=1
            else:
                a[26+ord(s[i])-65]+=1
        sum=0
        flag=0
        for i in range(52):
            if a[i]%2==1:
                sum=sum+a[i]-1
                flag=1
            else:
                sum=sum+a[i]
        if flag==1:
            return sum+1
        else:
            return sum

class Solution1(object):
    def longestPalindrome(self, s):
        odd=sum( v&1 for v in collections.Counter(s).values())
        return len(s)-odd+bool(odd)
        
        
s=Solution()
print s.longestPalindrome("aaaAaaaa")