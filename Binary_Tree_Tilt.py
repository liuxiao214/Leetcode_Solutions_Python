class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def findTilt(self, root):
        self.sum=0  
        def sum_all(root):
            if root==None:
                return 0
            left=sum_all(root.left)
            right=sum_all(root.right)
            self.sum=self.sum+abs(left-right)
            return left+right+root.val        
        sum_all(root)
        return self.sum
    
s=Solution()
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
print s.findTilt(p1)