'''


In this problem we need to generate all possible letter case permutations, 
and let us first underatand how many of them we have. If we have digit, 
we have only 1 option: we need to choose this digit. If we have letter: 
we have 2 options: choose either small or capital letter. 
So, if we have m letters, there will be O(2^m) different solutions. 
When you have a lot of different solutions, it is is a good indicator that it is backtracking problem.

So, let us use dfs(i, built) function, where:

i is current number of symbols we are processing and
built is string built so far.
If we have next symbols which is letter, we need to consider two options, if it is digit, only one.

Complexity is O(2^m*k), where m is number of letters and k is length of all string: 
we have 2^m solutions, each of them has length k, and what is important we never go to deadend, 
so all solutions we are trying to build will be added to final answer. Space complexity is O(2^m*k) as well.


'''

#DFS


class Solution:
    def letterCasePermutation(self, S):
        def dfs(i, built):
            if i == len(S):
                self.ans.append(built)
                return
            if S[i].isalpha():
                dfs(i+1, built + S[i].lower())
            dfs(i+1, built + S[i].upper())
        
        self.ans = []
        dfs(0, "")
        return self.ans
      
      
      
      
# Using product
      
      
# Using product functionality from python: complexity is the same but it can work a bit faster do to low-level optimizations.

class Solution:
    def letterCasePermutation(self, S):
        return map(''.join, product(*[set([i.lower(), i.upper()]) for i in S]))


# Backtracking


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)
                
        res = []
        backtrack()
        return res


      
      
# Iterative

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
        return res
      
      

      
      
'''


Explanation:
For every alphabet in S,
- if it is a number, append it to solution,
- else, append both, lower and upper case

'''


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for i in S:
            if i.isalpha():
                s, u = i.lower(), i.upper()
                n_ans = []
                for e in ans:
                    n_ans.append(e + s)
                    n_ans.append(e + u)
            else:
                n_ans = [e + i for e in ans]
            ans = n_ans
        return ans
      
      
      
      
# same logic but code reduced

class Solution(object):
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for c in S:
            ans = [s+i for i in set([c.upper(), c.lower()]) for s in ans]
        return ans
      
      
      
# same using set

class Solution(object):
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for c in S:
            ans = [s+i for i in set([c.upper(), c.lower()]) for s in ans]

        return ans
      
      
      
      
# concise code


class Solution:
    def letterCasePermutation(self, S):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res
      
      
# Another

class Solution(object):
    def letterCasePermutation(self, S):
        L = [set([i.lower(), i.upper()]) for i in S]
        return map(''.join, itertools.product(*L))
      
      
      
