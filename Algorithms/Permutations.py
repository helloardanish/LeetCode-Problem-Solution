'''

Iterative


The basic idea is, to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, 
in every possible position.
For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>> (let's call it "answer").
Then, 2 can be added in front or after 1. So we have to copy the List in answer (it's just {1}), add 2 in position 0 of {1}, 
then copy the original {1} again, and add 2 in position 1. Now we have an answer of {{2,1},{1,2}}. 
There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, and add 3 into position 1, 
then do the same thing for position 3. Finally we have 2*3=6 lists in answer, which is what we want.


'''


def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms






# DFS
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
        
# For visualization

dfs(nums = [1, 2, 3] , path = [] , result = [] )
|____ dfs(nums = [2, 3] , path = [1] , result = [] )
|      |___dfs(nums = [3] , path = [1, 2] , result = [] )
|      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
|           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
|____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
|      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
|      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
|           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
|____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
       |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
            |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
        
        
        

        
        
        
# Recursive

class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]
            other_permutations = self.permute(others)
            for permutation in other_permutations:
                result.append([nums[i]] + permutation)
        return result
      
      

# backtracking

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ans = []
        
        def bt(i):
            if i == n:
                self.ans.append(deepcopy(nums))
                return
            
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                bt(i+1)
                nums[i], nums[j] = nums[j], nums[i]
                
        bt(0)
        return self.ans

'''

Complexity

Time: O(N!)
Space: O(N!)
'''        
   

# Easy recursion


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
		
		# Base conditions
		# If length is 0 or 1, there is only 1 permutation
        if n in [0, 1]:
            return [nums]
		
		# If length is 2, then there are only two permutations
		# Example: [1,2] and [2,1]
        if n == 2:
            return [nums, nums[::-1]]
			
        res = []
		# For every number in array, choose 1 number and permute the remaining
		# by calling permute recursively
        for i in range(n):
            permutations = self.permute(nums[:i] + nums[i+1:])
            for p in permutations:
                res.append([nums[i]] + p)
				
        return res
      
      

        
# Recursive, take any number as first
# Take any number as the first number and append any permutation of the other numbers.

class Solution:
    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
      
      
      
# Recursive, insert first number anywhere
# Insert the first number anywhere in any permutation of the remaining numbers.


class Solution:
    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]
      
      
# Reduce, insert next number anywhere
# Use reduce to insert the next number anywhere in the already built permutations.


class Solution:
    def permute(self, nums):
        return reduce(lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in range(len(p)+1)], nums, [[]])


# Using the permutations library

class Solution:
    def permute(self, nums):
        return list(itertools.permutations(nums))
      
# It returns a list of tuples, but the OJ accepts it anyway. If needed, I could easily turn it into a list of lists:

class Solution:
    def permute(self, nums):
        return map(list, itertools.permutations(nums))
      

