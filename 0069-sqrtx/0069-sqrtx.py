import math
class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        j=x
        l=[]
        while(i<=j):
            mid=i +(j-i)//2
            if mid*mid==x:
                return mid
            if mid*mid>x:
                j=mid-1
            elif mid*mid<x:
                ans=mid
                i=mid+1
        return ans
            
        
        