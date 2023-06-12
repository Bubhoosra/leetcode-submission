class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        f=[]
        f=nums1+nums2
        f.sort()
        print (f)
        n=len(f)
        if(n%2!=0):
            for i in range(len(f)):
                if(i+1==(n+1)//2):
                    return(float(f[i]))
        elif(n%2==0):
            for i in range(len(f)):
                if(i+1==n//2):
                    s=(f[i]+ f[i+1])
                    return (s/2)
        
        
        
        