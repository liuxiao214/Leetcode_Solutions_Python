class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=[]
        flag=1
        while(n!=1):
            sum=0
            while(n>0):
                sum=sum+(n%10)**2
                n=n/10
            if sum in a:
                flag=0
                break
            else:
                a.append(sum)
            n=sum
        if flag==1:
            return True
        else:
            return False

s=Solution()
print s.isHappy(19)
        