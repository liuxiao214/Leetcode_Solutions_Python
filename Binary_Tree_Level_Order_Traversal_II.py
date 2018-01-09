class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        a=[[]]
        if root==None:
            return []
        def DFS(p,level):
            if p==None:
                return None
            if level==len(a):
                a.append([])
            a[level].append(p.val)
            DFS(p.left, level+1)
            DFS(p.right,level+1)
        DFS(root,0)
        return a[::-1]
 
import Queue 
class Solution1(object):
    def levelOrderBottom(self, root):
        a=[]
        if root==None:
            return []  
        q=Queue.Queue()
        q.put(root)
        p=root
        size=1
        while(q.empty()==False):
            temp=[]
            while(size>0):
                p=q.get()
                temp.append(p.val)
                if p.left!=None:
                    q.put(p.left)
                if p.right!=None:
                    q.put(p.right)
                size=size-1
            if len(temp)>0:
                a.append(temp)
            size=q.qsize()
        return a[::-1]
        
        
s=Solution1()
p1 = TreeNode(3)
p2 = TreeNode(9)
p3 = TreeNode(20)
p4 = TreeNode(15)
p5 = TreeNode(7)
p1.left = p2
p1.right = p3
p2.left = None
p2.right = None
p3.left = p4
p3.right = p5
p4.left = None
p4.right = None
p5.left = None
p5.right = None

p6=None
print s.levelOrderBottom(p1)