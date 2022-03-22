'''


str=["flower","flow","flight"]

after zip(*strs)

[('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]

taken first set

len(set( "f","f","f"))=1

and taken 3
len(set("o","o","i"))=2


'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)


      
      
'''

strs = ["flower","flow","flight"]
l = list(zip(*strs))
>>> l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]


'''
      
   
    
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix
      
      
      
      


# another function

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        str1, str2 = min(strs), max(strs)
        i = 0
        while i < len(str1):
            if str1[i] != str2[i]:
                str1 = str1[:i]
            i +=1

        return str1
      
      
      

      
# another solution


class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        if not S: return ''
        m, M, i = min(S), max(S), 0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: break
        else: i += 1
        return m[:i]
      
      
      
      
# another solution


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
      
      
      
      
      
      
# using enumerater

class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
      
      
      
      
# another solution


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
          
          
          
          

		
		
		
# another solution


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    def longest_prefix(self):
        res = []
        cur = self.root
        while cur:
            # return when reaches the end of word or when there are more than 1 branches
            if cur.end or len(cur.children) > 1:
                return ''.join(res)
            c = list(cur.children)[0]
            res.append(c)
            cur = cur.children[c]
        return ''.join(res)
        
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        T = Trie()
        for s in strs:
            T.add_word(s)
        return T.longest_prefix()



'''


Time complexity:

building Trie: O(N*len(s)) where N = len(strs) and s is the longest word in strs
finding longest prefix: O(M) where M is the length of LCP (which is in the range of 0 and the length of shortest string)


'''
