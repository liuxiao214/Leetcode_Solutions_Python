class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f3=0
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            f1=nums[0]
            f2=max(nums[0],nums[1])
            i=3
            while(i<=len(nums)):
                f3=max(f2,f1+nums[i-1])
                f1=f2
                f2=f3
                i=i+1
        return f3

class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for i in range(len(nums)):
            if i%2==0:
                a=max(a+nums[i],b)
            else:
                b=max(b+nums[i],a)
        return max(a,b)

class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for i in range(len(nums)):
            a,b=b,max(b,a+nums[i])
        return b
    
s=Solution2()
nums=[6,4,9,5,8,10]
print s.rob(nums)