# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=head
        l=[]
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        p=[]
        for i in range(len(l)):
            if i>=left-1 and i<right:
                p.append(l[i])
        p=p[::-1]
        print(p)
        c=0
        for i in range(len(l)):
            if i>=left-1 and i<right:
                l[i]=p[c]
                c+=1
        temp=head=ListNode(0)
        n=len(l)
        i=0
        while(n!=i):
            temp.next=ListNode(l[i])
            temp=temp.next
            i+=1
        return head.next
            

        