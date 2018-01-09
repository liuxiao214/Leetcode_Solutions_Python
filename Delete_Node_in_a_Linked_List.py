class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
        
s=Solution()

p1=ListNode(1)
p2=ListNode(2)
p3=ListNode(3)
p4=ListNode(4)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=None
s.deleteNode(p2)
print p1.val
print p1.next.val
print p1.next.next.val
