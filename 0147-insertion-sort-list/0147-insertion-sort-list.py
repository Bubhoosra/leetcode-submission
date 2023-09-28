# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def findmid(head):
    slow=head
    fast=head
    while(fast.next!= None and fast.next.next != None):
        slow=slow.next
        fast=fast.next.next
    return slow
def merge(head):
    if head.next ==None:
        return head
    mid=findmid(head)
    afterMid=mid.next
    mid.next=None
    head1=merge(head)
    head2=merge(afterMid)
    finalHead=mergeSort(head1,head2)
    return finalHead
def mergeSort(head1,head2):
    final=ListNode(0)
    temp=final
    while(head1!=None and head2!=None):
        if(head1.val<=head2.val):
            temp.next=ListNode(head1.val)
            head1=head1.next
        else:
            temp.next=ListNode(head2.val)
            head2=head2.next
        temp=temp.next
    while(head1!=None):
        temp.next=ListNode(head1.val)
        temp=temp.next
        head1=head1.next
    while(head2!=None):
        temp.next=ListNode(head2.val)
        temp=temp.next
        head2=head2.next
    return final.next
        


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge(head)
        