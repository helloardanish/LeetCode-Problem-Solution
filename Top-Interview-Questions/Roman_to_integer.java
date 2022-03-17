public int romanToInt(String s) {
    int nums[]=new int[s.length()];
    for(int i=0;i<s.length();i++){
        switch (s.charAt(i)){
            case 'M':
                nums[i]=1000;
                break;
            case 'D':
                nums[i]=500;
                break;
            case 'C':
                nums[i]=100;
                break;
            case 'L':
                nums[i]=50;
                break;
            case 'X' :
                nums[i]=10;
                break;
            case 'V':
                nums[i]=5;
                break;
            case 'I':
                nums[i]=1;
                break;
        }
    }
    int sum=0;
    for(int i=0;i<nums.length-1;i++){
        if(nums[i]<nums[i+1])
            sum-=nums[i];
        else
            sum+=nums[i];
    }
    return sum+nums[nums.length-1];
}



// Another solution


class Solution {
    public int romanToInt(String s) {
        if(s==null || s.length() == 0){return 0;}
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X', 10);
        map.put('L',50);
        map.put('C',100);
        map.put('D', 500);
        map.put('M',1000);
        int num = 0;
        num += map.get(s.charAt(0));
        for(int i=1;i<s.length();i++){
            if(map.get(s.charAt(i)) <= map.get(s.charAt(i-1))){
                num += map.get(s.charAt(i));
            }else{
                num = num - 2*map.get(s.charAt(i-1)) + map.get(s.charAt(i));
            }
        }
        return num;
    }
}



// Another solution


public int romanToInt(String s) {
        int n = 0;
        char prev = ' ';
        for (byte i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            n += getValue(c, prev);
            prev = c;
        }
        
        return n;
    }
    
    private int getValue(char c, char prev) {
        switch (c) {
            case 'I':
                return 1;
            case 'V':
                return prev == 'I' ? 3 : 5;
            case 'X':
                return prev == 'I' ? 8 : 10;
            case 'L':
                return prev == 'X' ? 30 : 50;
            case 'C':
                return prev == 'X' ? 80 : 100;
            case 'D':
                return prev == 'C' ? 300 : 500;
            case 'M':
                return prev == 'C' ? 800 : 1000;
        }
        
        throw new IllegalArgumentException();
    }
