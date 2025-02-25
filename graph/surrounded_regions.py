def surrounded_regions(grid):

	drow = [1,0,-1,0]
	dcol = [0,1,0,-1]

	n = len(grid) #rows
	m = len(grid[0]) #cols

	def is_valid(r,c):
		return r>=0 and r<n and c>=0 and c<m

	queue = []
	visited = [[0]*m for i in range(n)]

	for i in range(n):
		#for 1st and last column

		if grid[i][0]=="O":
			queue.append((i,0))

		if grid[i][m-1] =="O":
			queue.append((i,m-1))


	for i in range(m):
		#for 1st and last row

		if grid[0][i]=="O":
			queue.append((0,i))
		if grid[n-1][i] == "O":
			queue.append((n-1,i))

	
	#start bfs traversal and mark all connedted cells to the border cells
	while queue:

		r,c = queue.pop(0)
		visited[r][c] = 1

		for i in range(4):
			nrow = r + drow[i]
			ncol = c + dcol[i]

			if is_valid(nrow,ncol) and not visited[nrow][ncol] and grid[nrow][ncol]=="O":
				queue.append((nrow,ncol))
	

	for i in range(n):
		for j in range(m):
			if not visited[i][j] and grid[i][j]=="O":
				grid[i][j] = "X"

	return grid

grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

print(surrounded_regions(grid))