class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        for i in range(0,15+1):
            p=4**i
            if p==n:
                return True
        return False