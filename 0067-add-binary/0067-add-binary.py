class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=0
        j=0
        for i in range(len(a)-1,-1,-1):


            p=int(a[i])*(2**j)
            
            res+=p
            j+=1
        j=0
       
        for i in range(len(b)-1,-1,-1):
            res+=int(b[i])*(2**j)
            j+=1
        
        ans=str(bin(res))
        ans=ans.replace("0b","")
        return ans
        