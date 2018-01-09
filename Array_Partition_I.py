def arrayPairSum(nums):
    sum=0
    nums.sort()
    for i in range(0,len(nums),2):
        if nums[i]>nums[i+1]:
            sum+=nums[i+1]
        else:
            sum+=nums[i]
    return sum
a=[1,3,4,2]
print arrayPairSum(a)    