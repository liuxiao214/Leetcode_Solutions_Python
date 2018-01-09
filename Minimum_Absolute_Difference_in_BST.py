class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def getMinimumDifference(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """ 
            if root==None:
                return 0
            s=[]
            p=root
            q=root
            min=100000000
            flag=0
            while(len(s)!=0 or p!=None):
                while (p!=None):
                    s.append(p)
                    p=p.left
                if len(s)!=0:
                    p=s.pop()
                    flag=flag+1
                    if flag==1:
                        q=p
                    else:
                        if min > (p.val-q.val):
                            min=p.val-q.val
                        q=p
                    p=p.right
            return min
        
s=Solution()
p=TreeNode(5)
q1=TreeNode(4)
q2=TreeNode(7)
p.left=q1
p.right=q2
q2.left=None
q2.right=None
q1.left=None
q1.right=None
print s.getMinimumDifference(p)
            