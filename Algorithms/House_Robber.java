/*

Intution: At every i-th house we have two choices to make, i.e., rob the i-th house or don't rob it.

Case1 : Don't rob the i-th house - then we can rob the i-1 th house...so we will have max money robbed till i-1 th house
Case 2 : Rob the i-th house - then we cann't rob the i-1 th house but we can rob i-2 th house....so we will have max money robbed till i-2 th house + money of i-th house.
Example:
1.) If the array is [1,5,3] then robber will rob the 1st index house because arr[1] > arr[0]+arr[2] (i.e., at last index, arr[i-1] > arr[i-2]+arr[i])
2.) If the array is [1,2,3] then robber will rob the 0th and 2nd index house because arr[0]+arr[2] > arr[1] (i.e., at last index, arr[i-2] + arr[i] > arr[i-1])
Approach 1: Dynamic Programming
T.C : O(n)
S.C : O(n)


*/


class Solution {
    public int rob(int[] nums) {
        
        int n = nums.length;
        int dp[] = new int[n];
        dp[0]=nums[0];
        if(n==1){
            return nums[0];
        }
        
        dp[1] = Math.max(nums[0],nums[1]);
        
        for(int i=2;i<n;i++){
            dp[i] = Math.max(nums[i]+dp[i-2],dp[i-1]);
        }
        
        return dp[n-1];

    }
}






/*



Modified Dynammic Programming
T.C : O(n)
S.C : O(1)

Explanation: We actually don't need to have full dp array to store the previous values beacause 
we need only two previous values that is max robbery till i-2 th index and i-1 th index 
which we can store using two variables dp2 and dp1 resepectively.




*/


class Solution {
    public int rob(int[] nums) {
        
        int n = nums.length;
        
        if(n == 1) return nums[0];
        
        int dp2=nums[0], dp1=Math.max(nums[0],nums[1]),dp=dp1;
        
        for(int i = 2; i < n; i++){
            dp = Math.max(dp1, dp2 + nums[i]);
            dp2 = dp1;
            dp1 = dp;
        }
        return dp;

    }
}










// Another solution

class Solution {
    public static int rob(int[] nums) 
	{
	    int ifRobbedPrevious = 0; 	// max monney can get if rob current house
	    int ifDidntRobPrevious = 0; // max money can get if not rob current house
	    
	    // We go through all the values, we maintain two counts, 1) if we rob this cell, 2) if we didn't rob this cell
	    for(int i=0; i < nums.length; i++) 
	    {
	    	  // If we rob current cell, previous cell shouldn't be robbed. So, add the current value to previous one.
	        int currRobbed = ifDidntRobPrevious + nums[i];
	        
	        // If we don't rob current cell, then the count should be max of the previous cell robbed and not robbed
	        int currNotRobbed = Math.max(ifDidntRobPrevious, ifRobbedPrevious); 
	        
	        // Update values for the next round
	        ifDidntRobPrevious  = currNotRobbed;
	        ifRobbedPrevious = currRobbed;
	    }
	    
	    return Math.max(ifRobbedPrevious, ifDidntRobPrevious);
	}
}





// Another solution



class Solution {
    public static int rob(int[] nums) 
	{
	    int ifRobbedPrevious = 0; 	// max monney can get if rob current house
	    int ifDidntRobPrevious = 0; // max money can get if not rob current house
	    
	    // We go through all the values, we maintain two counts, 1) if we rob this cell, 2) if we didn't rob this cell
	    for(int i=0; i < nums.length; i++) 
	    {
	    	// If we rob current cell, previous cell shouldn't be robbed. So, add the current value to previous one.
	        int currRobbed = ifDidntRobPrevious + nums[i];
	        
	        // If we don't rob current cell, then the count should be max of the previous cell robbed and not robbed
	        int currNotRobbed = Math.max(ifDidntRobPrevious, ifRobbedPrevious); 
	        
	        // Update values for the next round
	        ifDidntRobPrevious  = currNotRobbed;
	        ifRobbedPrevious = currRobbed;
	    }
	    return Math.max(ifRobbedPrevious, ifDidntRobPrevious);
	}
}




// DP


class Solution {
    public int rob(int[] num) {
        int rob = 0; //max monney can get if rob current house
        int notrob = 0; //max money can get if not rob current house
        for(int i=0; i<num.length; i++) {
            int currob = notrob + num[i]; //if rob current value, previous house must not be robbed
            notrob = Math.max(notrob, rob); //if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            rob = currob;
        }
        return Math.max(rob, notrob);
    }
}



// Another dp

class Solution {
    public int rob(int[] nums) {  
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];

        //Initialize an arrays to store the money
        int[] mark = new int[nums.length];

        //We can infer the formula from problem:mark[i]=max(num[i]+mark[i-2],mark[i-1])
        //so initialize two nums at first.
        mark[0] = nums[0];
        mark[1] = Math.max(nums[0], nums[1]);

        //Using Dynamic Programming to mark the max money in loop.
        for(int i=2;i<nums.length;i++){
            mark[i] = Math.max(nums[i]+mark[i-2], mark[i-1]);
        }
        return mark[nums.length-1];
    }
}



// Another solution


public class Solution {

    public int rob(int[] num) {
        int last = 0;
        int now = 0;
        int tmp;
        for (int n :num) {
            tmp = now;
            now = Math.max(last + n, now);
            last = tmp;
        }
        return now;        
    }
}


// concise solution


class Solution {
    public int rob(int[] nums) {
        if(nums.length==0) {
            return 0;
        }
        int[] dp = new int[nums.length+1];
        dp[1]=nums[0];
        for(int i=1;i<nums.length;i++) {
            dp[i+1]=Math.max(dp[i],dp[i-1]+nums[i]);
        }
        return dp[nums.length];
    }
}
