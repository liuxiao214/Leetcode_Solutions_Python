import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        a=dict(collections.Counter(nums))
        prei=a.keys()[0]
        tempmax=0
        tempnum=0
        imax=0
        n=sorted(a.items(),key=lambda item:item[0])
        for i in range(len(n)):
            if n[i][0]==prei+1:
                tempmax=tempnum+n[i][1]
            if tempmax>imax:
                imax=tempmax
            tempnum=n[i][1]
            prei=n[i][0]
        return imax
 
 
class Solution1(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=collections.Counter(nums)# not understand
        return max(a[i+1]+a[i] for i in a if a[i+1] or [0])
        
        
s=Solution1()   
nums=[-1,0,-1,0,2,2,2,2,2,2,2]
print s.findLHS(nums)
            
            
        