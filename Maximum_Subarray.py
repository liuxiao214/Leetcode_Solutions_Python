class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=nums[0]
        temp=max
        for i in range(1,len(nums)):
            if temp<=0:
                temp=nums[i]
            else:
                temp=temp+nums[i]
            if max<temp:
                max=temp
        return max
    
s=Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])