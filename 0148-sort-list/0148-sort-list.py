# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        l=sorted(l)
        temp=head1=ListNode(0)
        i=0
        n=len(l)
        while(i<n):
            temp.next=ListNode(l[i])
            temp=temp.next
            i+=1
        return head1.next
        