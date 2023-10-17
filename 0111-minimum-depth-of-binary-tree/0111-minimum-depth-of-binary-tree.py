# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q=deque()
        q.append(root)
        c=0
        while(len(q)>0):
            size=len(q)
            c+=1
            
            while(size>0):
                
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if node.left==None and node.right==None:
                    return c
                size-=1
            
        
                



        