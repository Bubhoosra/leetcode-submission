class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while(nums[0]!=nums[nums[0]]):
            temp=nums[nums[0]]
            nums[nums[0]]=nums[0]
            nums[0]=temp
        return nums[0]
        
        