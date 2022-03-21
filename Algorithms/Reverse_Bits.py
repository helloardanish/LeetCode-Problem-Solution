'''



We are asked to reverse bits in our number. What is the most logical way to do it? 
Create number out, process original number bit by bit from end and 
add this bit to the end of our out number, and that is all! Why it is works?

out = (out << 1)^(n & 1) adds last bit of n to out
n >>= 1 removes last bit from n.
Imagine number n = 11011010, and out = 0

out = 0, n = 1101101
out = 01, n = 110110
out = 010, n = 11011
out = 0101, n = 1101
out = 01011, n = 110
out = 010110, n = 11
out = 0101101, n = 1
out = 01011011, n = 0
Compexity: time complexity is O(32), space complexity is O(1).




'''


class Solution:
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out
      
      

      
      

# Bit manipulation

def reverseBits(self, n):
    ans = 0
    for i in xrange(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    return ans
  
  
  
  
  
  
'''

One pass for just 16 times.
Swapping the bit and or them into a new number.

'''

class Solution:
    def reverseBits(self, n):
        ret = 0
        for i in range(16):
            right_bit = (n>>i)&1
            left_bit = (n>>(31-i))&1
            ret |= right_bit<<(31-i)
            ret |= left_bit<<i
        return ret
      
      

      
      
      
      
'''


Divide and Conquer!  Someway like merge sort.
For example, if there are 8 bit binary number abcdefgh,
the process is as follow:
abcdefgh -> efghabcd -> ghefcdab -> hgfedcba


'''

class Solution:
    def reverseBits(self, n):
        # For python, there is no 32bit int, so we need to force it 32 bits.
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) & 0xffffffff
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) & 0xffffffff
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) & 0xffffffff
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) & 0xffffffff
        return n

      
      
  
  
  
      
# Compress the four lines into one

class Solution:
    def reverseBits(self, n):
        ret = 0
        for i in range(16):
            ret |= ((n>>i)&1)<<(31-i) | ((n>>(31-i))&1)<<i
        return ret
      
      
      
      
# minimised solution


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
      
      
      
# string manipulation, slicing


class Solution:
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)
      
      

      
      
