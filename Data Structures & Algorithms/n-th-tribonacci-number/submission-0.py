class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n <= 1:
            return n
        if n <= 3:
            return n - 1
        
        a, b, c = 0, 1, 1

        for x in range(3, n):
            temp = a + b + c
            a, b = b, c
            c = temp

        return a + b + c
        

            