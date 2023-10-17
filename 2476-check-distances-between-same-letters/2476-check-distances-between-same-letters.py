class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                d[s[i]]=i-d[s[i]]-1
        print(d)
        for i in s:
            res=ord(i)%97
            print(res,d[i])
            if distance[res]!=d[i]:
                return False
        return True

        