class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
    
        clcost = [0] * len(cost)
        clcost[0] = 0
        clcost[1] = 0
        for i in range(2, len(cost)):
            clcost[i] = min(clcost[i-2] + cost[i-2], clcost[i-1] + cost[i-1])


        return min(clcost[-1] + cost[-1], clcost[-2] + cost[-2])