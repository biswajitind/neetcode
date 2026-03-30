class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        #  We will need to compute all the consecutive sub arrays. 
        # at the same time keep track of a global max, which we will return.
        longest = 0
        numSet = set(nums)

        for n in nums:
            size = 1
            while n - size in numSet:
                size += 1
            longest = max(longest, size)
        
        return(longest)
            
