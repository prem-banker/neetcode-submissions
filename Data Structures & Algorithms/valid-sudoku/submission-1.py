class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            repeat = {}
            for col in row:
                if col in repeat and col != '.':
                    return False
                repeat[col] = True

        for i in range(9):
            repeat = {}
            for j in range(9):
                if board[j][i] in repeat and board[j][i] != '.':
                    return False
                repeat[board[j][i]] = True

        for i in range(0, 7, 3):
            for j in range(0,7,3):
                subboard = []
                for x in range(i, i+3):
                    row = []
                    for y in range(j, j+3):
                        row.append(board[x][y])
                    subboard.append(row)
                print(subboard)
                repeat = {}
                for row in subboard:
                    for col in row:
                        if col in repeat and col != '.':
                            return False
                        repeat[col] = True
        return True
