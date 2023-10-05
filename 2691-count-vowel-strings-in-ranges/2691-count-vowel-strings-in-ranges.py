class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l=[]
        p={"a":1,"e":1,"o":1,"i":1,"u":1}
        for i in words:
            if i[0] in p and i[-1] in p:
                l.append(1)
            else:
                l.append(0)
        print(l)
        k=[0]*len(l)
        k[0]=l[0]
        m=0
        for i in range(1,len(l)):
            
            k[i]=m+k[i-1]+l[i]
                
        print(k)

        ans=[]
        for i in queries:
            if i[0]==i[1]:
                ans.append(l[i[0]])
            elif i[0]==0:
                ans.append(k[i[1]])
            else:
                ans.append(k[i[1]]-k[i[0]-1])
        

        return ans
        
        