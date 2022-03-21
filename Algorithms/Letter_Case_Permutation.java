/*


When I saw a problem, my first step is to draw a figure. See the figure below:
abc
abc Abc 0
abc aBc Abc ABc 1
abc abC aBc aBC Abc AbC ABc ABC 2

There we go! Is that a typical BFS/DFS problem? Yes, you are right!
Be careful to check whether a character is a digit or a letter(lower case or upper case).


*/


// BFS


class Solution {
    public List<String> letterCasePermutation(String S) {
        if (S == null) {
            return new LinkedList<>();
        }
        Queue<String> queue = new LinkedList<>();
        queue.offer(S);
        
        for (int i = 0; i < S.length(); i++) {
            if (Character.isDigit(S.charAt(i))) continue;            
            int size = queue.size();
            for (int j = 0; j < size; j++) {
                String cur = queue.poll();
                char[] chs = cur.toCharArray();
                
                chs[i] = Character.toUpperCase(chs[i]);
                queue.offer(String.valueOf(chs));
                
                chs[i] = Character.toLowerCase(chs[i]);
                queue.offer(String.valueOf(chs));
            }
        }
        
        return new LinkedList<>(queue);
    }
}



// DFS


class Solution {
    public List<String> letterCasePermutation(String S) {
        if (S == null) {
            return new LinkedList<>();
        }
        
        List<String> res = new LinkedList<>();
        helper(S.toCharArray(), res, 0);
        return res;
    }
    
    public void helper(char[] chs, List<String> res, int pos) {
        if (pos == chs.length) {
            res.add(new String(chs));
            return;
        }
        if (chs[pos] >= '0' && chs[pos] <= '9') {
            helper(chs, res, pos + 1);
            return;
        }
        
        chs[pos] = Character.toLowerCase(chs[pos]);
        helper(chs, res, pos + 1);
        
        chs[pos] = Character.toUpperCase(chs[pos]);
        helper(chs, res, pos + 1);
    }
}





// With explanation DFS/Backtracking


class Solution {
    /**  
            a1b2   i=0, when it's at a, since it's a letter, we have two branches: a, A
         /        \
       a1b2       A1b2 i=1 when it's at 1, we only have 1 branch which is itself
        |          |   
       a1b2       A1b2 i=2 when it's at b, we have two branches: b, B
       /  \        / \
      a1b2 a1B2  A1b2 A1B2 i=3  when it's at 2, we only have one branch.
       |    |     |     |
      a1b2 a1B2  A1b2  A1B2 i=4 = S.length(). End recursion, add permutation to ans. 
      
      During this process, we are changing the S char array itself
    */
    public List<String> letterCasePermutation(String S) {
        List<String> ans = new ArrayList<>();
        backtrack(ans, 0, S.toCharArray());
        return ans;
    }
    public void backtrack(List<String> ans, int i, char[] S){
        if(i==S.length)
            ans.add(new String(S));
        else{
            if(Character.isLetter(S[i])){ //If it's letter
                S[i] = Character.toUpperCase(S[i]);
                backtrack(ans, i+1, S); //Upper case branch
                S[i] = Character.toLowerCase(S[i]);
                backtrack(ans, i+1, S); //Lower case branch
            }
            else
                backtrack(ans, i+1, S); 
        }
    }
}




// Another backtrack


class Solution {
    
    void recurse(char[] str, int pos, List<String> result) {
        //If we have reached a leaf in the recursion tree, save the result.
        if (pos == str.length) {
            result.add(new String(str));
            return;
        }
        
        //If char is not a letter, no processing required.
        if (Character.isLetter(str[pos])) {
            //If uppercase char, we make it lower case, and recurse.
            if (Character.isUpperCase(str[pos])) {
                str[pos] = Character.toLowerCase(str[pos]);
                
                //Start a new branch in the recursion tree, exploring options that are possible only if we had changed the case.
                recurse(str, pos + 1, result);
                
                //Backtracking. We undo the change so that we can start a new branch in the recursion tree.
                str[pos] = Character.toUpperCase(str[pos]);
            }
            //If lowercase, then we make it upper case, and recurse.
            else {
                str[pos] = Character.toUpperCase(str[pos]);
                recurse(str, pos + 1, result);
                //Backtracking as explained above.
                str[pos] = Character.toLowerCase(str[pos]);
            }
        }
        //This branch explores options that are possible only if the previously performed change (if any) hadn't happened.
        recurse(str, pos + 1,  result);
    }
    
    public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<>();
        recurse(S.toCharArray(), 0, result);
        return result;
    }
}

/*


Time Complexity

O(N * 2^N), where N is the string length. 2^N because for each character, 
we have two choices (whether to transform it or not). 
The extra N factor is because once we reach a leaf, 
we have to copy the result into a new string (which costs O(N)).

Space Complexity

O(N * 2^N). Similar reasoning as above. 2^N combinations are possible, 
and we'll need O(N) space for each of them. 
I guess this includes the space required for recursion (O(2^N)), as well.

Notes

Notice that we are passing a char array to the recursion function, 
not a whole String. Doing so would consume a lot of extra memory, since Strings are immutable. 
Since we need the resultant strings only when we hit the end of recursion, 
they would be a waste of space anyway. 
A StringBuilder object would also serve the purpose.


*/



// Another solution


// Using recursion

class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> ans=new ArrayList<>();
        compute(ans,S.toCharArray(),0);
        return ans;
    }
    
    public void compute(List<String> ans, char[] chars, int index)
    {
        if(index==chars.length)
            ans.add(new String(chars));
        else
        {
            if(Character.isLetter(chars[index]))
            {
                chars[index]=Character.toLowerCase(chars[index]);
                compute(ans,chars,index+1);
                chars[index]=Character.toUpperCase(chars[index]);
            }
            compute(ans,chars,index+1);
        }
    }
}




// Using recursion

class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> list = new ArrayList<>();
        if (S == null || S.length() == 0) {
            list.add("");
            return list;
        }
        List<String> results = letterCasePermutation(S.substring(1));
        for (String result : results) {
            if (Character.isLetter(S.charAt(0))) {
                list.add(S.substring(0, 1).toLowerCase() + result);
                list.add(S.substring(0, 1).toUpperCase() + result);
            } else {
                list.add(S.substring(0, 1) + result);
            }
        }
        return list;
    }
}






// Recursive


class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<>();
        letterCasePermutation(S, 0, result, "");
        return result;
    }
    
    private void letterCasePermutation(String s, int idx, List<String> result, String current) {
        if (idx == s.length()) {
            result.add(current);
        } else {
            char c = s.charAt(idx);
            letterCasePermutation(s, idx + 1, result, current + c);
            if (Character.isLetter(c))
                letterCasePermutation(s, idx + 1, result,
                        current + (Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c)));
        }
    }
}





// Using only one queue


class Solution {
    public List<String> letterCasePermutation(String S) {
        LinkedList<String> r = new LinkedList<>();
        r.add(S);
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if (Character.isLetter(c))
                for (int size = r.size(); size > 0; size--) {
                    String s = r.poll(), left = s.substring(0, i), right = s.substring(i + 1);
                    r.add(left + Character.toLowerCase(c) + right);
                    r.add(left + Character.toUpperCase(c) + right);
                }
        }
        return r;
    }
}



