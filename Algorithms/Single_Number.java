/*



XOR Properties:
   n^n = 0
   n^0 = n

Now we use this property to iterate over the complete array and store it in the 0th index to save space
everything that is duplicated turns into 0 (using first property) and the single number left, that is unique is
remaining at 0 index because it has no duplicat, it is left.
To understand this further try XOR over an array with all members having a pair. 
You would see that the final result would be 0. Therfore as the problem says there is one unique number which does not have a pair, 
remains as it is at the 0th index here.



*/


class Solution {
    public int singleNumber(int[] nums) {
      for(int i = 1; i < nums.length; i++) {
        nums[0] = nums[0] ^ nums[i];
      }
      return nums[0];
    }
}


/*

A simple solution, using 2 properties of XOR: A ⊕ A = 0 and B ⊕ 0 = B
In other words, A ⊕ A ⊕ B = B


*/


public class Solution {
    public int singleNumber(int[] nums) {
      for(int i=0;i<nums.length-1;i++){
        nums[i+1] ^= nums[i];
      }
      return nums[nums.length-1];
    }
}



// Same XOR

public class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for(int i = 0;i<nums.length;i++){
        result = result ^ nums[i];
        }
        return result;
    }
}





// Hashmap


class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i],1);
            }
            else {
                map.put(nums[i],map.get(nums[i]) + 1);
            }
        }
        for ( Map.Entry<Integer,Integer> entry : map.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if (map.get(key) == 1) {
                return key;
            }
        }
        return -1;
    }
}





// Concise solution


class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for(int i : nums) {
            result ^= i;
        }
        return result;
    }
}



