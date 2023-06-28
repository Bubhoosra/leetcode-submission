class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        p=[]
    
        c=0
        l=[]
        for i in range(len(A)):
            l=A[:i+1]+B[:i+1]
            k=len(l)-len(set(l))
            p.append(k)
            
        
        return p
