class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        n=len(haystack)
        m=len(needle)
        for i in range(0,n-m+1):
            j=0
            while j<m:
                if haystack[i+j]!=needle[j]:
                    break
                j+=1
            if j==m:
                return i
        return -1


class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        if len(haystack)<len(needle):
            return -1
        def findnext(s):
            a=[-1]
            if len(s)==1:
                return a
            a.append(0)
            for i in range(2,len(s)):
                k=a[i-1]
                while(k>-1):
                    if s[k]==s[i-1]:
                        a.append(k+1)
                        break
                    else:
                        k=a[k]
                if k==-1:
                    a.append(0)
            return a
        next=findnext(needle)
        i=0
        j=0
        n=len(haystack)
        m=len(needle)
        while i<n and j<m:
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            elif j!=-1 and haystack[i]!=needle[j]:
                j=next[j]
        if j==m:
            return i-j
        else:
            return -1
        
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
                

    
s=Solution2()
s1="mississippi"
s2=""
print s.strStr(s1,s2)