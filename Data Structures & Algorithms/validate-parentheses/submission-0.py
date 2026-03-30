class Solution:
    def isValid(self, s: str) -> bool:
        pMatch = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for i in range(len(s)):
            print(stack)
            if stack:
                if s[i] in pMatch and pMatch[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                if s[i] in (')', '}', ']'):
                    return(False)
                else:
                    stack.append(s[i])
        if len(stack):
            return(False)

        return(True)
        