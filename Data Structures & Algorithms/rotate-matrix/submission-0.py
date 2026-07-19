class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        arr = []

        for col in range(0, len(matrix)):
            for row in range(len(matrix) - 1, -1, -1):
                arr.append(matrix[row][col])
        
        count = 0
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix)):
                matrix[row][col] = arr[count]
                count += 1