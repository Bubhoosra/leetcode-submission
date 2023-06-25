class Solution:
    def customSortString(self, order: str, s: str) -> str:
        l=[]
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in order:
            if i  in d:
                while(d[i]):
                    l.append(i)
                    d[i]-=1
        for i in s:
            if d[i]>=1:
                while(d[i]):
                    l.append(i)
                    d[i]-=1
        return "".join(l)

