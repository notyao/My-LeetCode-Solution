class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            seen = {}
            for num in row:
                if num in seen:
                    return False
                elif num == ".":
                    continue
                else:
                    seen[num] = 1

        for col in range(9):
            seen = {}
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                else:
                    seen[board[row][col]] = 1

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                seen = {}
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] == ".":
                            continue
                        elif board[row + i][col + j] in seen:
                            return False
                        else:
                            seen[board[row + i][col + j]] = 1
        return True
