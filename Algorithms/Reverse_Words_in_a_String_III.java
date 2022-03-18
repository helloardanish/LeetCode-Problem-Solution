/*

Idea:

Convert string to char array to avoid having to deal with separate strings (since concatenation is an expensive operation).
Go through char array, keeping pointer start at the beginning of words and pointer end iterating through whole array checking for white space.
If white space is found, call function reverse() on char array to reverse chars between start and end-1 (inclusive)
Once loop is finished, start now points to start of last word and end points to the last+1 index of char array
Thus, need to call reverse once again to reverse the last word.
Return char array as a String

*/


class Solution {
    public String reverseWords(String s) {
        
        char[] c = s.toCharArray();
        int start = 0, end = 0;
        for(; end < c.length; end++){
            if(c[end] == ' '){
                reverse(c, start, end-1);
                start = end+1;
            }
        }
        reverse(c, start, end-1);
        return new String(c);
    }
    
    private void reverse(char[] c, int start, int end){
        while(start < end){
            char tmp = c[end];
            c[end] = c[start];
            c[start] = tmp;
            start++;
            end--;
        }
    }
}




// another solution


/*

Step 1. Convert the string to char[] array
Step 2. Whenever I encounter a space ' ' , I call the reverse function ( just to keep the code clean )
Step 3. Repeat till the end!

*/

class Solution {
    public String reverseWords(String s) 
    {
        char[] s1 = s.toCharArray();
        int i = 0;
        for(int j = 0; j < s1.length; j++)
        {
            if(s1[j] == ' ')
            {
                reverse(s1, i, j - 1);
                i = j + 1;
            }
        }
        reverse(s1, i, s1.length - 1);
        return new String(s1);
    }

    public void reverse(char[] s, int l, int r)
    {
        while(l < r)
        {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++; r--;
        }
    }
}


// The basic idea is to get the first and last index of each word and reverse word with itself using first and last indexes

class Solution {
    public String reverseWords(String s) {
        
        final int len = s.length(); // saving the length as constant so as to avoid calling s.length() again and again.
        
        if(len == 1) // no need to iterate if string is of length 1
            return s;
        
        int firstIndex, lastIndex;
        char[] ch = s.toCharArray(); // converting the string into it's corresponding character array
        char temp;
        
        for(int index = 0 ; index < len ; index++){
            
            firstIndex = index; // store the first index of word
            
            while(++index < len && ch[index] != ' '); // iterate until space is found i.e. to get the last index of the word
            
            lastIndex = index - 1; // store the last index of the word
            
			// reverse characters of the word
            while(firstIndex < lastIndex){
                temp = ch[firstIndex];
                ch[firstIndex++] = ch[lastIndex];
                ch[lastIndex--] = temp;
            }
        }
        
        return new String(ch); // convert the character into string and return it
    }
}



// Another solution


class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder("");
        for (String word : words)
            sb.append(" ").append(reverse(word));
        return sb.toString().substring(1);
    }
    static String reverse(String s) {
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }
}
