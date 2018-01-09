class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def tree2str(self, t):
            """
            :type t: TreeNode
            :rtype: str
            """    
            if t==None:
                return ""
            s=str(t.val)
            if t.left!=None:
                s=s+"("+self.tree2str(t.left)+")"
            elif t.right!=None:
                s=s+"()"
            if t.right!=None:
                s=s+"("+self.tree2str(t.right)+")"
            return s

ss=Solution()
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
print ss.tree2str(p1)