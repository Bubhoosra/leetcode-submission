class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        j=0
        d={}
        for i in mat:
            l=i.count(1)
            d[j]=l
            j+=1
        a=[]
        p= sorted(d.items(), key=lambda x:x[1], reverse=False)
        o=dict(p)
        for i in o:
            a.append(i)
        return a[:k]
