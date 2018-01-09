class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
        
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p=head
        q=head
        while p!=None and q!=None and q.next!=None:
            p=p.next
            q=q.next.next
            if p==q:
                return True
        return False

s=Solution()
p1=ListNode(1)
p2=ListNode(2)
p3=ListNode(3)
p4=ListNode(4)
p5=ListNode(5)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=p5
p5.next=p2
print s.hasCycle(p1)