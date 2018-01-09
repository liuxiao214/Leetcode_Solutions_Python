class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a=[[]]*numRows
        for i in range(numRows):
            a[i]=[1]*(i+1)
            for j in range(1,i):
                a[i][j]=a[i-1][j-1]+a[i-1][j]
        return a

        
s=Solution()
print s.generate(6)
            