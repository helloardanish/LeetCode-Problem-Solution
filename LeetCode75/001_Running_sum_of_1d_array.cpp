// Running Sum of 1d Array


/*

https://leetcode.com/problems/running-sum-of-1d-array/

*/


// Solution 1

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if(nums.size()==0) return {-1};
        vector<int> ans;
        for(int i=0; i<nums.size(); i++){
            int sum=0;
            for(int j=0; j<=i; j++){
                sum = sum + nums[j];
            }
            ans.push_back(sum);
        }
        return ans;
    }
};


// Solution 2


class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if(nums.size()==0) return {-1};
        vector<int> ans;
        ans.push_back(nums[0]);
        for(int i=1; i<nums.size(); i++){
            nums[i] = nums[i-1] + nums[i];
            ans.push_back(nums[i]);
        }
        return ans;
    }
};


// Solution 3


class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if(nums.size()==0) return {-1};
        for(int i=1; i<nums.size(); i++){
            nums[i] = nums[i-1] + nums[i];
        }
        return nums;
    }
};
