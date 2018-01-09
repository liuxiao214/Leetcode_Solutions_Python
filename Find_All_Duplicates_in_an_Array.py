class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup=[]
        if len(nums)==0:
            return dup
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                dup.append(nums[i])
                i=i+1
        return dup


class Solution1(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup=[]
        if len(nums)==0:
            return dup
        i=0
        while i<len(nums):
            if nums[nums[i]-1]!=nums[i]:
                temp=nums[i]
                nums[i]=nums[nums[i]-1]
                nums[temp-1]=temp
            else:
                i+=1
        for j in range(len(nums)):
            if j+1!=nums[j]:
                dup.append(nums[j])
        return dup
 
class Solution2(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup=[]
        if len(nums)==0:
            return dup
        for i in range(len(nums)):
            nums[abs(nums[i])-1]=0-nums[abs(nums[i])-1]
            if nums[abs(nums[i])-1]>0:
                dup.append(abs(nums[i]))
        return dup
 
class Solution3(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup=[]
        if len(nums)==0:
            return dup
        for i in range(len(nums)):           
            if nums[abs(nums[i])-1]<0:
                dup.append(abs(nums[i]))
            nums[abs(nums[i])-1]=0-nums[abs(nums[i])-1]
        return dup
        
s=Solution3()
nums=[4,3,2,7,8,2,3,1]
dup=s.findDuplicates(nums)
print dup