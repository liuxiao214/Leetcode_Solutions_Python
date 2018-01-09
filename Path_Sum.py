class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        if root.left==None and root.right==None and root.val==sum:
            return True
        elif root.left==None and root.right==None and root.val!=sum:
            return False
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        
s=Solution()
p1=TreeNode(-2)
p2=TreeNode(-3)
p1.left=p2
p1.right=None
p2.left=None
p2.right=None
print s.hasPathSum(p1,-5)