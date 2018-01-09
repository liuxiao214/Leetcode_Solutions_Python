class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        dl=self.minDepth(root.left)
        dr=self.minDepth(root.right)
        if dl==0:
            return 1+dr
        if dr==0:
            return 1+dl
        return 1+min(dl,dr)
    
s=Solution()
p1=TreeNode(1)
p2=TreeNode(2)
p3=TreeNode(3)
p4=TreeNode(4)
p1.left=p2
p1.right=p3
p2.left=p4
p2.right=None
p3.left=None
p3.right=None
p4.left=None
p4.right=None
print s.minDepth(p1)