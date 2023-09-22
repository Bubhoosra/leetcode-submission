class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        size=len(nums)
        k=1
        for i in range(size-1):
            if nums[i]<=nums[i+1]:
                k+=1
        if k==size:
            return 0
        for i in range(size):
            nums.append(nums[i])
        n=len(nums)
        c=1
        for i in range(n-1):
            if nums[i]<=nums[i+1]:
                c+=1
                print(c)
            else:
                c=1
            if c==size:
                return (n-i-2)%n
        
                
        return -1


        
        
                

        