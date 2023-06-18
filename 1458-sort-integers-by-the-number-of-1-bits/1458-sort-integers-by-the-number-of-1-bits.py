class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d={}
        res=[]
        for i in arr:
            s=bin(i).replace("0b","")
            
            res.append([s.count("1"),i])
        res=sorted(res)
        l=[]

        for i in res:
            l.append(i[1])
        # print(l)
        # p=(list(dict(l).keys()))

        return l
        