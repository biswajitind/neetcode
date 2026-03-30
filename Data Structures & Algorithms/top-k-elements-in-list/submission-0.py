class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        maxHeap = []
        for val, count in c.items():
            heapq.heappush(maxHeap, (-1 * count, val))

        result = []
        for i in range(k):
            result.append(heapq.heappop(maxHeap)[1])

        return(result)

