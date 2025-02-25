from constructor import adj,n


#time complexity = O(V+E)
#s.c = o(V)
def bfs(vertex,par):
	queue = []
	queue.append((vertex,-1))
	is_loop = False
	visited = [0]*(n+1)
	level  = [0]*(n+1)
	level[vertex] = 1

	while queue:
		node,par  = queue.pop(0)
		print(node,end = " ")
		visited[node] = True


		for child in adj[node]:
			if not visited[child]:
				level[child] = level[node]+1
				queue.append((child,node))
			if visited[child] and child==par:
				continue
			elif visited[child] and child!=par:
				is_loop = True
				break
	print()
	print(level)
	return is_loop


print(bfs(1,0)) 

#it is used to find shortest path from single source having unit weight and directed or undirected or cyclic
#directed/undirected cyclc/acyclic and unit weighted