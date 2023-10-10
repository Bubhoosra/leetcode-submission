class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p=""
        ans=""
        
        c=0
        i=0
        j=0
        while(i<len(s)):
            j+=1
            p+=s[i]
            if j==2*k:
                w=p[:k]
                w=w[::-1]
                ans+=w+p[k:]
                p=""
                j=0
            i+=1
        if p!="":
            w=p[:k]
            w=w[::-1]
            ans+=w+p[k:]
        return ans

            


