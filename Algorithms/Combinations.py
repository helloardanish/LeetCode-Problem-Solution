'''


First the obvious solution - Python already provides this functionality and it's not forbidden, 
so let's take advantage of it.


'''

from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))
      
      
      
# recursive

class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]


      
# iterative

class Solution:
    def combine(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs
      
      
# same as iterative but using reduce instead of loops

class Solution:
    def combine(self, n, k):
        return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                      range(k), [[]])
      

      
      
# Recursive with extra method

class Solution(object):
    def combine(self, n, k):
        res = []
        self.dfs(range(1,n+1), k, 0, [], res)
        return res
    def dfs(self, nums, k, index, path, res):
        if k == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)

      
      
# backtracking iterative


class Solution(object):
    def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
                
                
                
      
      
# Recursive


class Solution(object):
    def combine(self, n, k):
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            rs=[]
            rs+=self.combine(n-1,k)
            part=self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            rs+=part
            return rs
          
          
          
      
      
# DFS

class Solution(object):
    def combine(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], ret)
            
            

## same as above a minor tweaks

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k, res, [], 1)
        return res
    
    def backtrack(self, n, k, res, path, index):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n+1):
            self.backtrack(n, k, res, path+[i], i+1)
            
            
            
