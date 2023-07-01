class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
               d[i]=1
            else:
                d[i]+=1
        l=sorted(list(d.values()),reverse=True)
        
        # l=sorted(l)
        print(l)
        


        n=len(arr)
        n1=len(arr)
        s=0
        for i in l:
            n-=i
            if n<=(n1//2):
                s+=1
                break
            else:
                s+=1
                
        
               
        return s
        

            

