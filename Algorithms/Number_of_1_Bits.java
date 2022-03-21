/*


An Integer in Java has 32 bits, e.g. 00101000011110010100001000011010.
To count the 1s in the Integer representation we put the input int
n in bit AND with 1 (that is represented as
00000000000000000000000000000001, and if this operation result is 1,
that means that the last bit of the input integer is 1. Thus we add it to the 1s count.
ones = ones + (n & 1);

Then we shift the input Integer by one on the right, to check for the
next bit.
n = n>>>1;

We need to use bit shifting unsigned operation >>> (while >> depends on sign extension)

We keep doing this until the input Integer is 0.
In Java we need to put attention on the fact that the maximum integer is 2147483647. 
Integer type in Java is signed and there is no unsigned int. 
So the input 2147483648 is represented in Java as -2147483648 (in java int type has a cyclic representation, 
that means Integer.MAX_VALUE+1==Integer.MIN_VALUE).
This force us to use

n!=0



*/

public class Solution {
    public static int hammingWeight(int n) {
        int ones = 0;
            while(n!=0) {
                ones = ones + (n & 1);
                n = n>>>1;
            }
            return ones;
    }
}




/* More explanation

Why can't we use n > 0?
The binary representation of Integer.MAX_VALUE is 0111 1111 1111 1111 1111 1111 1111 1111, and
the binary representation of Integer.MAX_VALUE + 1 is 1000 0000 0000 0000 0000 0000 0000 0000 (spaces added).
Note that the leftmost bit here denotes the sign of the number, but recall that we're told to treat input as unsigned.

As mentioned above, Integer.MAX_VALUE is 2147483647, and Integer.MAX_VALUE + 1 is -2147483648.

Intuitively, we would agree that -2147483648 has 1 one.

However, if our test is n > 0, -2147483648 fails that test, so we don't count any 1s, and instead incorrectly return 0.

Why can't we use n >>= 1?
The assumption of this code is that, starting with a 32-bit binary number, we can move the bits over to the right, filling in zeros from the left.

So a few shifts of Integer.MAX_VALUE + 1 should look like this:
0100 0000 0000 0000 0000 0000 0000 0000
0010 0000 0000 0000 0000 0000 0000 0000
0001 0000 0000 0000 0000 0000 0000 0000

The operation that describes that kind of shift is the unsigned shift (also "logical shift") operator, denoted by >>>.

The operation denoted by >> is indeed also a shift (the "signed" or "arithmetic" shift), 
but not the shift we're looking for (since it fills in whatever the sign bit is, either 0 or 1)

A few shifts of Integer.MAX_VALUE + 1 using the >> operator would look like this:
1100 0000 0000 0000 0000 0000 0000 0000
1110 0000 0000 0000 0000 0000 0000 0000
1111 0000 0000 0000 0000 0000 0000 0000
1111 1000 0000 0000 0000 0000 0000 0000
...
1111 1111 1111 1111 1111 1111 1111 1111, to infinity, which would never exit our n != 0 condition.

*/







// Another solution


/*


The best solution for this problem is to use "divide and conquer" to count bits:

First, count adjacent two bits, the results are stored separatedly into two bit spaces;
Second is to count the results from each of the previous two bits and store results to four bit spaces;
Repeat those steps and the final result will be sumed.


*/


class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        n = n - ((n >>> 1) & 0x55555555);
        n = (n & 0x33333333) + ((n >>> 2) & 0x33333333);
        n = (n + (n >>> 4)) & 0x0f0f0f0f;
        n = n + (n >>> 8);
        n = n + (n >>> 16);
        return n & 0x3f;
    }
}



// Iterative


class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        for(int i=0; i<32; i++){
            count += (n >> i & 1) == 1 ? 1: 0;
        }
        return count;
    }
}


// reduced code from above

class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        for(int i = 0; i < 32; i++){
            count += (n >> i & 1);
        }
        return count;
    }
}




// another solution



/*

Using Brian Kernighan Algorithm, we will not check/compare or loop through all the 32 bits present but 
only count the set bits which is way better than checking all the 32 bits
Suppose we have a number 00000000000000000000000000010110 (32 bits), 
now using this algorithm we will skip the 0's bit and directly jump to set bit(1's bit) 
and we don't have to go through each bit to count set bits i.e. 
the loop will be executed only for 3 times for the mentioned example and not for 32 times.


COMPLEXITY:

  Time: O(log2n), where n is the given number
  Space: O(1), in-place


*/


public class Solution {
 
    public int hammingWeight(int n) {
        
		int setBitCount = 0;
        
		while (n != 0) {
            n &= (n - 1); // to clear the right most set bit
            ++setBitCount;
        }
		
        return setBitCount;
    }
}



// Another solution

class Solution {
    public int hammingWeight(int n) {
        int result = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                result++;
            }
            n >>>= 1;
        }
        return result;
    }
}

// Using for loop in above solution

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        for(int i = 0; i < 32; i++){  
            if ((n & 1) == 1) count++;
            n >>= 1;
        }
        return count;
    }
}



// Bit shifting

class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        for(int i = 0; i < 32; i++) {
            if(((1 << i) & n) != 0) {
                count++;
            }
        }
        return count;
    }
}




// Another solution


public class Solution {
 
    public int hammingWeight(int n) {
        
		int setBitCount = 0;
        
		while (n != 0) {
            n &= (n - 1); // to clear the right most set bit
            ++setBitCount;
        }
		
        return setBitCount;
    }
}





// Builtin method

public class Solution {
    public int hammingWeight(int n) {
        return Integer.bitCount(n);
    }
}
