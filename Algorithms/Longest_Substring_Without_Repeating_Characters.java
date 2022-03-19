/*


the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values, 
and keep two pointers which define the max substring. 
move the right pointer to scan through the string , and meanwhile update the hashmap. 
If the character is already in the hashmap, then move the left pointer to the right of the same character last found. 
Note that the two pointers can only move forward.


*/


class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }
}



/*

Same algo with int[256] rather than HashMap. Faster than map and shorter code.

*/

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int[] cache = new int[256];
        for (int i = 0, j = 0; i < s.length(); i++) {
            j = (cache[s.charAt(i)] > 0) ? Math.max(j, cache[s.charAt(i)]) : j;
            cache[s.charAt(i)] = i + 1;
            result = Math.max(result, i - j + 1);
        }
        return result;
    }
}



// Java Sliding Window based on Queue


class Solution {
    public int lengthOfLongestSubstring(String s) {
        Queue<Character> queue = new LinkedList<>();
        int res = 0;
        for (char c : s.toCharArray()) {
            while (queue.contains(c)) {
                queue.poll();
            }
            queue.offer(c);
            res = Math.max(res, queue.size());
        }
        return res;
    }
}


// Similar idea using a Set


class Solution {
    public int lengthOfLongestSubstring(String s) {        
        int maxLen = 0;
        Set<Character> window = new HashSet<>(); 

        int left = 0, right = 0;
        while(right < s.length()) { 
            while(window.contains(s.charAt(right)))
                window.remove(s.charAt(left++));  
            window.add(s.charAt(right++)); 
            maxLen = Math.max(maxLen, right - left);
        }

        return maxLen;
    }
}



// another solution


class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, j = 0, max = 0;
        Set<Character> set = new HashSet<>();

        while (j < s.length()) {
            if (!set.contains(s.charAt(j))) {
                set.add(s.charAt(j++));
                max = Math.max(max, set.size());
            } else {
                set.remove(s.charAt(i++));
            }
        }

        return max;
    }
}



//Another solution

/**
 * Use HashMap to keep char and its index map. When we find a repeating char
 * update the start point.
 *
 * Time Complexity: O(N)
 *
 * Space Complexity: O(min(M,N)) = O(1) since there are 26 alphabets.
 *
 * N = Length of input string. M = Size of the character set
 */
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null) {
            throw new IllegalArgumentException("Input string is null");
        }

        int len = s.length();
        if (len <= 1) {
            return len;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        int start = 0;
        int maxLen = 0;

        for (int end = 0; end < len; end++) {
            char eChar = s.charAt(end);
            if (map.containsKey(eChar)) {
                start = Math.max(start, map.get(eChar) + 1);
            }
            map.put(eChar, end);
            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }
}


// Anothersolution


/*

Idea is that, while we traverse form left to right,
if we see a character at position j is a duplicate of a character at a position i < j on the left,
then we know that we can't start the substring from i anymore. 
So, we need to start a new substring from i+1 position. 
While doing this we also need to update the length of current substring and start of current substring. 
Important part of this process is to make sure that we always keep the latest position of the characters 
we have seen so far. Below is a simple O(n) implementation of this logic.

*/

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




// Acquire and Release(Sliding WIndow) solution


class Solution {
    public int lengthOfLongestSubstring(String s) {
        int acquire=0;
        int release=0;
        int max=0;
        HashSet<Character> hash=new HashSet();
        while(acquire<s.length()){
            if(!hash.contains(s.charAt(acquire))){
                hash.add(s.charAt(acquire));
                acquire++;
                max=Math.max(hash.size(),max);
            }
            else{
                hash.remove(s.charAt(release));
                release++;
            }
        }
        return max;
    }
}
