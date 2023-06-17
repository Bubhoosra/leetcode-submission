class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        l="balloon"
        c=0
        q=0
        r=0
        e=0
        f=0
        res=0
        for i in text:
            if i=="b":
                c+=1
            if i=="a":
                q+=1
            if i=="l":
                r+=1
            # if i=="l":
            #     e+=1
            if i=="o":
                e+=1

            
            if i=="n":
                f+=1
            if c>=1 and q>=1 and r>=2 and e>=2 and f>=1:
                res+=1
                c=c-1
                q=q-1
                r=r-2
                e=e-2
                f=f-1
            
        return(res)
        