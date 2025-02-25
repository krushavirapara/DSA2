import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n, m, edges):
        # Create an adjacency list as a dictionary of lists
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Priority queue for Dijkstra's algorithm
        pq = []
        heapq.heappush(pq, (0, 1))  # (distance, node)
        
        # Distance array initialized with a large value
        dist = [float('inf')] * (n + 1)
        parent = list(range(n + 1))  # Parent array for path reconstruction
        dist[1] = 0
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            for adjNode, edgeWeight in adj[node]:
                if dis + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dis + edgeWeight
                    heapq.heappush(pq, (dist[adjNode], adjNode))
                    parent[adjNode] = node
        
        # If no path exists
        if dist[n] == float('inf'):
            return [-1]
        
        # Reconstruct the path
        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        
        return path[::-1]  # Reverse to get the correct order

# Driver Code
V = 5
E = 6
edges = [
    [1, 2, 2], [2, 5, 5], [2, 3, 4],
    [1, 4, 1], [4, 3, 3], [3, 5, 1]
]

obj = Solution()
path = obj.shortestPath(V, E, edges)
print(path)
