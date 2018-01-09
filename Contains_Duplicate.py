import collections
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sum(v for v in collections.Counter(nums).values() if v<2)<len(nums)

class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))<len(nums)
s=Solution1()
nums=[1,2,3,3,3,4,4]
print s.containsDuplicate(nums)