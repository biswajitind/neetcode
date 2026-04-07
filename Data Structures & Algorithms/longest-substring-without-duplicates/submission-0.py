class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SIZE = len(s)
        chrSet = set()
        maxLen = 0
        l = 0

        for r in range(SIZE):

            while s[r] in chrSet:
                chrSet.remove(s[l])
                l += 1

            chrSet.add(s[r])
            
            maxLen = max(maxLen, r - l + 1)
        
        return(maxLen)