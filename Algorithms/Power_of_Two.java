/*


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



*/


class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<=0)
            return false;
        return ((n&(n-1))==0);
    }
}


// Iterative


class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n==0)
            return false;
        while(n!=1)
        {
            if(n%2!=0)
                return false;
            n = n/2;
        }
        return true;
    }
}




// Recursive

class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n==1)
            return true;
        if(n%2!=0 || n==0)
            return false;
        return isPowerOfTwo(n/2);
    }
}



// Bitwise Solution

class Solution {
    public boolean isPowerOfTwo(int n) {
        int count=0; 
        while(n>0)
        {
            if((n & 1) == 1)
                count++;
            n = n >> 1;
        }
        return count == 1 ? true : false;
    }
}


// One Liner 

public class Solution {
    public boolean isPowerOfTwo(int n) {
        return ((n & n - 1) == 0 && n > 0);
    }
}


