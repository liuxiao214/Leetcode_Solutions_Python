class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        d={}
        for i in range(len(nums)):
            if nums[i] in d and (i-d[nums[i]]) <= k:
                return True
            d[nums[i]]=i
        return False


class Solution1(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for key,value in enumerate(nums):
            if value in d and key-d[value] <= k:
                return True
            d[value]=key
        return False
        
s=Solution1()
nums=[5,6,1,2,3,1]
print s.containsNearbyDuplicate(nums, 2)