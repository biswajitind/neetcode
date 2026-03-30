class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])


        r1, r2 = 0, rows - 1
        while r1 <= r2:
            cRow = (r1 + r2) // 2
            if matrix[cRow][cols - 1] < target :
                r1 = cRow + 1
            elif matrix[cRow][0] > target:
                r2 = cRow - 1
            else:
                # We have found the column
                c1, c2 = 0, cols - 1
                while c1 <= c2:
                    cCol = (c1 + c2) // 2
                    if matrix[cRow][cCol] < target:
                        c1 = cCol + 1
                    elif matrix[cRow][cCol] > target:
                        c2 = cCol - 1
                    else:
                        return(True)
                return(False)
        return(False)
