class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        l=[]
        m=len(grid)
        n=len(grid[0])
        res=[]
        for i in range(n):
            for j in range(m):
                res.append(grid[j][i])
                # print(res)
            l.append(res)
            res=[]
        # print(l)
        c=0
        for i in range(len(grid)):
            for j in range(len(l)):
                if grid[i]==l[j]:
                    c+=1
        return c