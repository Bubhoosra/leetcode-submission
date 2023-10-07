class Solution:
    def pivotInteger(self, n: int) -> int:
        res=(n*(n+1))//2
        s=0
        for i in range(1,n+1):
            s+=i
            if s==res:
                return i
            res-=i
        return -1
            
        