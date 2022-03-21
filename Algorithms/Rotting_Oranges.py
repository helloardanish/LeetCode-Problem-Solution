'''


This is graph traversal problem, so here we have a choise: to use dfs or to use bfs. 
What is asked: minimum number of minutes passed until there is no fresh orange. 
In graphs it means to find the greatest distance from rotten oranges to any other orange. 
Usually, if we need to find the distances, we use bfs. So, let me define my variables:

m and n are dimensions of our grid, also we have queue to run our bfs and also we want to count number of fresh oranges: 
we need this to check in the end if all oranges become rotten or not.
We put all rotten oranges coordinates to our queue, so we are going to start from all of them. 
Also we count number of fresh oranges.
Define directions we can go: four of them and put levels = 0.
Now, we traverse our grid, using bfs, using level by level traversal: it means, that each time, 
when we have some elements in queue, we popleft all of them and put new neighbours to the end. 
In this way each time we reach line levels += 1, we have nodes with distance which is 1 bigger than previous level. 
In the end levels - 1 will be our answer, because one time in the end when we do not have anythin to add, 
levels still be incremented by one.

Finally, we check if we still have fresh oranges, and if yes, return -1. 
If not, we need to return max(levels-1, 0), because it can happen, 
that our queue was empty in the beginning and we do not need to subtract 1.

Complexity: time complexity is O(mn), because we first traverse our grid to fill queue and found number of fresh oranges. 
Then we use classical bfs, so each node will be added and removed from queue at most 1 time. 
Space complexity is also can be O(mn), we can have for example O(mn) rotten oranges in the very beginnig.


'''


class Solution:
    def orangesRotting(self, grid):
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i,j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i,j))
            if grid[i][j] == 1: fresh += 1
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        levels = 0
        
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
                        
        return -1 if fresh != 0 else max(levels-1, 0)
      
      
      

'''
Idea:

Add all fresh oranges to fresh_set and append all rotten oranges to rotten_queue.
Use BFS to find all fresh oranges that adjacent to the current rotten orange, 
turn these fresh oranges to rotten and remove these from fresh_set. In the meantime, track the steps of turning.
After we finish the turning, if there is still a fresh orange in fresh_set, return -1 otherwist return the step.

Time complexity is O(mn) where m is size of row and n is size of columns.

'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        fresh_set=set()
        rotten = collections.deque()
        step = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y]==1:
                    fresh_set.add((x,y))
                elif grid[x][y]==2:
                    rotten.append([x,y,step])
        while rotten:
            x,y,step = rotten.popleft()
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy]=2
                    fresh_set.remove((x+dx,y+dy))
                    rotten.append([x+dx,y+dy,step+1])
        return step if not fresh_set else -1
      
      
      




########## another solution ###############



from collections import deque

# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1
        
        # number of columns
        cols = len(grid[0])
        
        # keep track of fresh oranges
        fresh_cnt = 0
        
        # queue with rotten oranges (for BFS)
        rotten = deque()
        
        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1
        
        # keep track of minutes passed.
        minutes_passed = 0
        
        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1
            
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    fresh_cnt -= 1
                    
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        
        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1
      
      


      
      
      
      
################# Same as above BFS using for loop  ####################################




class Solution(object):
    def orangesRotting(self, grid):
        n,m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append((i,j))
        res = 0
        while Q:
            for _ in range(len(Q)):
                i,j = Q.popleft()
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x,y))
            res += 1
        return max(0, res-1) if cnt == 0 else -1
      
      
      
      
#################################   DFS   #######################################
      
  
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        # build initial array of rotten oranges
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        # get unvisited neighbors of all rotten oranges
        def add_neighbors(rotten):
            neighbors = []
            for i, j in rotten:
                if i > 0 and grid[i - 1][j] == 1:
                    neighbors.append((i - 1, j))
                    grid[i-1][j] = 2
                if j > 0 and grid[i][j - 1] == 1:
                    neighbors.append((i, j - 1))
                    grid[i][j-1] = 2
                if i < rows - 1 and grid[i + 1][j] == 1:
                    neighbors.append((i + 1, j))
                    grid[i + 1][j] = 2
                if j < columns - 1 and grid[i][j + 1] == 1:
                    neighbors.append((i, j + 1))
                    grid[i][j+1] = 2
            return neighbors

        minutes = 0
        while (1):
            rotten = add_neighbors(rotten)
            if len(rotten) == 0:
                break
            minutes += 1

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1

        return minutes
      
      
      
############## Minimized code  ##########################


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer
      
      
      
      
## another
      
      
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """ O(N*M)TS """

        bads = [(y, x) for y, row in enumerate(grid) for x, val in enumerate(row) if val == 2]
        grid = [[x - 2 for x in row] for row in grid]  # 0-bad -1-frash -2-obstacle

        for by, bx in bads:
            for y, x in ((by + 1, bx), (by - 1, bx), (by, bx + 1), (by, bx - 1)):
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == -1:
                    grid[y][x] = grid[by][bx] + 1
                    bads += (y, x),

        result = list(itertools.chain.from_iterable(grid)) + [0]  # for border case with no fruits
        return max(result) if -1 not in result else -1
      
      
      
      
