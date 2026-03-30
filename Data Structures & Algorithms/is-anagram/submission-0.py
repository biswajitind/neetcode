class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return(False)
        cHash = {}
        for i in range(len(s)):
            cHash[s[i]] = cHash.get(s[i], 0 ) + 1
            cHash[t[i]] = cHash.get(t[i], 0 ) - 1

        for k in cHash.keys():
            if cHash[k] != 0:
                return(False)
        return(True)
