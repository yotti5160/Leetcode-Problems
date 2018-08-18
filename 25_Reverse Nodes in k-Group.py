# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(node):
            Newtail=node
            count=0
            priv=None
            while count<k:
                tmp=node.next
                node.next=priv
                priv, node=node, tmp
                count+=1
            return (priv,Newtail) #return (new head, new tail) 
            
        dummy=ListNode(0)
        dummy.next=head
        n=1
        back, new=dummy, None
        while head:
            head=head.next
            n+=1
            if n==k and head:
                new=head.next #possible None
                (t1,t2)=reverse(back.next)
                back.next=t1
                t2.next=new
                back=t2
                new=head
                head=t2.next
                n=1
        return dummy.next
