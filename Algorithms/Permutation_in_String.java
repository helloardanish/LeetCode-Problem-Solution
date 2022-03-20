/*


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


*/



class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] map = new int[26];
        for(char c : s1.toCharArray()) map[c - 'a']++;
        int j = 0, i = 0;
        int count_chars = s1.length();
        while(j < s2.length()){
            if(map[s2.charAt(j++) - 'a']-- > 0)
                count_chars--;
            if(count_chars == 0) return true;
            if(j - i == s1.length() && map[s2.charAt(i++) - 'a']++ >= 0)
                count_chars++;
        }
        return false;
    }
}



// Another



/*

How do we know string p is a permutation of string s? 
Easy, each character in p is in s too. So we can abstract all permutation strings of s to a map (Character -> Count). 
i.e. abba -> {a:2, b:2}. Since there are only 26 lower case letters in this problem, 
we can just use an array to represent the map.

How do we know string s2 contains a permutation of s1? 
We just need to create a sliding window with length of s1, 
move from beginning to the end of s2. When a character moves in from right of the window, 
we subtract 1 to that character count from the map. 
When a character moves out from left of the window, we add 1 to that character count. 
So once we see all zeros in the map, meaning equal numbers of every characters between s1 and the substring in the sliding window, 
we know the answer is true.

*/




public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2) return false;
        
        int[] count = new int[26];
        for (int i = 0; i < len1; i++) {
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }
        if (allZero(count)) return true;
        
        for (int i = len1; i < len2; i++) {
            count[s2.charAt(i) - 'a']--;
            count[s2.charAt(i - len1) - 'a']++;
            if (allZero(count)) return true;
        }
        
        return false;
    }
    
    private boolean allZero(int[] count) {
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }
        return true;
    }
}




// Same idea, using a counter to avoid the loop


class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        // corner case
        if (len1 > len2) return false;
        int[] count = new int[26];
        // initialize the count for each unique character
        for (char c : s1.toCharArray()) {
            count[c - 'a'] ++;
        }
        // initialize the sliding window with static size len1
        int i = 0, j = 0, counter = len1;
        while (j < len1) {
            if (count[s2.charAt(j++) - 'a']-- > 0) {
                counter --;
            }
        }
        while (j < len2 && counter != 0) {
            if (count[s2.charAt(i++) - 'a']++ >= 0) counter ++;
            if (count[s2.charAt(j++) - 'a']-- > 0) counter --;
        }
        return counter == 0;
    }
}




// another solution


class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] count = new int[128];
        for(int i = 0; i < s1.length(); i++) count[s1.charAt(i)]--;
        for(int l = 0, r = 0; r < s2.length(); r++) {
            if (++count[s2.charAt(r)] > 0)
                while(--count[s2.charAt(l++)] != 0) { /* do nothing */}
            else if ((r - l + 1) == s1.length()) return true;
        }
        return s1.length() == 0;
    }
}




/*

Firstly, we count the number of characters needed in p string.
Then we sliding window in the s string:
Let l is the left index of the window, r is the right index of the window.
Iterate r in range [0..n-1].
When we meet a character c = s[r], we decrease the cnt[c] by one like cnt[c]--, if the cnt[c] < 0 then we need to slide left to make sure cnt[c] >= 0.
We also need nChars to keep remain of characters need to be filled, initial nChars = p.length().
If nChars == 0 then we already found a window which is perfect match with string p, then return true.

*/


class Solution {
    public boolean checkInclusion(String p, String s) { // renamed s1 to p, s2 to s
        int[] cnt = new int[128];
        for (char c : p.toCharArray()) {
            cnt[c]++;
        }

        int nChars = p.length();
        for (int r = 0, l = 0; r < s.length(); ++r) {
            char c = s.charAt(r);

            cnt[c]--;
            nChars--;
            while (cnt[c] < 0) { // If number of characters `c` is more than our expectation
                cnt[s.charAt(l)]++;  // Slide left until cnt[c] == 0
                l++;
                nChars++;
            }

            if (nChars == 0) { // If we already filled enough `p.length()` chars
                return true;
            }
        }
        return false;
    }
}


// Time: O(|p| + |s|)       Space: O(1)


// Simplified


class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] need = new int[26];
        for (char c : s1.toCharArray()) {
            need[c - 'a']++;
        }
        for (int i = 0, j = 0; i < s2.length(); i++) {
            if (--need[s2.charAt(i) - 'a'] < 0) { 
                while (need[s2.charAt(i) - 'a'] != 0) { 
                    need[s2.charAt(j++) - 'a']++;
                }
            } else if (i - j + 1 == s1.length()) { //check the length of the window equals the length of s1
                return true;
            }
        }

        return false;

    }
}



// Another

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1=s1.length(),n2=s2.length();
        int[] f1=new int[26];
        for(int i=0;i<n1;i++) f1[s1.charAt(i)-'a']++;
        
        int[] f2=new int[26];
        for(int j=0;j<n2;j++){
            f2[s2.charAt(j)-'a']++;
            if(j>=n1) f2[s2.charAt(j-n1)-'a']--;
            if(Arrays.equals(f2,f1)) return true;
        }
        return false;
    }
}
