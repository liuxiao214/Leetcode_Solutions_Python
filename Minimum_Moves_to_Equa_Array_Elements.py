def minMoves(nums):
    step = 0
    nums.sort()
    i = len(nums) - 1
    while(i>0):
        step = step + (nums[i]-nums[i-1]) * (len(nums)-i)
        i = i - 1
    return step
print minMoves([2,4,7,10])