'''


Approach 1. Brute-force solution
Time complexity: O((m * n)^2)
Space complexity: O(1) because the output doesn't count towards the space complexity.
For each cell that is not a zero, traverse the whole grid and compute its distance to the cells with zeros, 
taking the minimum of the current closest distance to a zero and what we've just found. 
Because we can only traverse vertically and horizontally, not diagonally, 
this means we'll have to use the Manhattan/taxicab distance/metric. 
So the distance between (i, j) and (k, l) is abs(i - k) + abs(j - l).



'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        output = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    for k in range(m):
                        for l in range(n):
                            if mat[k][l] == 0:
                                output[i][j] = min(output[i][j], abs(i - k) + abs(j - l))

        return output
        
        
        
        
'''


Approach 2a. Breadth-first search solution from ones
Time complexity: O((m * n)^2); in practice, this should be better than Approach 1's brute-force solution 
since the latter only scans the entire grid in the worst case (for example, if we zeros only on the top-left and bottom-right), 
whereas the former always scans the entire grid.
Space complexity: O(min(m, n)) due to the space taken up by the queue.
A slightly better approach than above is if we perform BFS outward from cells with 1 entries, 
rather than scanning the entire grid each time.


'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        output = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        def bfs(i, j):
            queue = deque([(i, j)])
            visited = set((i, j))

            distance = 0

            while len(queue) > 0:
                size = len(queue)

                while size > 0:
                    size -= 1

                    x, y = queue.popleft()

                    if mat[x][y] == 0:
                        return distance

                    for x, y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                            visited.add((x, y))
                            queue.append((x, y))

                distance += 1

            return distance                


        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    output[i][j] = bfs(i, j)

        return output
      
      
      
      
'''


Approach 2b. Breadth-first search solution from zeros
Time complexity: O(m * n)
Space complexity: O(m * n) because, in the worst case, 
the entire grid can be zeros so we'd enqueue all m * n cells onto our queue.
A better BFS than 2a, this solution is similar to the BFS solution for 286. Walls and Gates. 
Rather than doing DFS/BFS starting from non-zero cells, we can instead perform BFS from the zero cells simultaneously. 
In the first frontier, we'll encounter all the cells that are one cell removed from a zero; in the second frontier, 
we'll encounter all the cells that are two cells removed from a zero; and so on. Due to the nature of BFS (i.e. 
We visit all cells of distance d before visting cells of distance d + 1), the first time we encounter a cell, 
we know that the current distance will be its closest distance to a zero cell.


'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        output = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))

        distance = 0

        while len(queue) > 0:
            size = len(queue)

            while size > 0:
                size -= 1

                i, j = queue.popleft()

                if mat[i][j] != 0:
                    output[i][j] = distance

                for i, j in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                        visited.add((i, j))
                        queue.append((i, j))

            distance += 1

        return output
      
      
      
      
'''


Approach 3. Dynamic programming solution
Time complexity: O(m * n)
Space complexity: O(1) because the output does not count towards the space complexity
Given a non-zero cell mat[i][j] if we know the distances from zero for its neighbors, 
then we can compute the current cell's closest distance to zero as 1 + the minimum of it's neighboring cells' distances to zero. 
To enforce the optimal substructure needed to implement dynamic programming, we'll have to do two rounds: 
one from top-left to bottom-right, and a reverse round from bottom-right to top-left.


'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])

        return dp
      
      
      
      

      
'''


We simply do 2 iterations from first to last and last to first element.
For the 1st for loop, we update distance of element with minimum of previous top and left elements + 1 (itself).
For the 2nd for loop, we update distance of element with minimum of previous bottom and right elements + 1 (itself).
As a result, we get minimum distance value for each element updated with distances of neighbours + 1.


'''


class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix
      
      
      
      
'''


In this problem for each cell we need to find the closest distance to cell with 0 inside. 
We can reverse this problem: 
we start with all cells with 0 inside and run bfs - we can call it multi-source bfs, 
because in the first moment of time we start from several different cells. 
Also here I use variant of bfs when we go level by level: first we found all cells with distance 1, 
then with distance 2 and so on - you can do in in classical way as well. 
When we traverse some cell we update its value, so in the end we just return matrix M.

Complexity
Time complexity is O(mn), space complexity as well.


'''


class Solution:
    def updateMatrix(self, M):
        m, n, queue, visited = len(M), len(M[0]), deque(), set()
        for y, x in product(range(m), range(n)):
            if M[y][x] == 0: 
                queue.append((y, x))
                visited.add((y, x))
                
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                y, x = queue.popleft()
                for dy, dx in dirs:
                    if 0<=y+dy<m and 0<=x+dx<n and (y+dy, x+dx) not in visited:
                        M[y+dy][x+dx] = level
                        queue.append((y+dy, x+dx))
                        visited |= {(y+dy, x+dx)}
        
        return M
      
      
      

      
'''


BFS: first, we find all 0s, and the distance for them are 0. 
We push all of its cooridinates (i, j) to queue and record them as visited. 
Then we check all its neighours, those neighours should have distance 1. 
Then we push those neighours to the queue, and again check the neighours for each one, 
now the distance becomes 2, we will stop when all the cells are checked. 
Since the distances aways increase by one by each iteration, 
so we don't need to worry, that we might find shorter distance later, 
so the current distance + 1 is the best distance that its neighours can get already.


'''
      

  
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if i - 1 >= 0 and (i-1, j) not in visited:
                    matrix[i-1][j] = matrix[i][j] + 1
                    visited.add((i-1, j))
                    queue.append((i-1, j))
                if i + 1 < m and (i+1, j) not in visited:
                    matrix[i+1][j] = matrix[i][j] + 1
                    visited.add((i+1, j))
                    queue.append((i+1, j))
                if j - 1 >= 0 and (i, j-1) not in visited:
                    matrix[i][j-1] = matrix[i][j] + 1
                    visited.add((i, j-1))
                    queue.append((i, j-1))
                if j + 1 < n and (i, j+1) not in visited:
                    matrix[i][j+1] = matrix[i][j] + 1
                    visited.add((i, j+1))
                    queue.append((i, j+1))
        return matrix
      
      
      

      
      
############ minmized code #################


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """ O(N)TS in place modifications """
        gates = [(y, x) for y, row in enumerate(mat) for x, val in enumerate(row) if not val]
        mat = [[-1 * i for i in row] for row in mat]

        for y0, x0 in gates:
            for y, x in ((y0 + 1, x0), (y0 - 1, x0), (y0, x0 + 1), (y0, x0 - 1)):
                if 0 <= y < len(mat) and 0 <= x < len(mat[0]) and mat[y][x] == -1:
                    mat[y][x] = mat[y0][x0] + 1
                    gates += (y, x),
        return mat
      
      
      
