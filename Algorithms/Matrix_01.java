/*

Solution 1: BFS on zero cells first

For convinience, let's call the cell with value 0 as zero-cell, 
the cell has with value 1 as one-cell, the distance of the nearest 0 of a cell as distance.
Firstly, we can see that the distance of all zero-cells are 0.
Same idea with Topology Sort, we process zero-cells first, 
then we use queue data structure to keep the order of processing cells, 
so that cells which have the smaller distance will be processed first. 
Then we expand the unprocessed neighbors of the current processing cell and push into our queue.
Afterall, we can achieve the minimum distance of all cells in our matrix.


Complexity

Time: O(M * N), where M is number of rows, N is number of columns in the matrix.
Space: O(M * N), space for the queue.

*/

class Solution {
    int[] DIR = new int[]{0, 1, 0, -1, 0};
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length; // The distance of cells is up to (M+N)
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                if (mat[r][c] == 0) q.offer(new int[]{r, c});
                else mat[r][c] = -1; // Marked as not processed yet!

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0], c = curr[1];
            for (int i = 0; i < 4; ++i) {
                int nr = r + DIR[i], nc = c + DIR[i+1];
                if (nr < 0 || nr == m || nc < 0 || nc == n || mat[nr][nc] != -1) continue;
                mat[nr][nc] = mat[r][c] + 1;
                q.offer(new int[]{nr, nc});
            }
        }
        return mat;
    }
}




/*


Solution 2: Dynamic Programming

For convinience, let's call the cell with value 0 as zero-cell, 
the cell has with value 1 as one-cell, the distance of the nearest 0 of a cell as distance.
Firstly, we can see that the distance of all zero-cells are 0, 
so we skip zero-cells, we process one-cells only.
In DP, we can only use prevous values if they're already computed.
In this problem, a cell has at most 4 neighbors that are left, top, right, bottom. 
If we use dynamic programming to compute the distance of the current cell based on 4 neighbors simultaneously, 
it's impossible because we are not sure if distance of neighboring cells is already computed or not.
That's why, we need to compute the distance one by one:
Firstly, for a cell, we restrict it to only 2 directions which are left and top. 
Then we iterate cells from top to bottom, and from left to right, 
we calculate the distance of a cell based on its left and top neighbors.
Secondly, for a cell, we restrict it only have 2 directions which are right and bottom. 
Then we iterate cells from bottom to top, and from right to left, 
we update the distance of a cell based on its right and bottom neighbors.


Complexity

Time: O(M * N), where M is number of rows, N is number of columns in the matrix.
Space: O(1)

*/



class Solution { // 5 ms, faster than 99.66%
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length, INF = m + n; // The distance of cells is up to (M+N)
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 0) continue;
                int top = INF, left = INF;
                if (r - 1 >= 0) top = mat[r - 1][c];
                if (c - 1 >= 0) left = mat[r][c - 1];
                mat[r][c] = Math.min(top, left) + 1;
            }
        }
        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (mat[r][c] == 0) continue;
                int bottom = INF, right = INF;
                if (r + 1 < m) bottom = mat[r + 1][c];
                if (c + 1 < n) right = mat[r][c + 1];
                mat[r][c] = Math.min(mat[r][c], Math.min(bottom, right) + 1);
            }
        }
        return mat;
    }
}




// BFS


class Solution {
    private class Point {
        int x;
        int y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    private int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    // Soluton: use BFS starting from each 0 cell and mark new length for each 1 cell
    // Note: Need a way to differentiate original 1 and distance 1
    public int[][] updateMatrix(int[][] matrix) {
        Queue<Point> queue = new LinkedList<>();
        
        // Fill 1 with -1
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] = -1;
                } else {
                    queue.offer(new Point(i, j));
                }
            }
        }
        
        // BFS starting from each 0 cell
        int length = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            length++;
            for (int i = 0; i < size; i++) {
                Point curPoint = queue.poll();
                for (int[] dir : dirs) {
                    int ii = curPoint.x + dir[0];
                    int jj = curPoint.y + dir[1];
                    
                    if (ii >= 0 && jj >= 0 && ii < matrix.length && jj < matrix[0].length) {
                        if (matrix[ii][jj] == -1) {
                            matrix[ii][jj] = length;
                            queue.offer(new Point(ii, jj));
                        }
                    }
                }
            }
        }
        
        return matrix;
    }
}




/*

Using DFS method.

Assigned a large value to all the positions with value 1 and don't have 0 neighbors
Start dfs search from positions whose value is 1

*/



public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        if(matrix.length==0) return matrix;
        
        for(int i = 0; i<matrix.length; i++)
            for(int j = 0; j<matrix[0].length; j++)
                if(matrix[i][j]==1&&!hasNeiberZero(i, j,matrix)) 
                    matrix[i][j] = matrix.length+matrix[0].length+1;
        
        for(int i = 0; i<matrix.length; i++)
            for(int j = 0; j<matrix[0].length; j++)
                if(matrix[i][j]==1)
                    dfs(matrix, i, j, -1);
        
        return matrix;
    }
    private void dfs(int[][] matrix, int x, int y, int val){
        if(x<0||y<0||y>=matrix[0].length||x>=matrix.length||matrix[x][y]<=val)
            return;
        
        if(val>0) matrix[x][y] = val;
        
        dfs(matrix, x+1, y, matrix[x][y]+1);
        dfs(matrix, x-1, y, matrix[x][y]+1);
        dfs(matrix, x, y+1, matrix[x][y]+1);
        dfs(matrix, x, y-1, matrix[x][y]+1);
        
    }
    private boolean hasNeiberZero(int x, int y, int[][] matrix){
        if(x>0&&matrix[x-1][y]==0) return true;
        if(x<matrix.length-1&&matrix[x+1][y]==0) return true;
        if(y>0&&matrix[x][y-1]==0) return true;
        if(y<matrix[0].length-1&&matrix[x][y+1]==0) return true;
        
        return false;
    }
}




// alternate solution



class Solution {
    public class Pair{
        int x;
        int y;

    Pair(int x, int y) {
      this.x = x;
      this.y = y;
    }
    }
    
    private static int[][] dirs = new int[][] { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
    
    
    public int[][] updateMatrix(int[][] matrix) {
        //  Step 1:Store all the 0's index in queue and make all 1 as -1 in the matrix
    /*
    for eg:
           0 0 0
           0 1 1
           1 1 1
           
           make this as
           0 0 0
           0 -1 -1
           -1 -1 -1
           
    */
    
    ArrayDeque <Pair> q=new ArrayDeque<>();
    for(int i =0;i<matrix.length;i++){
        for(int j =0;j<matrix[i].length;j++){
            if(matrix[i][j]==0){
                // stored it in queue
                q.add(new Pair(i,j));
            }
            else{
                // make it as -1
                matrix[i][j]=-1;
                
            }
        }
    }
    
    
    // Now Start removing elements from queue check whehther its neighbour are less than 0 i.e -1;
    
    while(q.size()!=0){
        Pair rem=q.removeFirst();
        
        // after removing check if its neighbour are -1 or not 
        
        for(int i =0;i<dirs.length;i++){
            /*
            we already have a dirs matrix={ { 1, 0 },
                                           { -1, 0 },
                                           { 0, 1 }, 
                                           { 0, -1 } }
            */
            int newrow=rem.x+ dirs[i][0];//we are selecting it as a pair row and coloumn combine
            int newcoloum=rem.y+dirs[i][1];
            
            
            // Now we are checking element less than 0 around 0 in 4 direction
            if(newrow>=0 && newcoloum>=0 && newrow<matrix.length && newcoloum<matrix[0].length && matrix[newrow][newcoloum]<0){
             
               matrix[newrow][newcoloum]=matrix[rem.x][rem.y]+1;//distance of 1 unit will be added
               
              q.addLast(new Pair(newrow,newcoloum));
                     //   Now where -1 was present initially we are going to add its index into as now its distance will alod be added into the queue so that where -1 is still present its distance will also be added
          
            }
        }
    }
    
    return matrix;
    }
}

