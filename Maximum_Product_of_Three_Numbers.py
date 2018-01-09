class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=len(nums)-1
	a1 = nums[0] * nums[1] * nums[l]
	a2 = nums[l] * nums[l-1] * nums[l-2] 
	if a1>a2:
	    return a1
	else:
	    return a2

s=Solution()
print s.maximumProduct([1,2,3,4])