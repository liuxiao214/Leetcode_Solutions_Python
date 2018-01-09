class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        mid=len(nums)/2
        p=TreeNode(nums[mid])
        leftnums=nums[0:mid]
        rightnums=nums[mid+1:len(nums)]
        p.left=self.sortedArrayToBST(leftnums)
        p.right=self.sortedArrayToBST(rightnums)
        return p
 
class Solution1(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        mid=len(nums)/2
        p=TreeNode(nums[mid])
        p.left=self.sortedArrayToBST(nums[0:mid])
        p.right=self.sortedArrayToBST(nums[mid+1:len(nums)])
        return p   
    
s=Solution1()
print s.sortedArrayToBST([1,2,3]).val