# Built in solution with built-in function:

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
      
      
      
      
      
'''

Using bit operation to cancel a 1 in each round

Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. 
n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1

'''

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
      
      
# Recursively

class Solution:
    def hammingWeight(self, n, count=0):
        return self.hammingWeight(n & n-1, count+1) if n!=0 else count

      
      
      
'''


Explanation:
Use bitwise operations:

&1 returns 1 if the last bit of the result of n>>i == 1, else 0
By using n>>i, we shift the bits to the right by i places
this way, every bit of n is the 'last bit' of n>>i at one point
sum up the number of 1s that we found that way


'''

def hammingWeight(self, n: int) -> int:
        return sum((n>>i&1 for i in range(32)))
  
  
