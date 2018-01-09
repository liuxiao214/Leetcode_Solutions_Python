def findMaxConsecutiveOnes(nums):
    reallenth=0
    templenth=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            templenth=templenth+1
        else:
            templenth=0
        if templenth>reallenth:
            reallenth=templenth
    return reallenth
a=[1,1,0,0,1,1,1,0,1,1,1,1]
print findMaxConsecutiveOnes(a)