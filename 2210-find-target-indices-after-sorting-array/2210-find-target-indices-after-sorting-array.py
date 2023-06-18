class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        l=-1
        i=0
        n=len(nums)
        j=len(nums)-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                l=mid
                j=mid-1
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        i=l
        j=n-1
        r=-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                r=mid
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        if  l==-1:
            return []
        ans=range(l,r+1)
        return ans
            

            
        return l