class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=[]
        l[:]=score
        ans=[]
        l.sort(reverse=True)
        print(score)
        for i in score:
            
            if i==l[0]:
                ans.append("Gold Medal")
            elif i==l[1]:
                ans.append("Silver Medal")
            elif i==l[2]:
                ans.append("Bronze Medal")
            else:
                
                ans.append(str(int(l.index(i)+1)))
        return ans
        