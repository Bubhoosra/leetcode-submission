class Solution:
    def integerBreak(self, n: int) -> int:
        if n==3:
            return 2
        if n==2:
            return 1
        a=1
        while(n>4):
            a*=3
            n-=3
        return a*n
        