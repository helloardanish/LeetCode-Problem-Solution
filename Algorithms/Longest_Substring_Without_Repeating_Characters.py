'''


This is classical problem for sliding window. Let us keep window with elements [beg: end), 
where first element is included and last one is not. For example [0, 0) is empty window, 
and [2, 4) is window with 2 elements: 2 and 3.
Let us discuss our algorithm now:

1. window is set of symbols in our window, we use set to check in O(1) if new symbol inside it or not.
2. beg = end = 0 in the beginning, so we start with empty window, also ans = 0 and n = len(s).
3. Now, we continue, until one of two of our pointers reaches the end. First, we try to extend our window to the right: 
   check s[end] in window and if we can, add it to set, move end pointer to the right and update ans. 
   If we can not add new symbol to set, it means it is already in window set, 
   and we need to move left pointer and move beg pointer to the right.

Complexity: we move both of our pointers only to the left, so time complexity is O(n). Space complexity is O(1).


'''




class Solution:
    def lengthOfLongestSubstring(self, s):
        window = set()
        beg, end, ans, n = 0, 0, 0, len(s)
        
        while beg < n and end < n:
            if s[end] not in window:
                if end + 1 < n: window.add(s[end])
                end += 1
                ans = max(ans, end - beg)
            else:
                window.remove(s[beg])
                beg += 1
                
        return ans



## Similar approach but used list instead of set
      
      
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = maxCount = 0
        seen = []

        for x in s:
            if x not in seen:
                seen.append(x)
                count=len(seen)
                if count > maxCount:
                    maxCount = count
            else:
                seen[:seen.index(x)+1] = []
                seen.append(x)
                count = 0
        return maxCount
      
      
      
      
#### Using dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dic={}
        ans=0
        n=len(s)
        l=0
        for r,val in enumerate(s):
            if val in dic:
                if dic[val]>=l:
                    l=dic[val]+1
            ans=max(ans,r-l+1)
            dic[val]=r
        return ans
      
      
      
'''

Sliding window
We use a dictionary to store the character as the key, the last appear index has been seen so far as value.
seen[charactor] = index

move the pointer when you met a repeated character in your window.



'''
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
    

    
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            """
            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            """
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

      
      
'''

Time complexity :O(n).
n is the length of the input string.
It will iterate n times to get the result.

Space complexity: O(m)
m is the number of unique characters of the input.
We need a dictionary to store unique characters.


'''
     

  
# Another approach
      
      
'''

Idea is that, while we traverse form left to right. 
If we see a character at position j is a duplicate of a character at a position i < j on the left 
then we know that we can't start the substring from i anymore. 
So, we need to start a new substring from i+1 position. 
While doing this we also need to update the length of current substring and start of current substring. 
Important part of this process is to make sure that we always keep the latest position of the characters we have seen so far. 
Below is a simple O(n) implementation of this logic.



'''
      

  
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lastIndices[] = new int[256];
        for(int i = 0; i<256; i++){
            lastIndices[i] = -1;
        }
        
        int maxLen = 0;
        int curLen = 0;
        int start = 0;
        int bestStart = 0;
        for(int i = 0; i<s.length(); i++){
            char cur = s.charAt(i);
            if(lastIndices[cur]  < start){
                lastIndices[cur] = i;
                curLen++;
            }
            else{
                int lastIndex = lastIndices[cur];
                start = lastIndex+1;
                curLen = i-start+1;
                lastIndices[cur] = i;
            }
            
            if(curLen > maxLen){
                maxLen = curLen;
                bestStart = start;
            }
        }
        
        return maxLen;
    }
}
  
  
      
'''


We initialize the result res = 0, and two pointers j = 0, and i = 0. 
We initialize a dictionary dic which maps every element in s[:i+1] to its index of rightmost occurrence in s[:i+1]. 
Then we iterate i over range(len(s)), if s[i] is not in dic, we add it to dic: dic[s[i]] = i; 
Otherwise, we move j to max(j, dic[s[i]]+1), so that within the window [j:i+1], 
the element s[i] only occur once. Then we update the result res = max(res, i-j+1). 
Finally, we return res.

Time complexity: O(n), space complexity: O(n).


'''



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]]+1)
                dic[s[i]] = i
            res = max(res, i-j+1)
        return res
      
      
      
############# another solution ####################


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub = ''

        for l in s:
            if l in sub:
                sub = sub[sub.find(l)+1:]        
            sub += l
            if len(sub) > max_len:
                max_len = len(sub)

        return max_len
      
      
      
      
################## Using set ####################


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		characters = set()
		left = right = ans = 0
		length = len(s)
		
		while right < length:
			if s[right] in characters:
				characters.remove(s[left])
				left += 1
			else:
				characters.add(s[right])
				right += 1
				ans = max(ans, right - left)
		
		return ans
  
  
  
############# Minimized code ##################



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = ''
        mx = 0
		  #1. for each character in s
        for c in s:
			#2. check if c is seen
            if c not in seen:
			#3. if not seen, add to seen list 
                seen+=c
            #4 if seen, slice seen list to previous c
            # for example, if c is 'a' and seen list is 'abc'
            # you will be slicing previous 'a'(seen.index(c)+1), thus seen list become 'bc'
            # then add the current 'a' bc + a, seenlist = 'bca'
            else:
                seen = seen[seen.index(c) + 1:] + c
            #5 check max length between current max with new length of seen
            mx = max(mx, len(seen))
        return mx
      
      
      
##### another


## using left and right index with help of dictionary

def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        mx = left = 0
        #1. for each character in s
        for right, c in enumerate(s):
            #2. check if c is seen
            if c in seen:
                #3. if seen, advance left index
                left = max(left, seen[c] + 1)
            #4. regardless the character seen or not seen,
            #   it will update the index of the charater.
            seen[c] = right
            #5. check max length between current left index and right index + 1
            mx = max(mx, right-left+1)
        return mx



## another


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        lastIndex = [-1] * 128
        for r, c in enumerate(s):
            l = max(l, lastIndex[ord(c)] + 1)
            lastIndex[ord(c)] = r
            ans = max(ans, r - l + 1)
        return ans
      
      
## Time: O(N), where N <= 5 * 10^4 is length of string s. Space: O(128)

#### Another 

class Solution:
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start) # update the res
                start = max(start, dic[ch]+1)  # here should be careful, like "abba"
            dic[ch] = i
        return max(res, len(s)-start)  # return should consider the last non-repeated substring
      
      
