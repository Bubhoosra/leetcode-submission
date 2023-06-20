class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        n=len(word1)
        res=list(set(word1+word2))
        
        for i in range(len(res)):
            k=abs(word1.count(res[i]) - word2.count(res[i]))
            if k>3:
                return False
        return True
        
