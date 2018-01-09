import string
import collections

def firstUniqChar(s):
    return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])

def firstUniqChar2(s):
    return min([s.find(c) for c,v in collections.Counter(s).iteritems() if v==1] or [-1])

class Solution1(object):
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=list(s)
        if len(s)==0:
            return -1
        fla=0
        for i in range(len(a)):
            if a[i]=='A':
                continue
            flag=0
            for j in range(i+1,len(a)):
                if a[i]==a[j]:
                    flag=1
                    fla=1
                    a[j]='A'
            if flag==0:
                return i
        if fla==1:
            return -1

s=Solution1()
print s.firstUniqChar1("gcece")
print firstUniqChar("cece")        
print firstUniqChar2("zgcecef")  
print min([1,2,3] or [-1])
print min([-1] or [-1,-2]) 
print min([] or [1,2,4,5])   