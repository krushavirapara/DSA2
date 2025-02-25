#0-1 bfs 
#if the dege is 0 then append in front else append in last
def min_edge_reversal(vertex,edges,s,e):
	dist = [float("inf") for i in range(vertex)]
	dist[s] = 0

	def build_graph(edges):
		from collections import defaultdict
		adj = defaultdict(list)


		for  u,v in edges:
			adj[u].append((v,0))
			adj[v].append((u,1))

		return adj

	adj = build_graph(edges)
	queue = []
	queue.append(s) #node

	while queue:
		node = queue.pop(0)
		if node==e:
			break

		for child,wt in adj[node]:
			if dist[node] +  wt < dist[child]:
				dist[child] = dist[node]+  wt
				if wt == 0 :
					queue.insert(0,child)
				else:
					queue.append(child)

	return dist[e] if dist[e]!= float("inf") else -1



V = 7
edge = [[0, 1], [2, 1], [2, 3], [5, 1],[4, 5], [6, 4], [6, 3]]
print(min_edge_reversal(V,edge,0,1))
