class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or p==None or q==None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) 
        else:
            return root
        
        
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or p==None or q==None:
            return None 
        while(1):
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q) 
            else:
                return root
            
s=Solution()
s1=Solution1()

p1 = TreeNode(5)
p2 = TreeNode(3)
p3 = TreeNode(6)
p4 = TreeNode(2)
p5 = TreeNode(4)
p6 = TreeNode(1)
p1.left = p2
p1.right = p3
p2.left = p4
p2.right = p5
p3.left = None
p3.right=None
p4.left = p6
p4.right = None
p5.left = None
p5.right = None
p6.left = None
p6.right = None

q=s.lowestCommonAncestor(p1, p5, p6)
q1=s1.lowestCommonAncestor(p1, p5, p6)
print q.val
print q1.val