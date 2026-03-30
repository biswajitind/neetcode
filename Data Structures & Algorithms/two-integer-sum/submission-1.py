class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Since we are given
        # 2 <= nums.length <= 1000
        # we can simply initialize with the first element in the list
        visited = {}
        visited[nums[0]] = 0

        for i in range(1, len(nums)):
            delta = target - nums[i]
            if delta in visited:
                return([visited[delta], i])
            visited[nums[i]] = i

