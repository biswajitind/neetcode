class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        blocks = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if r in rows:
                    if board[r][c] in rows[r]:
                        return(False)
                else:
                    rows[r] = set()

                if c in cols:
                    if board[r][c] in cols[c]:
                        return(False)
                else:
                    cols[c] = set()

                bTuple = (r // 3, c // 3)
                if bTuple in blocks:
                    if board[r][c] in blocks[bTuple]:
                        return(False)
                else:
                    blocks[bTuple] = set()

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[bTuple].add(board[r][c])

        return(True)