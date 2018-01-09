class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==0 or k<0:
            return 0
        count=0
        if k==0:
            d={}
            for i in range(len(nums)):
                if nums[i] in d.keys():
                    d[nums[i]]+=1
                else:
                    d[nums[i]]=1
            for i in d:
                if d[i]>1:
                    count+=1
            return count
        else:
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i+1]==nums[i]:
                    continue
                for j in range(i+1,len(nums)):
                    if nums[j]-nums[i]==k:
                        count+=1
                        break
                    if nums[j]-nums[i]>k:
                        break
            return count

class Solution1(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==0 or k<0:
            return 0
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i]-k in a:
                b.append(nums[i]-k)
            if nums[i]+k in a:
                b.append(nums[i])
            a.append(nums[i])
        return len(set(b))
    
import collections
class Solution2(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        elif k>0:
            return len(set(nums)&set(v+k for v in nums))
        else:
            return 0

class Solution3(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        c=collections.Counter(nums)
        for i in c:
            if (k>0 and i+k in c) or (k==0 and c[i]>1):
                count+=1
        return count
        
s=Solution3()
nums=[1,1,4,1,1,5]
print s.findPairs(nums, 1)
                        