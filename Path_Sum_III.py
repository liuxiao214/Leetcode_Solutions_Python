class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root==None:
            return 0
        def signal(p,sum):
            res=0
            if p==None:
                return res
            if sum==p.val:
                res=res+1
            res=res+signal(p.left,sum-p.val)
            res=res+signal(p.right,sum-p.val)
            return res
        return signal(root,sum)+self.pathSum(root.left, sum)+self.pathSum(root.right,sum)
    
s=Solution()
p1=TreeNode(5)
p2=TreeNode(3)
p3=TreeNode(-3)
p4=TreeNode(11)
p5=TreeNode(2)
p6=TreeNode(1)
p1.left=p2
p1.right=p5
p2.left=p3
p2.right=None
p3.left=p4
p3.right=None
p4.left=None
p4.right=None
p5.left=p6
p5.right=None
p6.left=None
p6.right=None

print s.pathSum(p1,8)
