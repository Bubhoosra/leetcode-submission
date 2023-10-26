class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i=0
        j=0
        n=len(arr)
        c=0
        p=0
        res=0
        while(i<n):
            res+=arr[i]
            j+=1
            if j==k:
                ans=res//k
                if ans>=threshold:
                    c+=1
                j-=1
                res-=arr[p]
                p+=1
            i+=1
        return c


        