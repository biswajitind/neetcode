class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def alphaNum(c):
            return(
                ord("a") <= ord(c) <= ord("z") or 
                ord("A") <= ord(c) <= ord("Z") or
                ord("0") <= ord(c) <= ord("9") 
            )

        cleanS = ""
        for i in range(len(s)):
            if alphaNum(s[i]):
                cleanS += s[i].lower()

        l, r = 0, len(cleanS) - 1 
        while l <= r:
            if cleanS[l] != cleanS[r]:
                return(False)
            l += 1
            r -= 1
            
        return(True)
        