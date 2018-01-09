import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0 or len(nums2)==0:
            return []
        nums1.sort()
        nums2.sort()
        a=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                a.append(nums1[i])
                i=i+1
                j=j+1
            elif nums1[i]>nums2[j]:
                j=j+1
            else:
                i=i+1
        return a
  
class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
    
s=Solution1()
print s.intersect([1,2,2,3],[2,2])
        
        