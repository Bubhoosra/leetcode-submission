class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        for i in nums:
            if i<pivot:
                left.append(i)
        mid=[]
        for i in nums:
            if i==pivot:
                mid.append(i)
        for i in nums:
            if i>pivot:
                right.append(i)
        ans=left+mid+ right
        return ans
        