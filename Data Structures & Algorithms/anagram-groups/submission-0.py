class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resHash = {}
        res = []
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ ord(s[i]) - ord("a") ] += 1
            k = tuple(count)
            if k in resHash:
                resHash[k].append(s)
            else:
                resHash[k] = [s]
        for k in resHash.keys():
            res.append(resHash[k])
        #print(resHash)
        #print(type(res))
        return(res)