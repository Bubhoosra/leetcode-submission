class Solution:
    def similarPairs(self, words: List[str]) -> int:
        l=[]
        for i in words:
            l.append("".join(list(set(i))))
        c=0
        for i in range(len(l)-1):
            for j in range(i+1,len(l)):
                x=l[i]
                y=l[j]
                x=sorted(x)
                y=sorted(y)
                if x==y:
                    c+=1
        return c
        