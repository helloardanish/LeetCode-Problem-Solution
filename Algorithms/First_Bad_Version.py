####################### One Solution #########################

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in reversed(range(0,n)):
            if isBadVersion(i)==False:
                return i+1;
                
### Time limit exceeds
                
                
####################### Use divide and conqueror like merge sort to minimise the time #########################

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        while isBadVersion(n/2)==True:
            n = n//2;
        for i in reversed(range(n//2,n)):
            if isBadVersion(i)==False:
                return i+1;
        
###  Still time limit exceeds


############### Because pervious isn't well implemented for large numbers:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution(object):
    def firstBadVersion(self, n):
        
        l,r = 0, n
        while l <=r:
            m = (l+r)//2
            if isBadVersion(m-1) == False and isBadVersion(m)== True:
                return m
            else:
                if isBadVersion(m) == False:
                    l = m +1
                else:
                    r = m -1
        return -1

############## Different sol ##############################33

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, u = 1, n
        while l<=u:
            mid = l + (u- l)//2
            if isBadVersion(mid) :
                u = mid - 1
                res = mid
            else:
                l = mid + 1
        return res
