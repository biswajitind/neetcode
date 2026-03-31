class Solution:
    def climbStairs(self, n: int) -> int:
        # # Bottom up 
        # one = 1
        # two = 1
        # for i in range( n - 1):
        #     one, two = one + two, one
        # return(one)

        # Top down
        dp = {}
        def dfs(step):
            if step > n:
                return(0)
            if step in dp:
                return(dp[step])

            if step == n:
                return(1) 
            count = 0
            if not step + 1 > n:
                count += dfs(step + 1)
            
            if not step + 2 > n:
                count += dfs(step + 2)

            dp[step] = count
            return(count)

        return(dfs(0))
