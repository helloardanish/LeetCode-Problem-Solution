/*
  
The problem seems to be a dynamic programming one. Hint: the tag also suggests that!
Here are the steps to get the solution incrementally.

Base cases:
if n <= 0, then the number of ways should be zero.
if n == 1, then there is only way to climb the stair.
if n == 2, then there are two ways to climb the stairs. 
One solution is one step by another; the other one is two steps at one time.

The key intuition to solve the problem is that given a number of stairs n, 
if we know the number ways to get to the points [n-1] and [n-2] respectively, 
denoted as n1 and n2 , then the total ways to get to the point [n] is n1 + n2. 
Because from the [n-1] point, we can take one single step to reach [n]. 
And from the [n-2] point, we could take two steps to get there.

The solutions calculated by the above approach are complete and non-redundant. 
The two solution sets (n1 and n2) cover all the possible cases on how the final step is taken. 
And there would be NO overlapping among the final solutions constructed from these two solution sets, 
because they differ in the final step.

Now given the above intuition, one can construct an array where each node stores the solution for each number n. 
Or if we look at it closer, it is clear that this is basically a fibonacci number, 
with the starting numbers as 1 and 2, instead of 1 and 1.

  
  
*/


class Solution {
    public int climbStairs(int n) {
        // base cases
        if(n <= 0) return 0;
        if(n == 1) return 1;
        if(n == 2) return 2;

        int one_step_before = 2;
        int two_steps_before = 1;
        int all_ways = 0;

        for(int i=2; i<n; i++){
            all_ways = one_step_before + two_steps_before;
            two_steps_before = one_step_before;
            one_step_before = all_ways;
        }
        return all_ways;
    }
}




/*

Brute-Force Approach

Base cases:
if n == 0, then the number of ways should be zero.
if n == 1, then there is only one way to climb the stair.
if n == 2, then there are two ways to climb the stairs. One solution is one step by another; the other one is two steps at one time.

We can reach ith step in one of the two ways:
Taking a single step from (i - 1)th step
Taking a step of two from (i - 2)th step.
So, the total number of ways to reach ith step is equal to sum of ways of reaching (i - 1)th step and ways of reaching (i - 2)th step.
Time complexity: O(2^n) - since size of recursion tree will be 2^n
Space Complexity: O(n) - space required for the recursive function call stack.


*/


class Solution
{
    public int climbStairs(int n)
    {
        if(n <= 2)
            return n;
        else
            return climbStairs(n - 1) + climbStairs(n - 2);
    }
}




// Arithmetic way

class Solution {
    public int climbStairs(int n) {
        if(n == 0 || n == 1 || n == 2){return n;}
        int[] mem = new int[n];
        mem[0] = 1;
        mem[1] = 2;
        for(int i = 2; i < n; i++){
            mem[i] = mem[i-1] + mem[i-2];
        }
        return mem[n-1];
    }
}






// dp idea explained

class Solution {
    /*
     * Ideas:
     * Use Dynamic Programming,
     * for each step, the stair could ether combine with the previous one or as a single step.
     * Ways to climb to ith stair is W(i) = W(i-1) + W(i-2)
     * where W(i-1) is when the ith stair is as a single step
     * and W(i-2) is when the ith stair is paired with the previous one.
     */
    public int climbStairs(int n) {
        int[] tmp = new int[n];
        if (n < 2){
            return 1;
        }
        tmp[0] = 1;
        tmp[1] = 2;
        for (int i = 2; i < n; i++){
            tmp[i] = tmp[i-1] + tmp[i-2];
        }
        return tmp[n-1];
    }
}







// Recustion (Top Down Approach)

/**
 * Complexity : Time: O(2^n) ; Space: O(n)
 */
class Solution {
    public int climbStairs(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}




// Recustion + Memorization (Top Down Approach)

/**
 * Complexity : Time: O(n) ; Space: O(n)
 */
class Solution {
    public int climbStairs(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(1, 1);
        memo.put(2, 2);
        return climbStairs(n, memo);
    }

    private int climbStairs(int n, Map<Integer, Integer> memo) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        memo.put(n, climbStairs(n - 1, memo) + climbStairs(n - 2, memo));
        return memo.get(n);
    }
}




// DP (Bottom Up Approach)

/**
 * Complexity : Time: O(n) ; Space: O(n)
 */
class Solution {
    public int climbStairs(int n) {
        if (n <= 1) {
            return 1;
        }
        
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
}



//DP + Optimization (Bottom Up Approach)

// To calculate the new value we only leverage the previous two values. So we don't need to use an array to store all the previous values.

/**
 * Complexity : Time: O(n) ; Space: O(1)
 */
class Solution {
    public int climbStairs(int n) {
        if (n <= 1) {
            return 1;
        }

        int prev1 = 1;
        int prev2 = 2;

        for (int i = 3; i <= n; i++) {
            int newValue = prev1 + prev2;
            prev1 = prev2;
            prev2 = newValue;
        }

        return prev2;
    }
}





// Fibonacci sequence same as above

class Solution {
    public int climbStairs(int n) {
        if(n < 0)
            return 0;
        if(n == 1)
            return 1;

        int[] store = new int[n];

        store[0] = 1;
        store[1] = 2;

        for(int i = 2; i < n; ++i)
            store[i] = store[i-1] + store[i-2];

        return store[n-1];
    }
}



/*

Variable a tells you the number of ways to reach the current step, 
and b tells you the number of ways to reach the next step. 
So for the situation one step further up, the old b becomes the new a, 
and the new b is the old a+b, 
since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

*/


class Solution {
    public int climbStairs(int n) {
        int a = 1, b = 1;
        while (n-- > 0)
            a = (b += a) - a;
        return a;
    }
}




// Time and space minimised


/**
 * Binets Method (Using Matrix Multiplication to find the Fibonacci Number)
 *
 * Time Complexity: O(log N)
 *
 * Space Complexity: O(1) -> Uses constant complexity
 *
 * N = Input number n
 */
class Solution {
    public int climbStairs(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n in invalid");
        }
        if (n <= 1) {
            return n;
        }

		int[][] q = { { 1, 1 }, { 1, 0 } };
        int[][] result = q;
        n--; // As we have already solved for n = 1. q[0][0] points to 2nd Fibonacci Number.
        while (n > 0) {
            if (n % 2 == 1) {
                result = multiplyMatrix(result, q);
                if (n == 1) {
                    break;
                }
                n--;
            }

            q = multiplyMatrix(q, q);
            n /= 2;
        }

        return result[0][0];
    }

    private int[][] multiplyMatrix(int[][] a, int[][] b) {
        int[][] c = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
            }
        }
        return c;
    }
}






// another


/**
 * Space Optimized Dynamic Programming
 *
 * DP[i] = DP[i-1] + DP[i-2]
 *
 * Time Complexity: O(N)
 *
 * Space Complexity: O(1)
 *
 * N = Input number n.
 */
class Solution {
    public int climbStairs(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n in invalid");
        }
        if (n <= 1) {
            return n;
        }

        int pre = 1; // n == 1
        int cur = 2; // n == 2
        for (int i = 3; i <= n; i++) {
            int sum = cur + pre;1
            pre = cur;
            cur = sum;
        }
        return cur;
    }
}

