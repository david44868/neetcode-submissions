class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check if valid square
        for col in range(0, len(board), 3):
            for row in range(0, len(board), 3):
                arr = 10 * [0]
                for row2 in range(row, row + 3):
                    for col2 in range(col, col + 3):
                        if board[row2][col2] != ".":
                            arr[int(board[row2][col2])] += 1
                            if arr[int(board[row2][col2])] > 1:
                                return False

        # Check if valid row
        for row in board:
            arr = 10 * [0]
            for number in row:
                if number != ".":
                    arr[int(number)] += 1
                    if arr[int(number)] > 1:
                        return False
        
        # Check if valid col
        for col in range(0, len(board)):
            arr = 10 * [0]
            for row in range(0, len(board)):
                if board[row][col] != ".":
                    arr[int(board[row][col])] += 1
                    if arr[int(board[row][col])] > 1:
                        return False

        return True