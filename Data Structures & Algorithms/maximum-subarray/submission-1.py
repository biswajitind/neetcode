class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cSum = 0

        for n in nums:

            if cSum < 0:
                cSum = 0 

            cSum += n
            maxSum = max(maxSum, cSum)
        return(maxSum)