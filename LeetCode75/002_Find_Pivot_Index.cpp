// Find Pivot Index


/*

https://leetcode.com/problems/find-pivot-index/

*/



// Solution 1

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++){
            int leftsum = 0;
            int rightsum = 0;
            
            //leftsum calculate
            for(int j=i-1; j>=0; j--){
                leftsum = leftsum + nums[j];
            }
            
            //rightsum calculate
            for(int j=i+1; j<=nums.size()-1; j++){
                rightsum = rightsum + nums[j];
            }
            
            if(leftsum == rightsum) return i;
        }
        return -1;
    }
};



// Solution 2


class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int sum=0;
        for(int i=0; i<nums.size(); i++){
            sum = sum + nums[i];
        }
        
        int leftsum = 0;
        
        for(int i=0; i<nums.size(); i++){
            if(i>0) leftsum = leftsum + nums[i-1];
            int rightsum = sum-leftsum-nums[i];
            if(leftsum==rightsum) return i;
            
        }
        return -1;
    }
};



// Solution 3

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if(nums.size()==0) return -1;
        
        int sum=0;
        for(int i=0; i<nums.size(); i++){
            sum = sum + nums[i];
        }
        
        if(sum-nums[0] == 0) return 0;
        
        int leftsum = 0;
        
        for(int i=1; i<nums.size(); i++){
            leftsum = leftsum + nums[i-1];
            int rightsum = sum-leftsum-nums[i];
            if(leftsum==rightsum) return i;
            
        }
        return -1;
    }
};
