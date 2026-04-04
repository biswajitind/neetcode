class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        count = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, 0
        rInc, cInc = 0, 1
        top, left, bottom, right = 0, 0, ROWS - 1, COLS - 1


        for i in range(ROWS):
            for j in range(COLS):
                print(matrix[i][j],"  ", end="")
            print("")


        while count < (ROWS * COLS):

            output.append(matrix[r][c])
            count += 1

            if cInc == 1 and c == right:
                rInc, cInc = 1, 0
                top += 1
            elif rInc == 1 and r == bottom:
                rInc, cInc = 0, -1
                right -= 1
            elif cInc == -1 and c == left:
                rInc, cInc = -1, 0
                bottom -= 1
            elif rInc == -1 and r == top:
                rInc, cInc = 0, 1
                left += 1

            r, c =  r + rInc, c + cInc
        
        return(output)


