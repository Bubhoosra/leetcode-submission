# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=deque()
        q.append(root)
        i=0
        p=x
        z=y
        counter=0
        promise=0
        promise1=0
        while(len(q)>0):
            size=len(q)
            l=[]
            

            

            x=p
            y=z
            counter=0
            
            while(size>0):
                node=q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                    if x==node.left.val:
                        x=-1
                    elif y==node.left.val:
                        y=-1
                if node.right:
                    q.append(node.right)
                    if x==node.right.val:
                        x=-1
                    elif y==node.right.val:
                        y=-1
                
                if x==-1 and y==-1 and counter==0:
                    print("2")
                    return False
                
                if counter==1 and (x==-1 and y==-1):
                    return True
                if x==-1 and y!=-1:
                    counter=1
                if x!=-1 and y==-1:
                    counter=1
                
                
                    

                size-=1
            if p in l and promise1==1:
                return False
            if z in l and promise==1:
                return False
            if p in l:
                promise=1
            if z in l:
                promise1=1

            i+=1
        return True
            
        


        