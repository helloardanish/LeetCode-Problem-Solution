'''


Explaination: If number equals or less than 0 then it cant be any power of 2. Now for positive numbers, 
it should have only one binary bit as 1 (becaus power of 2 will come as 2^0,2^1,2^2.......).

for example,
1 -> 2^0 -> 0000001
2 -> 2^1 -> 0000010
4 -> 2^2 -> 0000100
8 -> 2^3 -> 0001000
16-> 2^4 -> 0010000
....... and so on.


So here we can take a bitwise and (&) operation between the number and a number less than it, 
if it equal to 0 then it means that no other position has high bit, except at one place. 
Thus return true, else false.

for ex: take the number, n=16

n (in bits) -> 1 0 0 0 0 (16 is a power of 2 and thus has only one high bit)
n-1 (in bits) -> 0 1 1 1 1 ( n-1 i.e. 15 will make all bits high excpet the 5th bit)
n & n-1 -> 0 0 0 0 0 (& operation will make all the bits to 0, thus its power of 2)


'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<=0):
            return False
        return ((n&(n-1))==0);
      


'''

This is classical bit manipulation problem for n & (n-1) trick, which removes the last non-zero bit from our number

example:
1.n = 100000, then n - 1 = 011111 and n & (n-1) = 000000, so if it is power of two, result is zero
2.n = 101110, then n - 1 = 101101 and n & (n-1) = 101100, number is not power of two and result is not zero.

'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n&n-1 if n else False
      
# another O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0
      
# another O(n)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and sum(list(map(int,bin(n)[2:])))==1
      
      
'''


O(1) above Explanation:

It's figuring out if n is either 0 or an exact power of two.

It works because a binary power of two is of the form 1000...000 and subtracting one will give you 111...111. Then, when you AND those together, you get zero, such as with:

  1000 0000 0000 0000
&  111 1111 1111 1111
  ==== ==== ==== ====
= 0000 0000 0000 0000
Any non-power-of-two input value (other than zero) will not give you zero when you perform that operation.

For example, let's try all the 4-bit combinations:

     <----- binary ---->
 n      n    n-1   n&(n-1)
--   ----   ----   -------
 0   0000   0111    0000 *
 1   0001   0000    0000 *
 2   0010   0001    0000 *
 3   0011   0010    0010
 4   0100   0011    0000 *
 5   0101   0100    0100
 6   0110   0101    0100
 7   0111   0110    0110
 8   1000   0111    0000 *
 9   1001   1000    1000
10   1010   1001    1000
11   1011   1010    1010
12   1100   1011    1000
13   1101   1100    1100
14   1110   1101    1100
15   1111   1110    1110
You can see that only 0 and the powers of two (1, 2, 4 and 8) result in a 0000/false bit pattern, all others are non-zero or true.


'''
