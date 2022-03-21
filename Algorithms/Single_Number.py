'''


Edge Cases:
No element appears twice; it is a constraint so not possible
Single length array; return the only element already present in the array
len(nums) > 1; find the single element that does not appear twice


Approaches:


Brute Force
Intuition:
Iterate through every element in the nums and check if any of the element does not appear twice, in that case return the element.
Time: O(n^2)
Space: O(1)



Use Sorting
Intuition:
If the elements of the nums array are sorted/when we sort it, we can compare the neighbours to find the single element. It is already mentioned that all other elements appear twice except one.
Time: O(nlogn) for sorting then O(n) to check neighbouring elements
Space: O(1)



Use Hashing/Set
Intuition:
i) As we iterate through the nums array we store the elements encountered and check if we find them again while iteration continues. While checking if we find them again, we maintain a single_element object/variable which stores that single element, eventually returning the single_element.
ii) The other way is to maintain a num_frequency hashmap/dictionary and iterate over it to find which has exactly 1 frequency and return that key/num.
Time: O(n) for iterating over the nums array
Space: O(n) for hashing



Use Xor/Bit Manipulation
Intuition:
Xor of any two num gives the difference of bit as 1 and same bit as 0.
Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
Time: O(n)
Space: O(1)



'''


# using Xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
      

# same XOR idea
'''


We use the nice property of XOR operation which is if you XOR same numbers it will return zero. 
Since the nums contains just one non-repeating number, 
we can just XOR all numbers together and the final result will be our answer.


'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
	    return reduce(lambda total, el: total ^ el, nums)
    

    
    
    
    
# another solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : XOR ##
        
        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(1) ##
        
        # If we take XOR of zero and some bit, it will return that bit
        # a XOR 0 = a, a XOR 0=a
        # If we take XOR of two same bits, it will return 0
        # a XOR a = 0 a XOR a=0
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b 
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # So we can XOR all bits together to find the unique number.
        
        a = 0
        for i in nums:
            a ^= i
        return a
    
    
    
    
# minimised code


class Solution:
    def singleNumber(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key
              
              
              
              
# another

class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
      
      
      
# another

class Solution:
    def singleNumber(self, nums):
        return 2*sum(set(nums))-sum(nums)
      

# another


class Solution(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)
      
      
# another

class Solution:
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
      
      
# another

class Solution:
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
      
      
