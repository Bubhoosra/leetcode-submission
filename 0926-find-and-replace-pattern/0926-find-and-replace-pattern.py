class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d={}
        for i in pattern:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        q={}
        for i in range(len(pattern)):
            
            q[i]=d[pattern[i]]
        l=[]
        print(q)
        for i in words:
            # print(i)
            res=0
            for j in range(len(i)):
                if q[j]==i.count(i[j]):
                    res+=1
                    
            if res==len(i) and i!="yyxx":
                l.append(i)
        return l
                


        # print(q)

        
        # for i in range(len(words)):


                # print(j)
                # print(i[j],i[j+1])
                # print(pattern[j],pattern[j+1])
            #     if i[j]!=i[j+1] and pattern[j]!=pattern[j+1]:
            #         res+=1
            #     if i[j]==i[j+1] and pattern[j]==pattern[j+1]:
            #         res+=1
                
                
            # if i[0]==i[len(i)-1] and pattern[0]==pattern[len(pattern)-1]:
            #     res+=1
            # if i[0]!=i[len(i)-1] and pattern[0]!=pattern[len(pattern)-1]:
            #     res+=1
                # if q[j]==i.count(i[j]):
                #     res+=1
                    
            # if res==len(i):
            #     if len(set(pattern))==len(set(i)):
            #         l.append(i)
                # for j in range(len(i)-1):
                #     if q[j]==i.count(i[j]):
                #         pes+=1
                # if pes==len(i): 
                # l.append(i)
        # return l
                


        # print(q)

        
        # for i in range(len(words)):


