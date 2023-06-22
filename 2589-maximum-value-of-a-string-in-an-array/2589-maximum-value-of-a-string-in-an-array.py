class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res=0
        c=0
        l=[]
        q=0
        for i in range(len(strs)):
            c=0
            # print(strs[i])
            for j in strs[i]:
                # print(j)
                if j in "1234567890":
                    c+=1
                else:
                    l.append(len(strs[i]))
                    break

            if c==len(strs[i]):
                l.append(int(strs[i]))
        return max(l)
        
        # for i in l:
        #     if int(i)>res:
        #         res=int(i)

            
        # return res