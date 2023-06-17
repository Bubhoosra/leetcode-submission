class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        q=0
        res=0
        for i in s:
            if i=="R":
                c+=1
            if i=="L":
                q+=1
            if c==q:
                c=0
                q=0
                res+=1
        return res
