class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res=[]
        l=set(nums1+nums2+nums3)
        res=[]
        p=[]
        for i in nums2:
            if i in nums1 and i not in res:
                res.append(i)
        for i in nums3:
            if i in nums1 and i not in res:
                res.append(i)
        for i in nums2:
            if i in nums3 and i not in res:
                res.append(i)
        # set(res)
        return res
        
        