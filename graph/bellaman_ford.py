class Solution:
    def bellman_ford(self, V, edges, S):
        dist = [float('inf')] * V
        dist[S] = 0
        
        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        # Nth relaxation to check for negative weight cycles
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist

if __name__ == "__main__":
    V = 6
    edges = [
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3]
    ]
    
    S = 0
    obj = Solution()
    dist = obj.bellman_ford(V, edges, S)
    print(" ".join(map(str, dist)))
