class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        origal=(len(nums)+1)*len(nums)/2
        now=0
        for i in nums:
            now=now+i
        return origal-now
 
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums)+1)*len(nums)/2-sum(nums)
    
s=Solution1()
print s.missingNumber([0, 1, 3])