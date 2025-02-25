def shortest_bridge(grid):
	drow = [1,0,-1,0]
	dcol = [0,1,0,-1]

	n = len(grid) #rows
	m = len(grid[0]) #cols

	def is_valid(r,c):
		return r>=0 and r<n and c>=0 and c<m

	visited = [[0]*m for i in range(n)]

	def bfs(r,c):
		queue = [(r,c)]
		res = []

		while queue:

			r,c = queue.pop(0)
			visited[r][c] = 1
			res.append((r,c))

			for i in range(4):
				nrow = r + drow[i]
				ncol = c + dcol[i]

				if is_valid(nrow,ncol) and not visited[nrow][ncol] and grid[nrow][ncol]==1:
					queue.append((nrow,ncol))
		return res

	is_found = False
	queue = []
	for i in range(n):
		for j in range(m):
			if grid[i][j]==1:
				queue = bfs(i,j)
				is_found = True
				break
		if is_found:
			break
#here the concept of marking while enqueing in the queue and marking while poping plays an important role in tle.
#look for that 
#its good practice to visit while enqueing in the queue it will not allow duplicate nodes in the queue.

	def bfs(queue):
		level = 0
		while queue:
			for _ in range(len(queue)):
				r,c = queue.pop(0)
				if not visited[r][c] and grid[r][c]==1:
					return level-1

				visited[r][c] = 1
				


				for i in range(4):
					nrow = r + drow[i]
					ncol = c + dcol[i]

					if is_valid(nrow,ncol) and not visited[nrow][ncol]:
						# if grid[nrow][ncol]:
						# 	return level
						queue.append((nrow,ncol))
			level+=1
			print(level,visited)
		return level

	return bfs(queue)

grid = [[0,1,0],[0,0,0],[0,0,1]]
print(shortest_bridge(grid))





