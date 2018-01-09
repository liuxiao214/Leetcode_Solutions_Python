import itertools
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i=len(num1)-1
        j=len(num2)-1
        ssum=""
        flag=0
        while(i>=0 or j>=0 or flag):
            sum=long(0)
            if i>=0:
                sum=sum+ord(num1[i])-48
                i=i-1
            if j>=0:
                sum=sum+ord(num2[j])-48
                j=j-1 
            sum=sum+flag
            flag=sum/10
            sum=sum%10
            ssum=str(sum)+ssum
        return ssum
class Solution1(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(
            reduce(# lei jia
                lambda a,b: 10*a+b,
                map(# ying she
                    lambda x: ord(x[0])+ord(x[1])-96,
                    list(
                        itertools.izip_longest(num1[::-1],num2[::-1],fillvalue='0')
                    )[::-1]
                )
            )
        )
        
s=Solution1()
print s.addStrings("1", "9")