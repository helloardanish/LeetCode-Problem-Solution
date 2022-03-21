/*

// BFS

Firstly, we traverse the whole grid to find out the positions of rotten oranges and compute the total num of orange as well, 
enqueue the positions of rotten oranges into a queue;
Secondly, dequeue to get the position of a rotten orange. 
Due to the infection, the fresh oranges near the rotten orange become rotten. 
So we check the cell in the left/right/top/down of the rotten orange, if it is a fresh orange, enqueue it. 
Continue to dequeue until all rotten oranges of last round are removed from the queue


*/



class Solution {
    // store the position of rotten orange
    static class Position {
        int x;
        int y;
        Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
	
    public int orangesRotting(int[][] grid) {
        Queue<Position> q = new LinkedList<>();
        int total = 0, rotten = 0, time = 0;
		
		// traverse the grid, offer position of rotten orange into queue, and count the total num of orange
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1 || grid[i][j] == 2) total++;
                if (grid[i][j] == 2) q.offer(new Position(i, j));
            }
        }
		
		// if there is no orange, return 0;
        if (total == 0) return 0;
		
        while (! q.isEmpty() && rotten < total) {
			// size is the num of rotten oranges of the last round
            int size = q.size();
			
			// count the num of rotten oranges, if it equals to total num, return time;
            rotten += size;
            if (rotten == total) return time;
			
			// every round, time ++
            time++;
			
			// Continue to dequeue until all rotten oranges of last round are removed from the queue
            for (int i = 0; i < size; i++) {
                Position p = q.peek();
				
				// check the cell in the left/right/top/down of the rotten orange, if it is a fresh orange, enqueue it.
                if (p.x + 1 < grid.length && grid[p.x + 1][p.y] == 1) {
                    grid[p.x + 1][p.y] = 2;
                    q.offer(new Position(p.x + 1, p.y));
                }
                if (p.x - 1 >= 0 && grid[p.x - 1][p.y] == 1) {
                    grid[p.x - 1][p.y] = 2;
                    q.offer(new Position(p.x - 1, p.y));
                }
                if (p.y + 1 < grid[0].length && grid[p.x][p.y + 1] == 1) {
                    grid[p.x][p.y + 1] = 2;
                    q.offer(new Position(p.x, p.y + 1));
                }
                if (p.y - 1 >= 0 && grid[p.x][p.y - 1] == 1) {
                    grid[p.x][p.y - 1] = 2;
                    q.offer(new Position(p.x, p.y - 1));
                }
                q.poll();
            }
        }
        return -1;
    }
}





// BFS

class Solution {
    public int orangesRotting(int[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int count_fresh = 0;
        //Put the position of all rotten oranges in queue
        //count the number of fresh oranges
        for(int i = 0 ; i < rows ; i++) {
            for(int j = 0 ; j < cols ; j++) {
                if(grid[i][j] == 2) {
                    queue.offer(new int[]{i , j});
                }
                else if(grid[i][j] == 1) {
                    count_fresh++;
                }
            }
        }
        //if count of fresh oranges is zero --> return 0 
        if(count_fresh == 0) return 0;
        int count = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        //bfs starting from initially rotten oranges
        while(!queue.isEmpty()) {
            ++count;
            int size = queue.size();
            for(int i = 0 ; i < size ; i++) {
                int[] point = queue.poll();
                for(int dir[] : dirs) {
                    int x = point[0] + dir[0];
                    int y = point[1] + dir[1];
                    //if x or y is out of bound
                    //or the orange at (x , y) is already rotten
                    //or the cell at (x , y) is empty
                        //we do nothing
                    if(x < 0 || y < 0 || x >= rows || y >= cols || grid[x][y] == 0 || grid[x][y] == 2) continue;
                    //mark the orange at (x , y) as rotten
                    grid[x][y] = 2;
                    //put the new rotten orange at (x , y) in queue
                    queue.offer(new int[]{x , y});
                    //decrease the count of fresh oranges by 1
                    count_fresh--;
                }
            }
        }
        return count_fresh == 0 ? count-1 : -1;
    }
}



// DFS


class Solution {
    
    public int orangesRotting(int[][] grid) {
        if(grid == null || grid.length == 0) return -1;
        
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j] == 2) rotAdjacent(grid, i, j, 2);
            }
        }
        
        int minutes = 2;
        for(int[] row : grid) {
            for(int cell : row) {
                if(cell == 1) return -1;
                minutes = Math.max(minutes, cell);
            }
        }
        
        return minutes - 2;
    }
    
    private void rotAdjacent(int[][] grid, int i, int j, int minutes) {
        if(i < 0 || i >= grid.length /* out of bounds */
          || j < 0 || j >= grid[0].length /* out of bounds */
          || grid[i][j] == 0 /* empty cell */
          || (1 < grid[i][j] && grid[i][j] < minutes) /* this orange is already rotten by another rotten orange */
          ) return;
        else {
            grid[i][j] = minutes;
            rotAdjacent(grid, i - 1, j, minutes + 1);
            rotAdjacent(grid, i + 1, j, minutes + 1);
            rotAdjacent(grid, i, j - 1, minutes + 1);
            rotAdjacent(grid, i, j + 1, minutes + 1);
        }
    }
}




