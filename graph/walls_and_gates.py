#multisource bfs

# multisource bfs
from typing import List
from collections import deque
class Solution:
    def __init__(self):
        self.drow = [1,0,-1,0]
        self.dcol = [0,1,0,-1]

    


    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        inf = 2**31 - 1
        q = deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + a, j + b
                    # bfs so first reaching inf is always the shortest
                    # set its value from inf to d, same as marking as visited
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == inf:
                        rooms[x][y] = d
                        q.append((x, y))

    #map of highest peak is exactly same as this but instead of int return whole level matrix

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m= len(grid[0])

        def is_valid(r,c):
            return r>=0 and r<n and c>=0 and c<m

        drow = [1,0,-1,0]
        dcol = [0,1,0,-1]

        queue = []
        level = [[float("inf") for i in range(m)] for j in range(n)]
         
        ans = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    queue.append((i,j))
                    level[i][j] = 0
        
        #satrt multisorce bfs
        while queue:
            r,c = queue.pop(0)

            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if is_valid(nrow,ncol) and level[r][c] + 1 < level[nrow][ncol]:
                    level[nrow][ncol] = level[r][c]+1
                    queue.append((nrow,ncol))
                    ans = max(ans,level[nrow][ncol])

        return ans

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt_fresh = 0
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    cnt_fresh+=1
                if grid[i][j]==2:
                    q.append([[i,j],0])
        
        cnt  = 0
        tm = 0
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        
        while q:
            r = q[0][0][0]
            c= q[0][0][1]
            t = q[0][1]
            tm = max(tm,t)
            q.pop(0)
            
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                
                if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1):
                    grid[nrow][ncol]=2
                    q.append([[nrow,ncol],t+1])
                    cnt+=1
        if cnt_fresh!=cnt:
            return -1
        return tm


    #good question and constructive thinking
    def distinct_islands(self,grid):
        n = len(grid)
        m  = len(grid[0])

        visited = [[0]*m for i in range(n)]

        def is_valid(r,c):
            return r>=0 and r<n and c>=0 and c<m

        def dfs(r,c,row0,col0):
            nonlocal vec
            visited[r][c] = True
            vec+=(r-row0 ,c-col0)
            for i in range(4):
                nrow = r + self.drow[i]
                ncol = c + self.dcol[i]

                if is_valid(nrow,ncol) and not visited[nrow][ncol] and grid[nrow][ncol]==1:
                    dfs(nrow,ncol,row0,col0)

            return vec


        ans = set()

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]==1:
                    vec = ()
                    dfs(i,j,i,j)

                    ans.add(vec)
                    
        return len(ans)


                

c = Solution()

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
grid = [[1,0,1],[0,0,0],[1,0,1]]

c.wallsAndGates(rooms)
print(rooms)

print("********************************")
print(c.maxDistance(grid))

print("********************************")
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(c.orangesRotting(grid))

print("********************************")
grid =[
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]];
print("distinct_islands: ",c.distinct_islands(grid))





