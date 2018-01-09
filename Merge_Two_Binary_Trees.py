class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1==None:
            return t2
        if t2==None:
            return t1
        temp=TreeNode(t1.val+t2.val)
        temp.left=self.mergeTrees(t1.left, t2.left)
        temp.right=self.mergeTrees(t1.right, t2.right)
        return temp
    
p1 = TreeNode(1)
p2 = TreeNode(2)
p1.left = p2
p1.right = None
p2.left = None
p2.right = None

q1 = TreeNode(3)
q2 = TreeNode(4)
q1.left = None
q1.right = q2
q2.left = None
q2.right = None

s=Solution()
t=s.mergeTrees(p1,q1)
print t.val
print t.left.val
print t.right.val