'''
First, I thought we could try every substring via recursion

Check if each substring is "valid"
If valid, update our "best" result
This is O(2^n), definitely not good enough
Second, why not "expand" a window from each character?

We loop over each character and call a function to "expand" a window
We try to increment the window by one to the right, if we ecounter a duplicate value, we stop
This is better, but still O(n^2)
Lastly, similar to previous idea, we can have a sliding window using a queue and a set

We just pop from the queue if we encounter a duplicate value
(we keep popping until queue is empty or we see the duplicate value)
Finally, we have O(n)


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                        
        queue = collections.deque([])        
        window = set()
        result = 0
        
        for c in s:            
            if c in window:
                while queue:
                    prev = queue.popleft()
                    window.remove(prev)
                    if prev == c:
                        break
                            
            queue.append(c)
            window.add(c)
            result = max(result, len(window))
            
        return result
      
      
################## Other solutions #########################



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
      
      
      
      ################ Time complexity O(n)
      ################ Space complexity O(m) m is the number of unique characters of the input.
      
      
      
############# using recursion
      
def lengthOfLongestSubstring(self, s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            res = max(res, i-start) # update the res
            start = max(start, dic[ch]+1)  # here should be careful, like "abba"
        dic[ch] = i
    return max(res, len(s)-start)  # return should consider the last non-repeated substring
  
  
  ############### Using list ######################################
  
  
  
  class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n // 10)
            return node
        return tolist(toint(l1) + toint(l2))
      
   # Time - O(n), Space - O(128) or say O(1) 
  
  
      
  
