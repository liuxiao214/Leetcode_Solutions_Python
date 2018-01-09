def intersection(nums1, nums2):
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    same = []
    while(i<len(nums2) and j<len(nums1)):
        if nums2[i] == nums1[j]:
            same.append(nums2[i])
            i = i + 1
            j = j + 1
        elif nums2[i] < nums1[j]:
            i = i + 1
        else:
            j = j + 1
    return same
print intersection([1,2,3,3,3,4,5],[1,2,2,2,3])