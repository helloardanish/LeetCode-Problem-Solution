'''


EXPLANATION:-
  In this problem, we need to find a substring in s2
  that is permuation of s1.
  
  Permutation means re-arranging the letters of s1.
  
  In other words, we can say that we need to 
  find an anagram of s1 in s2.
  
  First of all, What is anagram?
       A string s is angram of p, if it satisfies the following conditions,
	   1. s should contain all the characters in p.
	   2. Frequency of each character should be same in two strings.
  
  Now, we need to find anagram of s1 in s2.
  
  How to find?.
  This can be done by finding all the substrings of length same as s1
  and check that substring is anagram or not.
  If it is anagram, then return true.
  otherwise check next substring.
  
  Let's see how to solve this problem using an example.
  
  Take,  s1 = ab,  s2 = eioubab 
  find all substrings of length 2 in s2.
  
  substrings = [ ei , io, ou, ub, ba, ab ]
  from these substrings, find anagram
  
  1. ei -> it is not anagram of s1. Because e and i are not in s1.
  2. io -> it is not anagram of s1. Because e is not in s1.
  3. ou -> it is not anagram of s1. Because o is not in s1.
  4. ub -> it is not anagram of s1. Because u is not in s1.
  5. ba -> It is anagram of s1. So, return true.
      Correctness :- Is this correct? Is ba permutation of ab?
	  -> Yes. if we re-arrange letters in ab. we will get ba.
	      So, it is correct.

If you don't find any anagram, then return false.

Now, let's develop an algorithm to solve this problem.

1. Find frequency of each character in s1.
2. Now, we need to find all substrings of length s1 in s2.
    This process can be efficiently done by using sliding window technique.
	Sliding Window Technique:-
	s2 = dbcad, s1 = abc
	Take two pointers i and j. 
	Intially i and j point to starting position of string s. 
	s = d  b  c  a  d
        ^
	   i, j
	->  move j until j - i == len(p)
	s = d  b  c  a  d
        ^        ^
        i        j
	Now, the substring formed here is  dbc, 
	it is not anagram so, move to next substring.
	s = d  b  c  a  d
           ^     ^
           i     j
   Now, j at 3rd index, i at 1st index.
   3 - 1 < 3
   so, move j until j - i == len(p)
   s = d  b  c  a  d
          ^        ^
          i        j
    Now, substring formed here is bca.
	It is anagram. So, return true.
	We keep moving i and j until j reaches end of s2.
	This is how we find substring using sliding window technique.
 	and check whether it is anagram or not.
	if it is anagram, return true.
3. If you don't find anagram, then return false.

TIME:- O(N)
SPACE:- O(1)  



'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = [0] * 26
        for c in s1:
            mapp[ord(c) - 97] += 1
        i, j, count_chars = 0, 0, len(s1)
        while j < len(s2):
            if mapp[ord(s2[j]) - 97] > 0:   
                count_chars -= 1
            mapp[ord(s2[j]) - 97] -= 1
            j += 1
            if count_chars == 0:
                return True
            if j - i == len(s1):
                if mapp[ord(s2[i]) - 97] >= 0:
                    count_chars += 1
                mapp[ord(s2[i]) - 97] += 1
                i += 1
                
        return False
      
      
      
      

############### Hashmap ###################


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1=Counter(s1)
        n=len(s1)
        
        for i in range(len(s2)-len(s1)+1):
            h2 = Counter(s2[i:i+n])
            if h1==h2:
                return True
        return False
      
      
      
'''

Sliding window :


Sort the target_string (which is s1).
The window size is the size of the target_string (which is the size of s1).
The "window" is the current substring of the string.
Slide the window through the entire string.
For each iteration (or sliding of the window), sort the current substring and check if it matches the target_string.
If the sorted substring equals the target_string, then return True.
After sliding the window through the entire string, if no match is found, return False.


'''

class Solution:
    def checkInclusion(self, target_string: str, string: str) -> bool:
        
        target_string = ''.join(sorted(target_string))
        current_string = ''
        
        for char in string:
            
            # increase the window (equivalent to adding the next character to current string)
            current_string += char
            
            # start doing business once the window size is size of target_string
            if len(current_string) == len(target_string):
                
                # sort the current string and check if it equals the target_string
                if ''.join(sorted(current_string)) == target_string:
                    return True
                
                # shrink the window for next iteration (remove the leftmost character)
                current_string = current_string[1:]
        
        # we couldn't find a permutation in the string, return False
        return False
      
      
      
      
'''



Let us use sliding window, where we count frequencies of each letter. 
We can just remove old letter and add new one and check if frequencies are what we need in O(26) for each step, 
then we have O(26n) complexity, where n is length of string s2. 
We can do smarter if we also have num_to_correct variable which count number of letters for which we need to fix frequencies.

Complexity
Then time complexity will be O(n), space complexity is O(n) to keep A and B, which can be reduced to O(26) if we do it on the fly.



'''


class Solution:
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        if len(A) > len(B): return False
    
        target = [0] * 26
        for i in range(len(A)):
            target[A[i]] -= 1
            target[B[i]] += 1
        
        num_to_correct = sum([i != 0 for i in target])
        if num_to_correct == 0: return True
            
        for i in range(len(A), len(B)):
            new_s = B[i]
            target[new_s] += 1
            if target[new_s] == 0: num_to_correct -= 1
            if target[new_s] == 1: num_to_correct += 1
                
            old_s = B[i - len(A)]
            target[old_s] -= 1
            if target[old_s] == -1: num_to_correct += 1
            if target[old_s] == 0: num_to_correct -= 1
                                
            if num_to_correct == 0: return True  
                    
        return False
      
      
      
      
########### Same approach #################


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_c = Counter(s1)
        
        for i in range(len(s2)-window+1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True
            
        return False
      
      
      
############# Using counter #######################


from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1, d2 = Counter(s1), Counter(s2[:len(s1)])
        for start in range(len(s1), len(s2)):
            if d1 == d2: return True
            d2[s2[start]] += 1
            d2[s2[start-len(s1)]] -= 1
            if d2[s2[start-len(s1)]] == 0: 
                del d2[s2[start-len(s1)]]
        return d1 == d2
      
      
      
'''
   
Sorting:

One string is a permutation of another if they are the same string when sorted.
Hence, sort s1 and then sort the substrings of s2 that are of the same size
and compare
Time: O(n)O(k^2)O(klogk) = O(nk^3logk)
      
      
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s2 and not s1:
            return True
        '''
        
        One string is a permutation of another if 
        they are the same string when sorted. 
        
        Hence, sort s1 and then sort the substrings of s2 that are of the same size
        and compare
        Time: O(n)*O(k^2)*O(klogk) = O(n*k^3*logk)
        '''
        
        # sort s1
         s1 = "".join(sorted(list(s1)))
         k = len(s1)
        
         # sort the substrings of s2 that are of the same size
         for i in range(len(s2)): # -- O(n)
             sub = s2[i:i+k] # -- O(k)
             sub_str = "".join(sorted(list(sub)))  # ---- [1] 
            
             if s1 == sub_str:
                 return True
         return False
    
        # Runtime of that line = O(klogk) * O(k) * O(K)
        # Sorting and converting from string to list and back into a string
        
        
        
'''

Hashtable:


One string is a permutation of another if the two strings have the same character frequencies
Hence:
find freq dict for s1
find freq dict for substrings of s2 (that are the same size as s1)
runtime: O(n*k)


'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False
      
      
      
'''

Rolling Hash:

Enhanced freq dict - (Rolling hashmap)
simiar problem: 438. Find All Anagrams in a String
instead of generating a fresh freq hashmap for every new substring
build the freq dict for the initial window and then slide the window_dict
(add/remove chars) by adjusting their frequinces.
removing one preceding character and adding a new succeeding character to the new window


'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        from collections import Counter
        d1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        d2 = Counter(window)
        
        # check the intial window 
        if d1 == d2:
            return True
  
        for i in range(len(s2)-k):
        
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            
            # 2- add s2[i+k]
            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
                
            # check after sliding
            if d1 == d2:
                return True
                
        return False
      
      
      
      
'''

The only thing we care about any particular substring in s2 is having the same number of characters as in the s1. 
So we create a hashmap with the count of every character in the string s1. 
Then we slide a window over the string s2 and decrease the counter for characters that occurred in the window. 
As soon as all counters in the hashmap get to zero that means we encountered the permutation.

Time: O(n) - linear for window sliding and counter
Space: O(1) - conctant for dictionary with the maximum 26 pairs (English alphabet)


'''
      
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr: 
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]): # see optimized code below
                return True

        return False
      
      
      
'''

Optimized:

We can use an auxiliary variable to count a number of characters whose frequency gets to zero during window sliding. 
That helps us to avoid iterating over the hashmap for every cycle tick to check whether frequencies turned into zero.

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, match = Counter(s1), len(s1), 0     

        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]: match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]]: match += 1

            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]: match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]]: match += 1

            if match == len(cntr):
                return True

        return False
      
      
      
######### More optimized


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, matched = Counter(s1), len(s1), 0   

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in cntr: 
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True

        return False


      
      
'''
Simple solution:

or each window representing a substring of s2 of length len(s1), 
we want to check if the count of the window is equal to the count of s1. 
Here, the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]

We can maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). 
After, we only need to check if it is equal to the target. Working with list values of [0, 1,..., 25] 
instead of 'a'-'z' makes it easier to count later.

'''


class Solution:
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
      
      
      
