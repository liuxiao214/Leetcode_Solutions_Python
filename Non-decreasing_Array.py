class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
                if i==1 or nums[i-2]<=nums[i]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
                if count>1:
                    return False
        return True

class Solution1(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        a1=nums[:]
        a2=nums[:]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                a1[i]=nums[i+1]
                a2[i+1]=nums[i]
                break
        return a1==sorted(a1) or a2==sorted(a2)
        
s=Solution1()
nums=[2,3,3,2,4]
print s.checkPossibility(nums)