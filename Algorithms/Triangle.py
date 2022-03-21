'''

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



'''


class Solution:
    def minimumTotal(self, T: List[List[int]]) -> int:
        for i in range(len(T)-2,-1,-1):
            for j in range(len(T[i])-1,-1,-1):
                T[i][j] += min(T[i+1][j], T[i+1][j+1])
        return T[0][0]



'''


In-Place Bottom-Up Dynamic Programming


We can easily see that directly just choosing the minimum value in the next row(amongst triangle[nextRow][i] and triangle[nextRow][i+1]) 
won't fetch us the optimal final result since it maybe the case that the latter values of previous chosen path turn out to be huge.

We need to observe that to get the minimum possible sum, we must use a path that has Optimal Value for each intermediate stop in the path. 
Thus, we can use Dynamic Programming to find the optimal value to reach each position of the triangle level by level. 
We can do this by accumulating the sum of path(or more specifically sum of values of optimal stops in a path) 
for each cell of a level from top to the bottom of triangle.

We are given that, at each cell in the triangle, we can move to the next row using two choices -

Move to the same index i.
Move to the next index i + 1
Since we are following a bottom-up approach, the above can also be interpreted as :-

For cell in the triangle, we could have reached here either from the previous row/level either from -

the same index i, or
the index i - 1
So, obviously the optimal choice to arrive at the current position in triangle would be to come from the cell having minimum value of these two choices.

We will keep adding the result from the lower level to the next/higher level by each time choosing the optimal cell to arrive at the current cell. Finally, we can return the minimum value that we get at the bottom-most row of the triangle. Here, no auxillary space is used and I have modified the triangle itself to achieve a space complexity of O(1).





'''



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(1, len(triangle)):
            for i in range(level+1):
                triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        return min(triangle[-1])
      
      
      
      
      
'''

Time Complexity : O(N^2), where N are the total number of levels in triangle.
Space Complexity : O(1)

The min and max in the above code are used to do bound-checks.

'''





# Another solution

'''

We chose to go from top-level to the bottom-level of triangle in the previous approach. 
We can also choose to start from the bottom of triangle and move all the way to the top. 
We will again follow the same DP strategy as used in the above solution.

At each cell of the triangle, we could have moved here from the below level in 2 ways, either from -

the same index i in below row, or
the index i+1.
And again, we will choose the minimum of these two to arrive at the optimal solution. Finally at last, we will reach at triangle[0][0], which will hold the optimal (minimum) sum of path.

Actually, this approach will make the code a lot more clean and concise by avoiding the need of bound checks.


'''


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(len(triangle)-2,-1,-1):
            for i in range(level+1):
                triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
        return triangle[0][0]
      
      
      
'''


Time Complexity : O(N^2)
Space Complexity : O(1)



'''




'''



Bottom-Up Dynamic Programming w/ Auxillary Space


More often than not, you would not be allowed to modify the given input. In such a situation, 
we can obviously opt for making a copy of the given input(triangle in this case). 
This would lead to a space complexity of O(N^2). 
I won't show this solution since the only change needed in above solutions would be adding the line 
vector<vector<int>>dp(triangle); and replacing triangle with dp (Or better yet just pass triangle by 
value instead of reference & keep using that itself 🤷‍♂️).

Here, I will present a solution with linear space complexity without input modification. 
We can observe in the above solutions that we really ever access only two rows of the input at the same time. 
So, we can just maintain two rows and alternate between those two in our loop.

I have used level & 1 in the below solution to alternate between these two rows of dp. 
It's very common way to go when we are converting from 2d DP to linear space. 
If you are not comfortable with it, 
you can also choose to maintain two separate rows and swap them at end of each iteration.

All the other things and idea remains the same as in the above.



'''



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cur_row, prev_row = [0]*n, [0]*n
        prev_row[0] = triangle[0][0]  
        for level in range(1, n):
            for i in range(level+1):
                cur_row[i] = triangle[level][i] + min(prev_row[min(i, level-1)], prev_row[max(i-1,0)])
            cur_row, prev_row = prev_row, cur_row
        return min(prev_row)


      
      
'''


Time Complexity : O(N^2)
Space Complexity : O(N)


'''





# Top-Down Dynamic Programming w/ Auxillary Space




class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cur_row, next_row = [0]*n, triangle[n-1]        
        for level in range(n-2,-1,-1):
            for i in range(level+1):
                cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i+1])
            cur_row, next_row = next_row, cur_row
        return next_row[0]
      
      
      
      




# In-Place Top-Down Dynamic Programming
   


# top down


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])
      
      
      
# minimised the above code


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
      
      
      
      
# Bottom up


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
      
      
      
# Bottom up minimised


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
      
      

      
      
# Minimised solution


def minimumTotal(self, t):
    return reduce(lambda a,b:[f+min(d,e)for d,e,f in zip(a,a[1:],b)],t[::-1])[0]
  
# expanded version

class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
      
      
      
      
# Recursive


class Solution:
    def minimumTotal(self, triangle):
        self.triangle=triangle
        self.cache=dict()
        return self.recurse(0,0) if triangle else 0

    def recurse(self, level, i):
        if (level,i) in self.cache:
            return self.cache[(level,i)]

        if level==len(self.triangle)-1:
            return self.triangle[level][i]

        res=self.triangle[level][i]+min(self.recurse(level+1, i), self.recurse(level+1, i+1))
        self.cache[(level, i)]=res

        return res
      
      
      
      


      
      

      
# one-liner 

class Solution:
    def minimumTotal(self, triangle):
        return reduce(lambda x, y: [min(x[b], x[b+1])+y[b] for b in range(len(y))], triangle[::-1], [0]*(len(triangle)+1))[0]
      
      
      
# another
      
      
class Solution:
    def minimumTotal(self, triangle):
        triangle.append([0]*(len(triangle)+1))
        return reduce(lambda x, y: [min(x[b], x[b+1])+y[b] for b in range(len(y))], triangle[::-1])[0]
  
  
# another

class Solution:
    def minimumTotal(self, triangle):
        base=[0]*(len(triangle)+1)
        for i in range(len(triangle)-1, -1, -1):
            base=[min(base[b], base[b+1])+triangle[i][b] for b in range(i+1)]
        return base[0]
      
      

      
      
# another

class Solution:
    def minimumTotal(self, triangle):
        for i in reversed(range(len(triangle) - 1)):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
      
      
      
