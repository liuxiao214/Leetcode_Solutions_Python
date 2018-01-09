class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum=""
        flag=0
        i=len(a)-1
        j=len(b)-1
        while flag==1 or i>=0 or j>=0:
            if i>=0:
                flag=flag+ord(a[i])-ord('0')
                i-=1
            if j>=0:
                flag=flag+ord(b[j])-ord('0')
                j-=1
            sum=str(flag%2)+sum
            flag=flag/2
        return sum
    
s=Solution()
s1="111"
s2="1"
print s.addBinary(s1,s2)