class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr=sorted(arr)
        l=[]
        if len(arr)>1:
            m=max(arr)
            for i in range(len(arr)-1):
                res=arr[i+1]-arr[i]
                if res<m:
                    m=res
            for i in range(len(arr)-1):
                if m==arr[i+1]-arr[i]:
                    l.append([arr[i],arr[i+1]])
            return l