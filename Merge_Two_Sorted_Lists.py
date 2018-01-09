class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        p=ListNode(-1)
        q=p
        p1=l1
        p2=l2
        while p1!=None and p2!=None:
            if p1.val > p2.val:
                q.next=p2
                q=q.next
                p2=p2.next
            else:
                q.next=p1
                q=q.next
                p1=p1.next
        while p1!=None:
            q.next=p1
            q=q.next
            p1=p1.next
        while p2!=None:
            q.next=p2
            q=q.next
            p2=p2.next
        return p.next

class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        p=ListNode(-1)
        q=p
        p1=l1
        p2=l2
        while p1!=None and p2!=None:
            if p1.val > p2.val:
                q.next=p2
                q=q.next
                p2=p2.next
            else:
                q.next=p1
                q=q.next
                p1=p1.next
        if p1!=None:
            q.next=p1
        if p2!=None:
            q.next=p2
        return p.next
    
s=Solution1()
p1=ListNode(1)
q1=ListNode(2)
p1.next=None
q1.next=None
p=s.mergeTwoLists(p1,q1)
print p.val
print p.next.val