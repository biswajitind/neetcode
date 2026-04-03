class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)        
        low = 0
        high = n - 1

        while (high - low) > 0:
            inc = 0
            for i in range(low, high):
                r1, c1 = low, low + inc
                r2, c2 = low + inc, high
                r3, c3 = high, high - inc
                r4, c4 = high - inc, low
                tmp = matrix[r1][c1]
                matrix[r1][c1] = matrix[r4][c4]
                matrix[r4][c4] = matrix[r3][c3]
                matrix[r3][c3] = matrix[r2][c2]
                matrix[r2][c2] = tmp
                inc += 1
            high -= 1
            low += 1


