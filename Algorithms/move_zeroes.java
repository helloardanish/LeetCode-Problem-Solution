// Simple solution

class Solution {
    // Shift non-zero values as far forward as possible
    // Fill remaining space with zeros

    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;        

        int insertPos = 0;
        for (int num: nums) {
            if (num != 0) nums[insertPos++] = num;
        }        

        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }
}



// Another solution


class Solution {

    public void moveZeroes(int[] nums) {
        int count=0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i]==0)
                count++;
            if(count!=0&&nums[i]!=0){
                nums[i-count]=nums[i];
                nums[i]=0;
            }
        }
    }
}
