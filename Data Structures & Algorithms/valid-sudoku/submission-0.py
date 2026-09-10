class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_index = (i //3 ) * 3+ (j // 3)
                    if num in row[i]  or num in column[j] or num in boxes[box_index]:
                        return False

                    row[i].add(num)
                    column[j].add(num)
                    boxes[box_index].add(num)

        return True
print( Solution().isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))

# second approach

cols = [set() for _ in range(9)]
rows = [set() for _ in range(9)]
squares = [set() for _ in range(9)]
for r in range(9):
    for c in range(9):
        if board[r][c] == '.':
            continue
        if (board[r][c] in rows[r] or
            board[r][c] in cols[c] or 
            board[r][c] in squares[(r//3, c//3)]):
            return False
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squares[(r//3, c//3)].add(board[r][c])
return True
