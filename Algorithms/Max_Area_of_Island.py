'''


Idea:
So we can just use a simple iteration through the grid and look for islands. When we find an island, 
we can use a recursive helper function (trav) to sum up all the connected pieces of land 
and return the total land mass of the island.

As we traverse over the island, we can replace the 1s with 0s to prevent "finding" the same land twice. 
We can also keep track of the largest island found so far (ans), and after the grid has been fully traversed, 
we can return ans.

Time Complexity: O(N * M) where N and M are the lengths of the sides of the grid
Space Complexity: O(L) where L is the size of the largest island, representing the maximum recursion stack
or O(N * M + L) if we create an N * M matrix in order to not modify the input



'''



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        def trav(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
        for i, j in product(range(n), range(m)):
            if grid[i][j]: ans = max(ans, trav(i, j))
        return ans


################# DFS  ##############################



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]

        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0: 
                return 0
            ans = 1
            grid[r][c] = 0  # Mark this square as visited
            for i in range(4):
                ans += dfs(r + DIR[i], c + DIR[i + 1])
            return ans

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans

      
      
'''


Complexity:

Time: O(M * N), where M is number of rows, N is number of columns in the grid.
Space: O(M * N), the space used by the depth stack during our recursion, in worst case is O(M * N).


'''
      
      
##################   BFS   ##########################


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            ans = 0
            while q:
                r, c = q.popleft()
                ans += 1
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
                    grid[nr][nc] = 0  # Mark this square as visited
                    q.append((nr, nc))
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
        return ans


      
'''


Complexity:

Time: O(M * N), where M is number of rows, N is number of columns in the grid.
Space: O(M * N), the space used by the queue in bfs, in worst case is O(M * N).


'''
      
      
############# Another solution #####################




def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
      
      
      
###############  another solution  ################


'''

When you see problem about islands, you most probably should use dfs or bfs. 
It is possible to use any of them, for me dfs is a bit simpler to code. 
We start dfs from every not visited yet point and I direclty change grid cell to # symbol 
(we can change it back in the end if needed). 
For every island we count number of nodes inside this island and keep it in Counter. 
In the end we traverse all islands and choose the biggest one.

Complexity
Time complexity is O(mn), because we visit each edge in our graph only once. 
Space complexity can also be potentially O(mn) here.

'''

class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        neibs = [[1,0],[-1,0],[0,-1],[0,1]]
        islands, count = Counter(), 0
        
        def dfs(t, i, j):
            if not 0<=i<m or not 0<=j<n or grid[i][j] != 1: return
            islands[t] += 1
            grid[i][j] = '#'
            for x, y in neibs: dfs(t, x+i, y+j)
        
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dfs(count, i, j)
                count += 1
                
        return max(list(islands.values()) + [0])
      
      
      
      
########### Another solution ###################


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
                    
        return maxArea
    
                    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return 0
        
        maxArea = 1
        grid[i][j] = '#'  # this will act as visited set
        maxArea += self.dfs(grid, i+1, j)
        maxArea += self.dfs(grid, i-1, j)
        maxArea += self.dfs(grid, i, j+1)
        maxArea += self.dfs(grid, i, j-1)
        
        return maxArea
      
      
      
############# Another solution ###################


class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
					# Reset cur_area to 0
                    self.cur_area = 0
                    self.dfs(grid, i, j)
                    
                    max_area = max(max_area, self.cur_area)
                    
        return max_area
        
    def dfs(self, grid, i, j):
        self.cur_area += 1
        grid[i][j] = '#'
        
		# Check left
        if j - 1 >= 0 and grid[i][j-1] == 1:
            self.dfs(grid, i, j-1)
        
		# Check right
        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            self.dfs(grid, i, j+1)
        
		# Check up
        if i - 1 >= 0 and grid[i-1][j] == 1:
            self.dfs(grid, i-1, j)
        
		# Check down
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            self.dfs(grid, i+1, j)
          
          
          

          
          
############## Union-find ########################


class UnionFind:
    def __init__(self, N):
        self.group = N                  # all disjoint
        self.parent = list(range(N))    # point to self
        self.rank = [0] * N             # approx subtree height
        self.size = [1] * N             # tree size

    def find(self, p):
        parent = self.parent
        while p != parent[p]:
            parent[p] = parent[parent[p]] # path compression
            p = parent[p]
        return p

    def union(self, p, q):
        if p == q: return
        i, j = self.find(p), self.find(q)
        if i == j: return
        self.group -= 1
        parent, rank, size = self.parent, self.rank, self.size
        if rank[i] > rank[j]:
            parent[j] = i
            size[i] += size[j]
        elif rank[i] < rank[j]:
            parent[i] = j
            size[j] += size[i]
        else:
            parent[i] = j
            size[j] += size[i]
            rank[j] += 1
            
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        H = len(grid)
        if H <= 0: return 0
        W = len(grid[0])
        if W <= 0: return 0
        
        uf = UnionFind(H*W)
        ind, max_area = -1, 0
        for r in range(H):
            for c in range(W):
                ind += 1
                if grid[r][c] == 1:
                    if r > 0 and grid[r-1][c] == 1:
                        uf.union(ind, ind-W)
                    if c > 0 and grid[r][c-1] == 1:
                        uf.union(ind, ind-1)
                    max_area = max(max_area, uf.size[uf.find(ind)])
        
        return max_area
      
      
      
################# DFS   ###########################


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def getArea(r,c,area):
                        
            if r>=rows or r<0 or c>=cols or c<0:
                return 0
                        
            if grid[r][c]==0: return 0
            
            grid[r][c]=0
            area=1+ getArea(r-1,c,area) + getArea(r+1,c,area) +getArea(r,c+1,area)+ getArea(r,c-1,area)
            return area
            
        
        rows=len(grid)
        cols=len(grid[0])
        maxArea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxArea=max(maxArea,getArea(r,c,0))
        return maxArea


      

      
########## Minimized solution ####################


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ O(N*M)TS """

        def fn(y, x):
            return grid.pop((y, x), 0) and 1 + fn(y + 1, x) + fn(y - 1, x) + fn(y, x + 1) + fn(y, x - 1) # это позволяет возвращать ноль в base case

        grid = {(y, x): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}
        return max(fn(y, x) for y, x in grid.copy())
