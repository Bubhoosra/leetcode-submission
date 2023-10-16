# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if root!=None:

            q.append(root)
        ans=[]
        
        while(len(q)>0):
            size=len(q)
            l=[]
            while(size>0):
                
                node=q.popleft()
                
                l.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size-=1
            print(l)
            ans.append(l)
        ans[:]=ans[::-1]
        return ans
        