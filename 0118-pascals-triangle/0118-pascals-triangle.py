class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # n=len(str(11**(numRows-1)))
        # print(11**numRows)
        # print(n)
        p=[]
        # print(p)

        for i in range(numRows):
            l=[]
            for i in range(numRows):
                l.append(0)
            p.append(l)
            # print(p)
        # p[0][0]=1
        # print(p)
        for i in range(numRows):
            for j in range(numRows):
                if j==0:
                    p[i][j]=1
                
                else:
                    p[i][j]=p[i-1][j]+p[i-1][j-1]
        l=[]
        for i in p:
            q=[]
            for j in i:
                if j==0:
                    break
                else:
                    q.append(j)
            l.append(q)
            # print(p)
        return l
               
            
    
            
                    
            

        
                    
                        
        # print(p)





        # p=[]
        # for i in range(0,numRows):
        #     k=str(11**i)
        #     l=[]
        #     for j in k:
        #         l.append(int(j))
        #     p.append(l)
        # return p

        