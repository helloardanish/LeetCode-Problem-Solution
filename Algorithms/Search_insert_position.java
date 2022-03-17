class Solution {
public int searchInsert(int[] nums, int target) {
    int x=Arrays.binarySearch(nums,target);
    if(x<0){
        return -x-1;
    }
    return x;
    }
}
