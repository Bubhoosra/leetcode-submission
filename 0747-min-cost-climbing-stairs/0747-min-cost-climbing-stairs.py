class Solution:
    def solve(self,cost,n,dp):
        if n==1:
            return cost[1]
        if n==0:
            return cost[0]
        if dp[n]!=-1:
            return dp[n]
        dp[n]=cost[n]+min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))
        return dp[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i=0
        n=len(cost)
        dp=[-1]*(n+1)
        ans=min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))
        return ans
        