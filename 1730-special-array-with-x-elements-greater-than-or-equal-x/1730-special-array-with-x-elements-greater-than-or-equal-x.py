class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        q=0
        c=0
        while(i<=n):
            c=0
            for j in nums:
                if j>=i:
                    c+=1
            if c==i:
                q=1
                return c
            
            i+=1
        if q==0:
            return -1