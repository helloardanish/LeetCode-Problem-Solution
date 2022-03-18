############# Simple solution ######################


class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)
      
      
      
'''


Idea:
initilialize two pointers, l and r.
Move the right pointer as long as it's not pointing to the whitespace.
If it finally points to the whitespace, we have a word. Take this word by using slicing, reverse it, and add to res.
Move r and l. Now they point to the character after the whitespace (essentially, it's where the next word starts).

Once the loop ends, we have the last word unproccessed.

Add an extra space to res (because l always points to the first character of a word).
Add the reversed word to res.
Finally, res has one extra whitespace in the beginning. It appeared when we were appending the first word. But you can account for this in your return statement.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l:r + 1][::-1]
                r += 1
                l = r
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]
      
      
## Reducing line of code

class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0  # start of current word
        r = 0  # position after end of current word
        #   For each word in the string
        while r < len(s):
            #   Advance r to end-of-current-word or end-of-string
            while r < len(s) and s[r] != ' ':
                r += 1
            #   reverse current word within s and assign result back to s
            s = s[:l] + s[l:r][::-1] + s[r:]
            #   Advance l and r to the start of next word
            r += 1
            l = r
        return s
      
      
      
############### 1 liner and more faster ###################

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda x: x[::-1], s.split()))
        
        
        
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])
        
        
        
################ 
