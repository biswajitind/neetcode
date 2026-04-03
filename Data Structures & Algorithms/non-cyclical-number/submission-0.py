class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            # Compute digit squar sum.
            nextNumber = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                nextNumber += digit
                n = n // 10
            if nextNumber == 1:
                return(True)
            n = nextNumber

        return(False)
        