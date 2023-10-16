class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        for i in range(34):
            ans.append([0]*(i+1))
        for i in ans:
            i[0]=1
            i[-1]=1
        for i in range(2,34):
            for j in range(1,len(ans[i])-1):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans[rowIndex]
        