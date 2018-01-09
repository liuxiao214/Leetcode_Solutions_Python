class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
import collections
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a=[]
        if root==None:
            return a
        s=[]
        p=root
        b=[]
        while len(s)!=0 or p!=None:
            while p!=None:
                s.append(p)
                p=p.left
            if len(s)!=0:
                p=s.pop(0)
                b.append(p.val)
                p=p.right
        c=collections.Counter(b)
        ma=max(c.values())
        for i in c.keys():
            if c[i]==ma:
                a.append(i)              
        return a
    
s=Solution()
p1=TreeNode(1444444444)
p1.left=None
p1.right=None

print s.findMode(p1)
