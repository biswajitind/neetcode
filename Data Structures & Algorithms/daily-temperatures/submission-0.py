class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp  in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                temp1, idx = stack.pop()
                result[idx] = i - idx
            else:
                stack.append([temp, i])
        return(result)