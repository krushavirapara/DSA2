def bipartite_graph(adj):
	#odd length cycel is alwaye not a bipartite graph

	#any child which has same colour as parent will result in bipartite graph

	def dfs(i,c):
		colour[i] = c

		for child in adj[i]:
			if colour[child]==-1:
				if not dfs(child,not c):
					return False
			elif colour[child] == c:
				return False
		return True

	colour = [-1]*n

	for i in range(n):
		if colour[i]==-1:
			if not dfs(i,0):
				return False
	return True
