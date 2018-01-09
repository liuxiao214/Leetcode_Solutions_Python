class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    max=0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.max
    
    def depth(self,root):
        if root==None:
            return -1
        left=self.depth(root.left)
        right=self.depth(root.right)
        temp=left+right+2
        if temp>self.max:
            self.max=temp
        return max(left,right)+1
            
s=Solution()
p1=TreeNode(1)
p2=TreeNode(2)
p3=TreeNode(3)
p1.left=p2
p1.right=None
p2.left=p3
p2.right=None
p3.left=None
p3.right=None
print s.diameterOfBinaryTree(p1)