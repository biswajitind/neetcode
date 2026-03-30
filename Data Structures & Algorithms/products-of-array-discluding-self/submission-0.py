class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # count zeros
        # if there are two zeros, all entries will be zero
        # if there is a single zero, except that one rest everything will be zero

        # lets compute the product ( excluding the zero, and also count number of zeros)            
        zCount = 0
        product = 1
        zIdx = -1
        output = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                zCount += 1
                zIdx = i
            else:
                product *= nums[i]
            
            if zCount > 1:
                return(output)

        if zCount == 1:
            output[zIdx] = product
            return(output)

        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = product
            else:
                output[i] = product // nums[i]

        return(output)
            





