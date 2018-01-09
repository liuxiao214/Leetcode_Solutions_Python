class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        if l1==None:
            return l2
        if l2==None:
            return l1
        q=ListNode(-1)
        p=q
        flag=0
        p1=l1
        p2=l2
        while p1!=None and p2!=None:
            temp=ListNode(p1.val+p2.val+flag)
            if temp.val>=10:
                temp.val=temp.val%10
                flag=1
            else:
                flag=0
            p.next=temp
            p=p.next
            if flag==1 and p1.next==None and p2.next==None:
                t=ListNode(1)
                p.next=t
            p1=p1.next
            p2=p2.next
        while p1!=None:
            p1.val=p1.val+flag
            if p1.val>=10:
                p1.val=p1.val%10
                flag=1
            else:
                flag=0
            p.next=p1
            p=p.next
            if flag==1 and p1.next==None:
                t=ListNode(1)
                p.next=t
                break
            p1=p1.next
        while p2!=None:
            p2.val=p2.val+flag
            if p2.val>=10:
                p2.val=p2.val%10
                flag=1
            else:
                flag=0
            p.next=p2
            p=p.next
            if flag==1 and p2.next==None:
                t=ListNode(1)
                p.next=t
                break
            p2=p2.next
        return q.next

class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        if l1==None:
            return l2
        if l2==None:
            return l1
        q=ListNode(-1)
        p=q
        flag=0
        p1=l1
        p2=l2        
        while p1 or p2 or flag:
            sum=flag
            if p1:
                sum=sum+p1.val
                p1=p1.next
            if p2:
                sum=sum+p2.val
                p2=p2.next
            p.next=ListNode(sum%10)
            p=p.next
            flag=sum/10
        return q.next
        
    
s=Solution1()
p1=ListNode(9)
p2=ListNode(9)
p3=ListNode(9)
q1=ListNode(1)
q2=ListNode(1)
q3=ListNode(1)

p1.next=p2
p2.next=p3
p3.next=None
q1.next=q2
q2.next=q3
q3.next=None

t=s.addTwoNumbers(p1,q1)
print t.val,t.next.val,t.next.next.val,t.next.next.next.val