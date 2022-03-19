'''


The idea is simple. Simply perform a DFS on the source cell. Continue the DFS if:

Next cell is within bounds.
Next cell is the same color as source cell.
There is a tricky case where the new color is the same as the original color and if the DFS is done on it, 
there will be an infinite loop. If new color is same as original color, 
there is nothing to be done and we can simply return the image.



'''


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != newColor:
            traverse(sr, sc)
        return image
      
      
      
################## Another solution  ##################


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r, c = len(image), len(image[0])
        color = image[sr][sc]
        def dfs(i, j):
            if i < 0 or i>=r or j < 0 or j >= c:
                return
            if image[i][j] == newColor or image[i][j] != color:
                return
            image[i][j] = newColor
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i,j+1)
            dfs(i, j-1)
        dfs(sr, sc)
        return image
        
        
        

#################       BFS        ###########################


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image
      
      
      
####################      DFS          ###########################


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            dfs(sr, sc)
        return image
      
      
      
      
############## Minimum liners #####################


def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    """ O(N*M)TS in place """

    def fn(y, x, color):
        if 0 <= y < len(image) and 0 <= x < len(image[0]) and image[y][x] == color:
            image[y][x] = newColor
            fn(y + 1, x, color), fn(y - 1, x, color), fn(y, x + 1, color), fn(y, x - 1, color)

    return (fn(sr, sc, image[sr][sc]) or image) if image[sr][sc] != newColor else image

  
  
  
#### Another solution



class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
      
