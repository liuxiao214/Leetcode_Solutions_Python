#import algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
    
s=Solution()
print s.majorityElement([1,1,1,1,2,3,1,4,1])