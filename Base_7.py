class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        s=""
        flag=0
        if num<0:
            num=0-num
            flag=1
        while(num>0):
            s=str(num%7)+s
            num=num/7
        if flag==0:
            return s
        else:
            return "-"+s
        
s=Solution()
print s.convertToBase7(-7)
        