class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        correct = n * (n + 1) / 2
        incorrect = 0
        for n in nums:
            incorrect += n
        return(abs(int(correct - incorrect)))
