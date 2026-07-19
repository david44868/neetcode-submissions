class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost[0], cost[1])
        else:
            arr = [0] * (len(cost) + 1)
            arr[0], arr[1] = cost[0], cost[1]

            for x in range(2, len(cost)):
                arr[x] = min(arr[x - 1] + cost[x], arr[x - 2] + cost[x])
            
            return min(arr[len(cost) - 1], arr[len(cost) - 2])