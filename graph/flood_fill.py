def flood_fill(matrix,sr,sc,newcolour):
	drow = [1,0,-1,0]
	dcol = [0,1,0,-1]

	m = len(matrix[0]) #cols
	n = len(matrix) #rows

	def is_valid(r,c):
		return r>=0 and r<n and c>=0 and c<m

	def dfs(r,c,ini):
		matrix[r][c] = newcolour

		for i in range(4):
			nrow = r + drow[i]
			ncol = c + dcol[i]

			if is_valid(nrow,ncol) and matrix[nrow][ncol]==ini:
				dfs(nrow,ncol,ini)

	dfs(sr,sc,matrix[sr][sc])
	return matrix



	pass 


matrix = [	[1,1,1], 
			[1,1,0],
			[1,0,1] ]

print(flood_fill(matrix,1,1,2))

#number of islands is also same

