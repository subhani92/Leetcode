class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        F =[0]*(len(cost))
        F[0] = cost[0]
        F[1] = cost[1]
        for i in range(2, len(cost)):
            F[i] =cost[i] + min(F[i-1], F[i-2])
        
        # print(F)
        return min(F[-1], F[-2])