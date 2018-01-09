class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        def TreeHigh(p):
            if p==None:
                return 0
            return 1+max(TreeHigh(p.left),TreeHigh(p.right))
        b=abs(TreeHigh(root.left)-TreeHigh(root.right))
        return (b<=1 and self.isBalanced(root.left) and self.isBalanced(root.right))
    
class Solution1(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """    
        def TreeHigh(p):
            if p==None:
                return 0
            left=TreeHigh(p.left)
            if left==-1:
                return -1
            right=TreeHigh(p.right)
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return TreeHigh(root)!=-1