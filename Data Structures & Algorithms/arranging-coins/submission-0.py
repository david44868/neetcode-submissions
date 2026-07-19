class Solution:
    def arrangeCoins(self, n: int) -> int:

        if n == 1:
            return 1
        
        total = 0
        complete = 1
        while total < n:
            total += complete
            complete += 1
        
        return complete - 2