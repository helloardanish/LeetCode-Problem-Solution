/*


Idea:


1)Take the first(index=0) string in the array as prefix.
2)Iterate from second(index=1) string till the end.
3)Use the indexOf() function to check if the prefix is there in the strs[i] or not.
If the prefix is there the function returns 0 else -1.
4)Use the substring function to chop the last letter from prefix each time the function return -1.

eg:
strs=["flower", "flow", "flight"]
prefix=flower
index=1
    while(strs[index].indexOf(prefix) != 0) means while("flow".indexOf("flower")!=0)
    Since flower as a whole is not in flow, it return -1 and  prefix=prefix.substring(0,prefix.length()-1) reduces prefix to "flowe"
    Again while(strs[index].indexOf(prefix) != 0) means while("flow".indexOf("flowe")!=0)
    Since flowe as a whole is not in flow, it return -1 and  prefix=prefix.substring(0,prefix.length()-1) reduces prefix to "flow"
    Again while(strs[index].indexOf(prefix) != 0) means while("flow".indexOf("flow")!=0)
    Since flow as a whole is in flow, it returns 0 so now prefix=flow
index=2
    while(strs[index].indexOf(prefix) != 0) means while("flight".indexOf("flow")!=0)
    Since flow as a whole is not in flight, it return -1 and  prefix=prefix.substring(0,prefix.length()-1) reduces prefix to "flo"
    Again while(strs[index].indexOf(prefix) != 0) means while("flight".indexOf("flo")!=0)
    Since flo as a whole is not in flight, it return -1 and  prefix=prefix.substring(0,prefix.length()-1) reduces prefix to "fl"
    Again while(strs[index].indexOf(prefix) != 0) means while("flight".indexOf("fl")!=0)
    Since fl as a whole is in flight, it returns 0 so now prefix=fl
index=3, for loop terminates and we return prefix which is equal to fl


*/



class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for(int index=1;index<strs.length;index++){
            while(strs[index].indexOf(prefix) != 0){
                prefix=prefix.substring(0,prefix.length()-1);
            }
        }
        return prefix;
    }
}





// another solution


public class Solution {
    public String longestCommonPrefix(List<String> strs) {
        if(strs.size()==0) return "";
        StringBuilder lcp=new StringBuilder();
        for(int i=0;i<strs.get(0).length();i++){
            char c=strs.get(0).charAt(i);
            for(String s:strs){
                if(s.length()<i+1||c!=s.charAt(i)) return lcp.toString();
            }
            lcp.append(c);
        }
        return lcp.toString();
    }
}




// another solution


class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null) return null;
        if (strs.length == 0) return "";

        Arrays.sort(strs);
        char[] first = strs[0].toCharArray();
        char[] last  = strs[strs.length - 1].toCharArray();

        int i = 0, len = Math.min(first.length, last.length);
        while (i < len && first[i] == last[i]) i++;
        return strs[0].substring(0, i);
    }
}






// another solution


class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0)    return "";
        String pre = strs[0];
        int i = 1;
        while(i < strs.length){
            while(strs[i].indexOf(pre) != 0)
                pre = pre.substring(0,pre.length()-1);
            i++;
        }
        return pre;
    }
}






// another solution


class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null) return null;
        if (strs.length == 0) return "";

        Arrays.sort(strs);
        char[] first = strs[0].toCharArray();
        char[] last  = strs[strs.length - 1].toCharArray();

        int i = 0, len = Math.min(first.length, last.length);
        while (i < len && first[i] == last[i]) i++;
        return strs[0].substring(0, i);
    }
}
