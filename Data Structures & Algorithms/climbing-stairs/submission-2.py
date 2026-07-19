class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        else:
            arr = [0] * n
            arr[0] = 1
            arr[1] = 2
            for x in range(2, n):
                arr[x] = arr[x - 1] + arr[x - 2]
            return arr[n - 1]


        