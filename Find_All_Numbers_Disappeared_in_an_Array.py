import math
def findDisappearedNumbers(nums):
    flag=[0]*len(nums)
    newnums=[]
    for i in range(0,len(nums)):
        flag[nums[i]-1]+=1
    for i in range(0,len(flag)):
        if flag[i]==0:
            newnums.append(i+1)
    return newnums
def findDisappearedNumbers_better(nums):
    newnums=[]
    for i in range(0,len(nums)):
        nums[abs(nums[i])-1]=0-abs(nums[abs(nums[i])-1])
    for i in range(0,len(nums)):
        if nums[i]>0:
            newnums.append(i+1)
    return newnums
a=[4, 3, 2, 7, 8, 2, 3, 1]
print findDisappearedNumbers(a)
print findDisappearedNumbers_better(a)
        
        
        