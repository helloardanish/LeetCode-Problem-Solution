class Solution {
    public void rotate(int[] nums, int k) {
      if(nums == null || nums.length < 2){
          return;
      }
      k = k % nums.length;
      reverse(nums, 0, nums.length - k - 1);
      reverse(nums, nums.length - k, nums.length - 1);
      reverse(nums, 0, nums.length - 1);
  }

  private void reverse(int[] nums, int i, int j){
      int tmp = 0;       
      while(i < j){
          tmp = nums[i];
          nums[i] = nums[j];
          nums[j] = tmp;
          i++;
          j--;
      }
  }
}



// Another similar way


class Solution {
    public void rotate(int[] nums, int k) {
      k %= nums.length;
      reverse(nums, 0, nums.length - 1);
      reverse(nums, 0, k - 1);
      reverse(nums, k, nums.length - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
          int temp = nums[start];
          nums[start] = nums[end];
          nums[end] = temp;
          start++;
          end--;
        }
    }
}




// Reduce code

class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length-1);  // reverse the whole array
        reverse(nums, 0, k-1);  // reverse the first part
        reverse(nums, k, nums.length-1);  // reverse the second part
    }

    public void reverse(int[] nums, int l, int r) {
        while (l < r) {
            //minimum code
            int tmp = nums[l];
            nums[l++] = nums[r];
            nums[r--] = tmp;
        }
    } 
}

