class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # build the adjacency Matrix
        adjList = {}

        # Intialize the adjMatrix with empty list so that we can append to the list
        for i in range(n):
            adjList[i] = []

        for s1, n1, w1 in edges:
            adjList[s1].append([n1, w1])
        
        shortest = {}
        minHeap = [[0, src]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return(shortest)
