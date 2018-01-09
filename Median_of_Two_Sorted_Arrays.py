class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)==0 and len(nums2)==0:
            return 0
        if len(nums1)==0:
	    l = len(nums2) / 2
	    if len(nums2)% 2 == 0:
		return float(nums2[l - 1] + nums2[l]) / 2
	    else:
		return float(nums2[l])          
	if len(nums2)==0:
	    l = len(nums1) / 2
	    if len(nums1)% 2 == 0:
		return float(nums1[l - 1] + nums1[l]) / 2
	    else:
		return float(nums1[l])	
	ll = (len(nums1) + len(nums2)) / 2
	lu = (len(nums1) + len(nums2)) % 2
	i = 0
	j = 0
	a=[]
	while i<len(nums1) and j<len(nums2):
	    if nums1[i] <= nums2[j]:
		a.append(nums1[i])
		i+=1
	    else:
		a.append(nums2[j])
		j+=1
	while i<len(nums1) :
	    a.append(nums1[i])
	    i+=1	    
	while j<len(nums2):
	    a.append(nums2[j])
	    j+=1	    
	if lu == 0:
	    return float(a[ll-1]+a[ll])/2
	else:
	    return float(a[ll])
	
s=Solution()
a1=[1,2]
a2=[1,1]
print s.findMedianSortedArrays(a1,a2)