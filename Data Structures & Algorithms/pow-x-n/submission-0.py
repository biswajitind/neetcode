class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}
        dp[0] = 1
        dp[1] = x

        negN = (n < 0)

        n = abs(n)
        negX = (x < 0 and n % 2)

        def _pow(n):
            if n in dp:
                return(dp[n])
            n1 = n // 2
            dp[n] = _pow(n1) * _pow(n - n1)
            return(dp[n])

        res = _pow(n)
        if negN:
            res = 1 / res
        if negX:
            res  = -1 * res

        return(res) 
        
