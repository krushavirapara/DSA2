def pacific_atlantic(grid):
	pac = []
	atl = []

	drow = [1,0,-1,0]
	dcol = [0,1,0,-1]

	n = len(grid)
	m = len(grid[0])


	def is_valid(r,c):
		return r>=0 and r<n and c>=0 and c<m
	

	for i in range(m):

		#1st and last row
		pac.append((0,i))
		atl.append((n-1,i))

	for i in range(n):

		#1st and last column
		pac.append((i,0))
		atl.append((i,m-1))

	def bfs(que):
		visited = [[0]*m for i in range(n)]

		while que:
			r,c = que.pop(0)
			visited[r][c] = 1

			for i in range(4):
				nrow  = r + drow[i]
				ncol = c +dcol[i]

				if is_valid(nrow,ncol) and not visited[nrow][ncol] and grid[nrow][ncol]>=grid[r][c]:
					que.append((nrow,ncol))
		return visited

	pac = bfs(pac)
	atl = bfs(atl)
	ans =[]
	for i in range(n):
		for j in range(m):
			if pac[i][j] and atl[i][j]:
				ans.append((i,j))

	return ans



#left and top are pacific ocean 
#right and bottom are atlantic ocean


grid = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(pacific_atlantic(grid))

