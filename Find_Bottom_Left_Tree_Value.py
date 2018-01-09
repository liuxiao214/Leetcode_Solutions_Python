import Queue
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=Queue.Queue()
        q.put(root)
        result=root.val
        while q.empty()==False:
            size=q.qsize()
            temp=q.get()
            result=temp.val
            if temp.left!=None:
                q.put(temp.left)
            if temp.right!=None:
                q.put(temp.right)            
            while size>1:
                size-=1
                temp=q.get()
                if temp.left!=None:
                    q.put(temp.left)
                if temp.right!=None:
                    q.put(temp.right)                 
        return result
    

class Solution1(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=[root]
        for node in q:
            q +=filter(None,[node.right,node.left])
        return node.val
    
s=Solution1()
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
#p5 = TreeNode(5)
p6 = TreeNode(6)
p1.left = p2
p1.right = p3
p2.left = p4
p2.right = None
p3.left = p6
p3.right = None
p4.left = None
p4.right=None
#p5.left = None
#p5.right = None
p6.left = None
p6.right = None
print s.findBottomLeftValue(p1)