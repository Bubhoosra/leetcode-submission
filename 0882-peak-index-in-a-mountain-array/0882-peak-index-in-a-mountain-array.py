class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        i=0
        j=n-1
        while(i<j):
            mid=(i+j)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            if arr[mid]>arr[mid+1]:
                j=mid
            else:
                i=mid+1

        