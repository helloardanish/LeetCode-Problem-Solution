'''


It is very tempting in Python just to use reverse() function, but I think it is not fully honest solution.
Instead, we go from the start and the end of the string and swap pair of elements. One thing, that we need to do is to stop at the middle of our string. We can see this as simplified version of two points approach, because each step we increase one of them and decrease another.

Complexity: Time complexity is O(n) and additional space is O(1).

'''


class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]
          
          
###### Using bitwise

class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]
          
          
          
### Other solutions


# we dont need to return, so a simple simple swapping operation will do the job
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        i , j = 0 , n-1
        
        while i<j:
            
            s[i] = ord(s[i])     # converting from char to int
            s[j] = ord(s[j])
            
            s[i]^=s[j]           # swapping operation inplace
            s[j]^=s[i]
            s[i]^=s[j]
            
            s[i] = chr(s[i])     # converting back to char
            s[j] = chr(s[j])
            
            i+=1                   # updating pointers
            j-=1
            
            
################ Using recursion ###################


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        n=len(s)
        return self.reverseString(s[n//2:])+self.reverseString(s[:n//2])
            
            
            
################ One-liner solution #######################


class Solution:
    def reverseString(self, s):
        s[:] = s[::-1]
        

        
class Solution:
    def reverseString(self, s):
        s.reverse()
        
        
        
    
