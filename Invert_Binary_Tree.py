class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object):
    def invertTree(self, root):
        if root!=None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp=root.left
            root.left=root.right
            root.right=temp
        
        return root

class Solution1(object):
    def invertTree(self, root):
        s=[]
        while (len(s)!=0 or root!=None):
            while root!=None:
                s.append(root)
                root=root.left
            if len(s)!=0:
                root=s.pop()
                temp=root.left
                root.left=root.right
                root.right=temp
                root=root.right
        return root
                

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

s1=Solution1()
s1.invertTree(p1)

print 1

s=Solution()
s.invertTree(p1)

print 1
