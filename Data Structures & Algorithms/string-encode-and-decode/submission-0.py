class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f'{len(s)}#{s}'
        return(result)

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        while idx < len(s):
            numStr = ""
            while s[idx].isdigit():
                numStr += s[idx]
                idx += 1
            if s[idx] != "#":
                print(f"Error in Transit, or encoding at {idx}\n ",s)
                return(-1)
            else:
                idx += 1
            
            # capture the word
            word = ""
            for i in range(int(numStr)):
                word += s[idx]
                idx += 1
            result.append(word)
        return(result)



                


                
