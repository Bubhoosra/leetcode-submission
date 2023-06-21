class Solution:
    def digitCount(self, nums: str) -> bool:
        for i in range(len(nums)):
            # print(i,nums.count(str(i)),nums[i])
            if nums.count(str(i))!=int(nums[i]):
                return False
        return True
