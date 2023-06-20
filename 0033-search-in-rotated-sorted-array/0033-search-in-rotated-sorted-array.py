class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        n=len(nums)-1
        j=n
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            if nums[i]<=nums[mid]:
                if target>nums[mid] or target<nums[i]:
                    i=mid+1
                else:
                    j=mid-1
            else:
                if target<nums[mid] or target>nums[j]:
                    j=mid-1 
                else:
                    i=mid+1
        return -1
        
        
       