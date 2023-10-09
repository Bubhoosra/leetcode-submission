class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
        s=0

        for i in range(len(grid[0])):
            x=0
            for j in range(len(grid)):
                x=max(grid[j][i],x)
            s+=x
        return s


        