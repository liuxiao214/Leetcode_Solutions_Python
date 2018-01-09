class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        a=[]
        if root==None:
            return a
        def DFS(p,t,s):
            if p.left==None and p.right==None:
                t.append(s)
                return
            if p.left!=None:
                DFS(p.left, t, s+"->"+str(p.left.val))
            if p.right!=None:
                DFS(p.right, t, s+"->"+str(p.right.val))
        DFS(root,a,str(root.val))
        return a

import Queue    
class Solution1(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        a=[]
        if root==None:
            return a  
        s=[(root,str(root.val))]
        while len(s)!=0:
            p,t=s.pop(0)
            if p.left==None and p.right==None:
                a.append(t)
            if p.left!=None:
                s.append((p.left,t+"->"+str(p.left.val)))
            if p.right!=None:
                s.append((p.right,t+"->"+str(p.right.val)))
        return a
    
class Solution2(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        a=[]
        if root==None:
            return a
        q=Queue.Queue((root,str(root.val)))
        while len(q)!=0:
            p,t=q.get()
            if p.left==None and p.right==None:
                a.append(t)
            if p.left!=None:
                q.put((p.left,t+"->"+str(p.left.val)))
            if p.right!=None:
                q.put((p.right,t+"->"+str(p.right.val)))        
        return a