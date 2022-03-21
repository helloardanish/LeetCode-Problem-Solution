'''


Brute-Force

Let's try solving with brute-force approach. For each house, we have two choices -

Dont rob the house and move to next house.
Rob the house and move to the house after next house (We dont move directly to next house because we can rob adjacent houses).
So, we will just try with both these choices and choose the one the yields the maximum amount of loot.



Time Complexity : O(2N), where N is the number of elements in A. 
At each index, we have two choices of either robbing or not robbing the current house. 
Thus this leads to time complexity of 2*2*2...n times ≈ O(2N)

Space Complexity : O(N), required by implicit recursive stack. The max depth of recursion can go upto N.



'''

class Solution:
    def rob(self, A, i = 0):
        return max(self.rob(A, i+1), A[i] + self.rob(A, i+2)) if i < len(A) else 0



      
      
      
      
      
'''


Nice and easy dynamic programming problem! Let dp1 be maximum gain we can get, using last i-1 houses and dp2 maximum gain we can get, 
using i houses. How we need to update these numbers if we go from i to i+1? So dp1 and dp2 should mean gain for i and i+1 houses.

dp1 = dp2, gain to rob i+1-1 houses is gain to rob i houses.
dp2 = max(dp1 + num, dp2): we have 2 choices: either rob house number i+1, then we can rob ith house, 
so we have total gain dp1 + num, or we do not rob i+1th house, then we can gain dp2.


Complexity: time complexity is O(n), space complexity is O(1).


'''


class Solution:
    def rob(self, nums):
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)          
        return dp2
      
'''


Dynamic Programming - Memoization

In the above solution, we were performing many redundant repeated computations. 
This can be observed by drawing out the recursive tree for above function and observing that rob(i) is called multiple times. 
But rob(i) is nothing but the maximum amount of loot we can get starting at index i and this amount remains the same at each call.

So, instead of re-computing multiple times, 
we can store the result of a function call and directly reuse it on future calls instead of recomputing from scratch. 
This calls for dynamic programming, or memoization to be more specific. 
Here, we can use a linear dp array where dp[i] will denote the maximum amount of loot we can get starting at i index. 
Initially all elements of dp are initialized to -1 denoting they haven't been computed yet, 
Each time, we will save the computed result in this dp for an index i and directly return it if a future call is made to this index.



Time Complexity : O(N), We calculate the result for each index only once & there are N indices. 
Thus overall time complexity is O(N).

Space Complexity : O(N), required for dp and implicit recursive stack.



'''


class Solution:
    def rob(self, A):
        def rob(i):
            return max(rob(i+1), A[i] + rob(i+2)) if i < len(A) else 0
        return rob(0)



'''


Dynamic Programming - Tabulation


We can implement the same logic as above in an iterate approach as well. 
Here, we again use a dp array to save the results of computation. 
In this case, dp[i] will denote maximum loot that we can get by considering till ith index. 

At every index,
  We can keep same loot as we had at previous index - dp[i-1]
  Or, we can rob the current house and add it to the loot we have at i-2th index - A[i] + dp[i-2]




Time Complexity : O(N), just single iteration is performed from 2 to N to compute each dp[i].
Space Complexity : O(N), required for dp.


'''



class Solution:
    def rob(self, A):
        if len(A) == 1: return A[0]
        dp = [*A]
        dp[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])
        return dp[-1]


      
      
      
'''


Space-Optimzed Dynamic Programming


We can observe that the above dp solution relied only on the previous two indices in dp to compute the value of current dp[i]. 
So, we dont really need to maintain the whole dp array and can instead just maintain the values of previous index (denoted as prev below) 
and previous-to-previous index (denoted as prev2) and we can calculate the value for current index (cur) using just these two variables and roll-forward each time.


Time Complexity : O(N)
Space Complexity : O(1), only constant extra space is used.


'''


class Solution:
    def rob(self, A):
        prev2, prev, cur = 0,0,0
        for i in A:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur






'''


Based on the recursive formula:

f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )


'''


class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
      
      
# with explanation


class Solution(object):
  def rob(self, nums):
    # Base Case: nums[0] = nums[0]
    # nums[1] = max(nums[0], nums[1])
    # nums[k] = max(k + nums[k-2], nums[k-1])
    '''
    # Approach 1:- Construct dp table
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
      dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[-1] # return the last element
    '''
    
    # Approach 2:- Constant space use two variables and compute the max respectively
    prev = curr = 0
    for num in nums:
      temp = prev # This represents the nums[i-2]th value
      prev = curr # This represents the nums[i-1]th value
      curr = max(num + temp, prev) # Here we just plug into the formula
      
      # above 3 line can be written in 1 line like this >>>>>>>>>   prev, curr = curr, max(NUM + prev, curr)
    return curr
  
  

  
  
  
# Bottom up DP
  
class Solution:
  def rob(self, nums: List[int]) -> int:
      n = len(nums)
      if n == 1: return nums[0]
      dp = [0] * n
      dp[0] = nums[0]
      dp[1] = max(nums[0], nums[1])
      for i in range(2, len(nums)):
          dp[i] = max(dp[i-1], dp[i-2] + nums[i])
      return dp[n-1]

'''      
Complexity:

Time: O(N), where N <= 100 is number of houses.
Space: O(N)
'''




# Bottom up DP (Space Optimzed)


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp, dp1, dp2 = 0, 0, 0
        for i in range(len(nums)):
            dp = max(dp1, dp2 + nums[i])
            dp2 = dp1
            dp1 = dp
        return dp1
      
      
'''


Complexity:

Time: O(N), where N <= 100 is number of houses.
Space: O(1)


'''



# using isslice

from itertools import islice

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        nums.append(0)
        nums.reverse()
        for idx, num in enumerate(islice(nums, 3, None), 3):
            nums[idx] = max(num + nums[idx - 2], num + nums[idx - 3])
            
        return max(nums[-1], nums[-2])
      
      

      
# Rolling window  -  Botom up

class Solution:
    def rob(self, nums: List[int]) -> int:        
        house_1 = 0
        house_2 = 0
        house_3 = 0
        for num in reversed(nums):
            temp = house_1
            house_1 = max(num + house_2, num + house_3)
            house_3 = house_2
            house_2 = temp
            
        return max(house_1, house_2)
      
      
      
      
      
# Rolling window  -  Top down
      
      
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
            
        return prev1



            



# another solution


class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        # DP O(n) time, O(1) space
        # ik: max include house k
        # ek: max exclude house k, (Note: ek is also the maximum for house 1,...,k-1)
        # i[k+1]: num[k] + ek #can't include house k
        # e[k+1]: max(ik, ek) # can either include house k or exclude house k
        i, e = 0, 0
        for n in num: #from k-1 to k
            i, e = n+e, max(i,e)
        return max(i,e)
      
      

      
# concise solution


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        l = r = 0
        for n in nums:
            l, r = r, max(n + l, r)
        return r
