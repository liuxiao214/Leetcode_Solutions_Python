class TreeNode(object):
    def __init__(self,x):
        self.x=x
        self.left=None
        self.right=None
        
class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        a=self.maxDepth(root.left)
        b=self.maxDepth(root.right)
        if a>b:
            return a+1
        else:
            return b+1
        
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)
p1.left = p2
p1.right = p3
p2.left = p4
p2.right = p5
p3.left = None
p3.right = None
p4.left = None
p4.right = None
p5.left = None
p5.right=None

s=Solution()
print s.maxDepth(p1)