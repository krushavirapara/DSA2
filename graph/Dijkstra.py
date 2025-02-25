
class Solution():

	#this will work for directed undirected cyclic acylic graph with only positive edge weight
	def __init__(self,n,edges,src):
		from collections import defaultdict
		

		self.adj = defaultdict(list)
		self.indegree = [0]*(n+1)

		

		for s,dest,weight in edges:
			self.adj[s].append((dest,weight))
			self.indegree[dest]+=1



	def shortest_path(self,n,edges,src):

		from collections import defaultdict
		import heapq 

		adj = defaultdict(list)

		dist = [float("inf") for i in range(n+1)]

		for s,dest,weight in edges:
			adj[s].append((dest,weight))

		dist[src] = 0
		min_heap = []
		heapq.heappush(min_heap,(0,src))

		while min_heap:
			di,node = heapq.heappop(min_heap)

			for child,wt in adj[node]:
				if dist[node] + wt < dist[child]:
					dist[child] = dist[node]+ wt
					heapq.heappush(min_heap,(dist[child],child))

		return dist

	#dag with or without negative weight
	def topo_shortest(self,n,src):
		queue = []
		for i in range(1,n+1):
			if self.indegree[i]==0:
				queue.append(i)

		topo = []
		dist = [float("inf") for i in range(n+1)]

		while queue:
			node = queue.pop(0)
			topo.append(node)

			for child,_ in self.adj[node]:
				self.indegree[child]-=1
				if self.indegree[child]==0:
					queue.append(child)
		print("TOPOLOGICAL ORDER:",topo)
		dist[src] = 0
		while topo:
			node = topo.pop(0)

			for child,wt in self.adj[node]:
				if dist[node]+wt<dist[child]:
					dist[child] = dist[node]+wt

		return dist




n = 5
edges= [[1,2,7],[1,3,12],[3,2,-6],[2,4,1],[2,5,1]]
src =1
c= Solution(n,edges,src)
print(c.shortest_path(n,edges,src))
print("**************************")
print(c.topo_shortest(n,src))

