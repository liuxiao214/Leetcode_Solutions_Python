class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def getsubtree(nums,start,end):
            if start==end:
                return None
            max_=max(nums[start:end])
            node=TreeNode(max_)
            node.left=getsubtree(nums,start,nums.index(max_))
            node.right=getsubtree(nums, nums.index(max_)+1, end)
            return node

        return getsubtree(nums, 0, len(nums))

class Solution1(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        store=[]
        for i in range(0,len(nums)):
            cur=TreeNode(nums[i])
            while len(store)!=0 and store[len(store)-1].val<cur.val:
                cur.left=store[len(store)-1]
                store.pop()
            if len(store)!=0:
                store[len(store)-1].right=cur
            store.append(cur)
        return store[0]

class Solution2(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        node=TreeNode(max(nums))
        i=nums.index(max(nums))
        if nums[:i]:
            node.left=self.constructMaximumBinaryTree(nums[:i])
        if nums[i+1:]:
            node.right=self.constructMaximumBinaryTree(nums[i+1:])
        return node
    
s=Solution2()
nums=[3,2,1,6,0,5]
p=s.constructMaximumBinaryTree(nums)
print p.val,p.left.val,p.right.val
        