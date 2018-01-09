class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        f="1"
        def say(s):
            i=0
            t=""
            count=1
            flag=0
            while i<len(s)-1:
                if s[i]==s[i+1]:
                    count+=1
                    flag=0
                else:
                    t=t+str(count)+s[i]
                    count=1
                    flag=1
                i+=1
            if flag==0:
                t=t+str(count)+s[i]
            else:
                t=t+"1"+s[i]
            return t
        while n>1:
            f=say(f)
            n-=1
        return f
    
s=Solution()
print s.countAndSay(4)
        