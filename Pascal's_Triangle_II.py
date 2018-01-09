class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a=[0]*(rowIndex+1)
        a[0]=1
        for i in range(1,rowIndex+1):
            j=i
            while j>=1:
                a[j]=a[j]+a[j-1]
                j=j-1
        return a
    
s=Solution()
print s.getRow(5)