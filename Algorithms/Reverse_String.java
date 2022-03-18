/*



There're many ways you can trip this up on an interview (or even just practising here). The simplest questions are the most lethal IMO. It's not always about going from O(n!) to O(log n) via incomprehensible cleverness (there are algorithms that you can't invent at an interview, you either know it or you don't; it doesn't test how good a developer you are). Think about how many ways there are just to do the char[] reversal. Here are some decision points one has to make during answering this question:

Use Java API or implement it low level?
Call reverse Java API?
+= between Strings in core loop (see, not all solutions are O(n) ;)
StringBuilder VS StringBuffer (synchronized)
Construct a StringBuilder from input and do mutating operations: charAt and setCharAt
Use toCharArray() and read from char[], or use String.charAt()
Do preallocate builder capacity or let it grow?
Use append(char) or setCharAt?
How to iterate?
loop based on input length
two pointers (start | end) or loop all items
start from front or back
while or for
while(true) or while(start < end) or while(start <= end)
cache length in for loop or query each time
recursion
+=
Collecting argument (char[] + index, StringBuilder)
Create a method for iteration or leave it inline?
shortcut for "", "x"?
specialize for "xy" and "xyz"?
What about null input?
How do you format your code?


*/



// Simple solution

class Solution {
    public void reverseString(char[] s) {
        for(int i = 0, j = s.length- 1 ; i < j ; i++,j--){
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    }
}



// Another


class Solution {
    public void reverseString(char[] s) {
        if (s == null || s.length <= 1) {
            return;
        }

        int left = 0;
        int right = s.length - 1;
        while (left < right) {
            s[left] = (char) (s[left] ^ s[right]);
            s[right] = (char) (s[left] ^ s[right]);
            s[left] = (char) (s[left] ^ s[right]);
            left++;
            right--;
        }
    }
}



// Recursive solution


class Solution {
    public void reverseString(char[] s) {
        if (s == null || s.length <= 1) {
            return;
        }

        reverseStringHelper(s, 0, s.length - 1);
    }

    private void reverseStringHelper(char[] s, int left, int right) {
        if (left >= right) {
            return;
        }
        s[left] = (char) (s[left] ^ s[right]);
        s[right] = (char) (s[left] ^ s[right]);
        s[left] = (char) (s[left] ^ s[right]);
        reverseStringHelper(s, left + 1, right - 1);
    }
}

// Recursive another

class Solution {
    public void reverseString(char[] s) {
        solve(s, 0, s.length-1);  
    }
    
    public void solve(char[] s, int start, int end){
        if(start>=end)return; //base case
        swap(s, start, end);
        solve(s, ++start, --end);
    }
    
    public void swap(char[] s, int i, int j){
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}



