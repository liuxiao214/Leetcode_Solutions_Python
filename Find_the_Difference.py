import collections
def findTheDifference(s,t):
    a=""
    for i in range(0,len(t)):
        flag=0
        for j in range(0,len(s)):
            if t[i]==s[j]:
                flag=1
                s=s[0:j-1]+s[j+1:len(s)]
                break
        if flag==0:
            a=t[i]
    return a
class Solution(object):
    def findTheDifference(self, s, t):
        return [c for c in t if s.count(c)==0 ][0]
class Solution1(object):
    def findTheDifference(self, s, t):
        return list((collections.Counter(t)-collections.Counter(s)))[0]
s="a"
t="aa"
print collections.Counter("ssde")-collections.Counter("ssdcf")
print findTheDifference(s, t)
s=Solution()
print s.findTheDifference("a","aaw")
s=Solution1()
print s.findTheDifference("as","asa")