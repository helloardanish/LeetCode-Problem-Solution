class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor) return image;
        fill(image, sr, sc, image[sr][sc], newColor);
        return image;
    }
    
    private void fill(int[][] image, int sr, int sc, int color, int newColor) {
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != color) return;
        image[sr][sc] = newColor;
        fill(image, sr + 1, sc, color, newColor);
        fill(image, sr - 1, sc, color, newColor);
        fill(image, sr, sc + 1, color, newColor);
        fill(image, sr, sc - 1, color, newColor);
    }
}


// Another solution

// BFS


class Solution {
    int[] dr = new int[] {0, 0 , 1, -1};
    int[] dc = new int[] {-1, 1, 0, 0};
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int R = image.length;
        int C = image[0].length;
        
        int oldColor = image[sr][sc];
        if (oldColor == newColor)
            return image;
        Queue<Point> q = new ArrayDeque<Point>();
        q.add(new Point(sr, sc));
        
        while(!q.isEmpty()) {
            Point p = q.poll();
            image[p.x][p.y] = newColor;
            for (int i = 0; i < 4; i++) {
                int x = p.x + dr[i];
                int y = p.y + dc[i];
                if (isValid(image, oldColor, x, y, R, C)) {
                    q.add(new Point(x, y));
                }
            }
        }
        return image;
    }
    
    
     private boolean isValid(int[][] image, int oldColor, int x, int y, int R, int C) {
            if (x >= 0 && x < R && y >= 0 && y < C && image[x][y] == oldColor)
                return true;
         return false;
        }
    
    class Point{
        int x;
        int y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
    }
}



// DFS


class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int o=image[sr][sc];
        helper(image,sr,sc,newColor,o);
        return image;

    }

    void helper(int[][] img,int r,int c,int n,int o) {
        if(r>=img.length || c>=img[0].length || r<0 || c<0 || img[r][c]==n || img[r][c]!=o)   return;
        img[r][c]=n;
        helper(img,r+1,c,n,o);
        helper(img,r-1,c,n,o);
        helper(img,r,c+1,n,o);
        helper(img,r,c-1,n,o);
    }
}




// Another solution


class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if(image[sr][sc] == newColor)
            return image;
        floodFill(image,sr,sc,image[sr][sc],image.length,image[0].length,newColor);
        return image;
    }

    public void floodFill(int[][] image,int cr,int cc,int color,int m,int n,int newColor){

        if(image[cr][cc] != color)
            return;

        image[cr][cc] = newColor;
        if(cr >= 1)
            floodFill(image,cr-1,cc,color,m,n,newColor);
        if(cc < n-1)
            floodFill(image,cr,cc+1,color,m,n,newColor);
        if(cr < m-1)
            floodFill(image,cr+1,cc,color,m,n,newColor);
        if(cc >= 1)
            floodFill(image,cr,cc-1,color,m,n,newColor);
    }
}




// Another



class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int color = image[sr][sc];
        if (color != newColor) dfs(image, sr, sc, color, newColor);
        return image;
    }
    public void dfs(int[][] image, int r, int c, int color, int newColor) {
        if (image[r][c] == color) {
            image[r][c] = newColor;
            if (r >= 1) dfs(image, r-1, c, color, newColor);
            if (c >= 1) dfs(image, r, c-1, color, newColor);
            if (r+1 < image.length) dfs(image, r+1, c, color, newColor);
            if (c+1 < image[0].length) dfs(image, r, c+1, color, newColor);
        }
    }
}
