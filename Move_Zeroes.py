def moveZeroes(nums):
    n=0
    m=0
    for i in range(0,len(nums)):
        if nums[i]==0:
            m=i
            flag=0
            for j in range(m+1,len(nums)):
                if nums[j]!=0:
                    flag=1
                    n=j
                    break
            if flag==0:
                break
            temp=nums[m]
            nums[m]=nums[n]
            nums[n]=temp
    return nums
print moveZeroes([0,0,1,2,3,0])