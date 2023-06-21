class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        left=-1
        right=-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                left=mid
                j=mid-1
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        i=0
        j=n-1

        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                right=mid
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        if left==-1:
            return []
        ans=range(left,right+1)
        return ans
                
        