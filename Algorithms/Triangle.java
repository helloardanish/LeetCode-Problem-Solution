/*


Idea:


In order to find the best path from the top of the input triangle array (T) to the bottom, 
we should be able to find the best path to any intermediate spot along that path, as well. 
That should immediately bring to mind a dynamic programming (DP) solution, 
as we can divide this solution up into smaller pieces and then build those up to our eventual solution.


The naive idea here might be to do a bottom-up DP approach (which is actually from the start of the path, 
or the top of T, to the end of the path, or the bottom of T), since that reflects the normal path progression and branching. 
If we do this, however, we'll need to write extra code to avoid going out-of-bounds when checking the previously completed rows of the DP array. 
We'll also have to then check the entire bottom row of our DP array to find the best value.

If we use a top-down DP approach (visually bottom to top of T), however, 
we can avoid having to check for out-of-bounds conditions, as we'll be going from larger rows to smaller rows. 
Also, we won't need to search for the best solution, because it will automatically be isolated in T[0][0].

Furthermore, since we'll never need to backtrack to previous rows, we can use T as its own in-place DP array, 
updating the values as we go, in order to achieve a space complexity of O(1) extra space.

In order to accomplish this, we'll just need to iterate backwards through the rows, starting from the second to the last, 
and figure out what the best path to the bottom would be from each location in the row. 
Since the values in the row below will already represent the best path from that point, 
we can just add the lower of the two possible branches to the current location (T[i][j]) at each iteration.

Once we're done, we can simply return T[0][0].



Implementation:

For Java, using an in-place DP approach, while saving on space complexity, is significantly less performant than using an O(N) DP array.


*/



class Solution {
    public int minimumTotal(List<List<Integer>> T) {
        for (int i = T.size() - 2; i >= 0; i--) 
            for (int j = T.get(i).size() - 1; j >= 0; j--) {
                int min = Math.min(T.get(i+1).get(j), T.get(i+1).get(j+1));
                T.get(i).set(j, T.get(i).get(j) + min);
            }
        return T.get(0).get(0);
    }
}



// DP

public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for(int i = triangle.size() - 2; i >= 0; i--)
            for(int j = 0; j <= i; j++)
                triangle.get(i).set(j, triangle.get(i).get(j) + Math.min(triangle.get(i + 1).get(j), triangle.get(i + 1).get(j + 1)));
        return triangle.get(0).get(0);
    }
}






// Another solution


class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[] A = new int[triangle.size()+1];
        for(int i=triangle.size()-1;i>=0;i--){
            for(int j=0;j<triangle.get(i).size();j++){
                A[j] = Math.min(A[j],A[j+1])+triangle.get(i).get(j);
            }
        }
        return A[0];
    }
}







// Another solution


//Recursive

public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) return 0;
           return dfs(0, 0, triangle);
       }

       int dfs(int row, int pos, List<List<Integer>> triangle){
           //Out of bounds so just return sum previous value must be leaf node
           if (row+1 >= triangle.size()) return triangle.get(row).get(pos);

         return  triangle.get(row).get(pos) + Math.min (dfs(row+1, pos,triangle), dfs(row+1, pos+1, triangle));

      }
}




//Top down


public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) return 0;
        Integer[][] cache = new Integer[triangle.size()][triangle.size()];
        return dfs(0, 0,triangle, cache);
    }
    
    
    int dfs(int row, int pos, List<List<Integer>> triangle, Integer[][] cache){
        //Out of bounds so just return sum previous value must be leaf node
        if (row+1 >= triangle.size()) {
            return triangle.get(row).get(pos); 
        }
        if(cache[row][pos] != null) return cache[row][pos];
        
      cache[row][pos] =  triangle.get(row).get(pos) + Math.min ( dfs(row+1, pos,triangle, cache), dfs(row+1, pos+1,triangle, cache));
        
        return cache[row][pos];
        
    }
}





//Bottom up

public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[][]dp = new int[triangle.size()][triangle.size()];
        //Remember base case is just returning leaf nodes
        for (int i = 0; i < triangle.size(); i++){
            dp[triangle.size()-1][i] = triangle.get(triangle.size()-1).get(i);
        }

        for (int row = triangle.size()-2; row >= 0; row--){
            for (int pos = 0; pos < triangle.get(row).size(); pos++){
                dp[row][pos] = triangle.get(row).get(pos) + Math.min(dp[row+1][pos+1], dp[row+1][pos]);
            }
        }

        return dp[0][0];
    }
}





//Bottom up O(n) space complexity.
class Solution {
  public int minimumTotal(List<List<Integer>> triangle) {

      int[]dp = new int[triangle.size()];
      int[]dp1 = new int[triangle.size()];
      //Remember base case is just returning leaf nodes
      for (int i = 0; i < triangle.size(); i++){
          dp[i] = triangle.get(triangle.size()-1).get(i);
      }

      for (int row = triangle.size()-2; row >= 0; row--){
          for (int pos = 0; pos < triangle.get(row).size(); pos++){
              dp1[pos] = triangle.get(row).get(pos) + Math.min(dp[pos+1], dp[pos]);
          }
          dp = dp1;
      }

      return dp[0];
  }
}




// Another solution



public class Solution {
    public int minimumTotal(List<List<Integer>> trgl) {
        int sz = trgl.size();
        int[] results = new int[sz+1];

        for(int i=sz-1; i>=0; i--) {
            List<Integer> tmp = trgl.get(i);

            for(int j=0; j<tmp.size(); j++) {
                results[j] = Math.min(results[j], results[j+1]) + tmp.get(j);
            }
        }
        return results[0];
    }
}







// Recursion

class Solution {
    Integer[][]c;
    public int minimumTotal(List<List<Integer>> triangle) {
        c=new Integer[triangle.size()][triangle.size()];
        return triangle.get(0).get(0)
+dfs(0,triangle,1);        
    }
    public int dfs(int index,List<List<Integer>> triangle,int level){
        if(level==triangle.size()) return 0;
        if(c[level][index]!=null) return c[level][index];
        int left=triangle.get(level).get(index)+dfs(index,triangle,level+1);
        int right=triangle.get(level).get(index+1)+dfs(index+1,triangle,level+1);
        return c[level][index]=Math.min(left,right);
    }
}



