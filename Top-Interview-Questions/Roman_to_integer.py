'''

First things first: Because we need to look up the value of each roman charater multiple times, let's store them in a dictionary called sym to have O(1) lookup.

Example:
Looking at these characters is confusing. To come up with an algorithm, FIRST replace these characters with their numeral values and then forget about the roman letters.
LVIII: 50, 5, 1, 1, 1
XIV: 10, 1, 5
MCMXCIV: 1000, 100, 1000, 10, 100, 1, 5

Just keep referencing the numbers and you'll see that you have 2 choices to add the numbers:

left-to-right. I'll leave left-to-right for you to solve and debate.
right-to-left.
When we go right-to-left, we see the pattern:

we need to add current number if it is bigger than previous number or if both are same.
we subtract current number if current number is smaller than the previous number.
Example: XIV (10, 1, 5)

We first add 5
In the next iteration, current is 1 and previous is 5. So, we subtract 1 from result
In next iteration, current is 10 and previous is 1. So, we add 10 to the result


'''

class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        result = 0
        prev = 0
        
        for c in reversed(s):
            if sym[c] >= prev:
                result += sym[c]
            else:
                result -= sym[c]
            prev = sym[c]
            
        return result


########## Simple approach ######################3

class Solution:
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
  
  
  ########## Creating own number system, haha xD ####################
  
  
  # my_mind.replace(original_roman_system, your_roman_system)
  class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
      

