class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s=[]
        while head!=None:
            s.append(head.val)
            head=head.next
        for i in range(len(s)/2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True

class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        def reverselist(head):
            pre=None
            ne=None
            while head!=None:
                ne=head.next
                head.next=pre
                pre=head
                head=ne
            return pre
        slow.next=reverselist(slow.next)
        slow=slow.next
        while slow!=None:
            if slow.val!=head.val:
                return False
            slow=slow.next
            head=head.next
        return True
    
s=Solution1()
p1=ListNode(1)
p2=ListNode(1)
p3=ListNode(2)
p4=ListNode(1)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=None
print s.isPalindrome(p1)