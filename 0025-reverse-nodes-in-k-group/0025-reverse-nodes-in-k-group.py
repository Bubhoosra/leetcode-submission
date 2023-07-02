# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        l=[]
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        n=k
        i=0
        m=[]
        while(i<len(l) and k<=len(l)):
            a=[]
            a=l[i:k]
            a=a[::-1]
            for g in a:
                m.append(g)
            i=k
            k+=n
        i=len(m)
        # print(m)
        while(i<len(l)):
            m.append(l[i])
            i+=1
        temp=root=ListNode(0)
        j=0
        while(j<len(m)):
            temp.next=ListNode(m[j])
            temp=temp.next
            j+=1
        return  root.next

        
            
        