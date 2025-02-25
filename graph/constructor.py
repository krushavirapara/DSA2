from collections import defaultdict
adj = defaultdict(list)
def graph(edges):
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj
edges = [[1,2],[1,3],[1,4],[2,5],[2,6],[2,7],[3,8],[6,9],[11,12]]
adj = graph(edges)


#to get total number of vertices 
n = 0
for i in adj:
    n = max(n,i)