/*

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



*/


class Solution {
    private int n, m;
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        n = grid.length;
        m = grid[0].length;
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < m; j++)
                if (grid[i][j] > 0) ans = Math.max(ans, trav(i, j, grid));
        return ans;
    }
    private int trav(int i, int j, int[][] grid) {
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] < 1) return 0;
        grid[i][j] = 0;
        return 1 + trav(i-1, j, grid) + trav(i, j-1, grid) + trav(i+1, j, grid) + trav(i, j+1, grid);
    }
}


// DFS

class Solution {
    int m, n;
    int[] DIR = new int[]{0, 1, 0, -1, 0};
    public int maxAreaOfIsland(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int ans = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                ans = Math.max(ans, dfs(grid, r, c));
            }
        }
        return ans;
    }
    int dfs(int[][] grid, int r, int c) {
        if (r < 0 || r == m || c < 0 || c == n || grid[r][c] == 0) return 0;
        int ans = 1;
        grid[r][c] = 0; // Mark this square as visited
        for (int i = 0; i < 4; i++)
            ans += dfs(grid, r + DIR[i], c + DIR[i+1]);
        return ans;
    }
}

/*

Complexity:

Time: O(M * N), where M is number of rows, N is number of columns in the grid.
Space: O(M * N), the space used by the depth stack during our recursion, in worst case is O(M * N).

*/


// BFS



class Solution {
    int m, n;
    int[] DIR = new int[]{0, 1, 0, -1, 0};
    public int maxAreaOfIsland(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int ans = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1)
                    ans = Math.max(ans, bfs(grid, r, c));
        return ans;
    }
    int bfs(int[][] grid, int r, int c) {
        int ans = 0;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{r, c});
        grid[r][c] = 0;
        while (!q.isEmpty()) {
            int[] top = q.poll();
            ++ans;
            for (int i = 0; i < 4; i++) {
                int nr = top[0] + DIR[i], nc = top[1] + DIR[i+1];
                if (nr < 0 || nr == m || nc < 0 || nc == n || grid[nr][nc] == 0) continue;
                grid[nr][nc] = 0; // Mark as visited
                q.offer(new int[]{nr, nc});
            }
        }
        return ans;
    }
}


/*

Complexity:

Time: O(M * N), where M is number of rows, N is number of columns in the grid.
Space: O(M * N), the space used by the queue in bfs, in worst case is O(M * N).

*/



// Another solution

// The idea is to count the area of each island using dfs. During the dfs, we set the value of each point in the island to 0. 
// Time complexity is O(mn).

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max_area = 0;
        for(int i = 0; i < grid.length; i++)
            for(int j = 0; j < grid[0].length; j++)
                if(grid[i][j] == 1)max_area = Math.max(max_area, AreaOfIsland(grid, i, j));
        return max_area;
    }
    
    public int AreaOfIsland(int[][] grid, int i, int j){
        if( i >= 0 && i < grid.length && j >= 0 && j < grid[0].length && grid[i][j] == 1){
            grid[i][j] = 0;
            return 1 + AreaOfIsland(grid, i+1, j) + AreaOfIsland(grid, i-1, j) + AreaOfIsland(grid, i, j-1) + AreaOfIsland(grid, i, j+1);
        }
        return 0;
    }
}




// Another solution


class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                max = Math.max(max, dfs(grid, i, j));
            }
        }
        return max;
    }
    
    int dfs(int[][] grid, int row, int column) {
        if(row < 0 || row >= grid.length || column < 0 || column >= grid[0].length || grid[row][column] == 0) return 0;
        
        grid[row][column] = 0;
        
        return 1+ dfs(grid, row+1, column) + dfs(grid, row-1, column) + dfs(grid, row, column+1) + dfs(grid, row, column-1);
    }
}



// Another solution


class Solution 
{
    public int maxAreaOfIsland(int[][] grid)  // Main method.
    {
        int supportMetod = 0; // Set var for the support method so that we can hold onto the method's progress.
        int maxIslandSize = 0; // Set var for max area of an Island.
        
         for(int x = 0; x < grid.length; x++) // Loop through the matrix in search for a starting point.
         {
             for(int y = 0; y < grid[0].length; y++)
             {
                 if(grid[x][y] == 1) // When a starting point has been found, call the support method.
                 {
                     supportMetod = helper(grid, x, y);
					 
                     maxIslandSize = Math.max(maxIslandSize, supportMetod); // Assess which var holds the max value.
                 }
             }
         }
             return maxIslandSize; // return the said value;
    }
    
    private int helper(int[][] grid, int x, int y) // Support method.
    {
        if(x < 0 || grid.length-1 < x || y < 0 || grid[0].length-1 < y || grid[x][y] == 0) // Check for boundaries or spots that are coverd in water.
        {
            return 0;
        }
       
        grid[x][y] = 0; // When an Island has been found, start calculate it's size and then sink the sucker.
        
        int up = helper(grid, x-1, y);  // Valid ways to traversing  the matrix.
        int down = helper(grid, x+1, y);
        int left = helper(grid, x, y-1);
        int right = helper(grid, x, y+1);
        
        return up + down + left + right + 1; // Return the area of the Island to the main method for further assessment.
		
    }
}




// DFS minimum code


class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, maxarea = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                maxarea = Math.max(maxarea, dfs(i, j, grid));
        return maxarea;
    }

    private int dfs(int i, int j, int[][] grid) {
        return (i < 0 || grid.length <= i || j < 0 || grid[0].length <= j || grid[i][j] <= 0) ? 0
            : grid[i][j]-- + dfs(i, j+1, grid) + dfs(i+1, j, grid) + dfs(i, j-1, grid) + dfs(i-1, j, grid);
    }
}
