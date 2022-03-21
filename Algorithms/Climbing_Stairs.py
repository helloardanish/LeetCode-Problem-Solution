'''


Variable a tells you the number of ways to reach the current step, 
and b tells you the number of ways to reach the next step. 
So for the situation one step further up, the old b becomes the new a, 
and the new b is the old a+b, 
since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.


'''


class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
      
      
      
      
# Top down - TLE
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
 
# Bottom up, O(n) space
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]

# Bottom up, constant space
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b
    
# Top down + memorization (list)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n-1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
        return dic[n]
    
# Top down + memorization (dictionary)  
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]
      
      
      
      
# Using dp


class Solution:
    def climbStairs(self, n):
        #edge cases
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]
      
      
# dp concise code


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,1]
        for i in range(2,n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]
