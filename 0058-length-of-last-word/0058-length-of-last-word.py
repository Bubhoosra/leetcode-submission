class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=""
        p=""
        s=s.lower()
        # for i in s:
        #     if i==" ":
        #         s=s.replace(i,"-1")
        #         break
        c=0
        for i in s[::-1]:
            if "a"<= i and i<="z":
                c=1
                p+=i
            else:
                if c==1:
                    return len(p)
        return(len(p))
            
                
        
        
            
        