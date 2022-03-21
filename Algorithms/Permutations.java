/*

Iterative


The basic idea is, to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, 
in every possible position.
For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>> (let's call it "answer").
Then, 2 can be added in front or after 1. So we have to copy the List in answer (it's just {1}), add 2 in position 0 of {1}, 
then copy the original {1} again, and add 2 in position 1. Now we have an answer of {{2,1},{1,2}}. 
There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, and add 3 into position 1, 
then do the same thing for position 3. Finally we have 2*3=6 lists in answer, which is what we want.



*/


class Solution {
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (num.length ==0) return ans;
        List<Integer> l0 = new ArrayList<Integer>();
        l0.add(num[0]);
        ans.add(l0);
        for (int i = 1; i< num.length; ++i){
            List<List<Integer>> new_ans = new ArrayList<List<Integer>>(); 
            for (int j = 0; j<=i; ++j){            
               for (List<Integer> l : ans){
                   List<Integer> new_l = new ArrayList<Integer>(l);
                   new_l.add(j,num[i]);
                   new_ans.add(new_l);
               }
            }
            ans = new_ans;
        }
        return ans;
    }
}


// Backtracking

class Solution {
    public List<List<Integer>> permute(int[] nums) {
       List<List<Integer>> list = new ArrayList<>();
       // Arrays.sort(nums); // not necessary
       backtrack(list, new ArrayList<>(), nums);
       return list;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
       if(tempList.size() == nums.length){
          list.add(new ArrayList<>(tempList));
       } else{
          for(int i = 0; i < nums.length; i++){ 
             if(tempList.contains(nums[i])) continue; // element already exists, skip
             tempList.add(nums[i]);
             backtrack(list, tempList, nums);
             tempList.remove(tempList.size() - 1);
          }
       }
    }
}





// Bottom up approach



public class Solution {
   public List<List<Integer>> permute(int[] nums) {
		List<List<Integer>> permutations = new ArrayList<>();
		if (nums.length == 0) {
			return permutations;
		}

		collectPermutations(nums, 0, new ArrayList<>(), permutations);
		return permutations;
    }

	private void collectPermutations(int[] nums, int start, List<Integer> permutation,
 			List<List<Integer>>  permutations) {
		
		if (permutation.size() == nums.length) {
			permutations.add(permutation);
			return;
		}

		for (int i = 0; i <= permutation.size(); i++) {
			List<Integer> newPermutation = new ArrayList<>(permutation);
			newPermutation.add(i, nums[start]);
			collectPermutations(nums, start + 1, newPermutation, permutations);
		}
	}
}


//Code flow

/*
nums = 1,2,3

start = 0, permutation = []
i = 0, newPermutation = [1]
	start = 1, permutation = [1]
	i = 0, newPermutation = [2, 1]
		start = 2, permutation = [2, 1]
		i = 0, newPermutation = [3, 2, 1]
		i = 1, newPermutation = [2, 3, 1]
		i = 2, newPermutation = [2, 1, 3]
	i = 1, newPermutation = [1, 2]
		start = 2, permutation = [1, 2]
		i = 0, newPermutation = [3, 1, 2]
		i = 1, newPermutation = [1, 3, 2]
		i = 2, newPermutation = [1, 2, 3]
    
*/


// Base case and build approach


public class Solution {
   public List<List<Integer>> permute(int[] nums) {
		return permute(Arrays.stream(nums).boxed().collect(Collectors.toList()));
   }

	private List<List<Integer>> permute(List<Integer> nums) {
		List<List<Integer>> permutations = new ArrayList<>();
		if (nums.size() == 0) {
			return permutations;
		}
		if (nums.size() == 1) {
			List<Integer> permutation = new ArrayList<>();
			permutation.add(nums.get(0));
			permutations.add(permutation);
			return permutations;
		}
		
		List<List<Integer>> smallPermutations = permute(nums.subList(1, nums.size()));
		int first = nums.get(0);
		for(List<Integer> permutation : smallPermutations) {
			for (int i = 0; i <= permutation.size(); i++) {
				List<Integer> newPermutation = new ArrayList<>(permutation);
				newPermutation.add(i, first);
				permutations.add(newPermutation);
			}
		}
		return permutations;
	}
}


// Code flow

/*

nums = 1,2,3

smallPermutations(2, 3)
	smallPermutations(3)
		return [[3]]
	first = 2
 		permutation = [3]
			i = 0, newPermutation = [2, 3]
			i = 1, newPermutation = [3, 2]
	return [[2, 3], [3, 2]]
first = 1
 	permutation = [2, 3]
		i = 0, newPermutation = [1, 2, 3]
		i = 1, newPermutation = [2, 1, 3]
		i = 2, newPermutation = [2, 3, 1]
 	permutation = [3, 2]
		i = 0, newPermutation = [1, 3, 2]
		i = 1, newPermutation = [3, 1, 2]
		i = 2, newPermutation = [3, 2, 1]
    
*/





// Recursive Backtracking



/**
 * Recursive Backtracking. In this solution passing the index of the nums that
 * needs to be set in the current recursion.
 *
 * Time Complexity: O(N * N!). Number of permutations = P(N,N) = N!. Each
 * permutation takes O(N) to construct
 *
 * T(n) = n*T(n-1) + O(n)
 * T(n-1) = (n-1)*T(n-2) + O(n-1)
 * ...
 * T(2) = (2)*T(1) + O(2)
 * T(1) = O(N) -> To convert the nums array to ArrayList.
 *
 * Above equations can be added together to get:
 * T(n) = n + n*(n-1) + n*(n-1)*(n-2) + ... + (n....2) + (n....1) * n
 *      = P(n,1) + P(n,2) + P(n,3) + ... + P(n,n-1) + n*P(n,n)
 *      = (P(n,1) + ... + P(n,n)) + (n-1)*P(n,n)
 *      = Floor(e*n! - 1) + (n-1)*n!
 *      = O(N * N!)
 *
 * Space Complexity: O(N). Recursion stack.
 *
 * N = Length of input array.
 */
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return result;
        }

        permutationsHelper(result, nums, 0);
        return result;
    }

    private void permutationsHelper(List<List<Integer>> result, int[] nums, int start) {
        if (start == nums.length - 1) {
            List<Integer> list = new ArrayList<>();
            for (int n : nums) {
                list.add(n);
            }
            result.add(list);
            return;
        }
        for (int i = start; i < nums.length; i++) {
            swap(nums, start, i);
            permutationsHelper(result, nums, start + 1);
            swap(nums, start, i);
        }
    }

    private void swap(int[] nums, int x, int y) {
        int t = nums[x];
        nums[x] = nums[y];
        nums[y] = t;
    }
}






// Iterative Solution



/**
 * Iterative Solution
 *
 * The idea is to add the nth number in every possible position of each
 * permutation of the first n-1 numbers.
 *
 * Time Complexity: O(N * N!). Number of permutations = P(N,N) = N!. Each
 * permutation takes O(N) to construct
 *
 * T(n) = (x=2->n) ∑ (x-1)!*x(x+1)/2
 *      = (x=1->n-1) ∑ (x)!*x(x-1)/2
 *      = O(N * N!)
 *
 * Space Complexity: O((N-1) * (N-1)!) = O(N * N!). All permutations of the first n-1 numbers.
 *
 * N = Length of input array.
 */
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return result;
        }

        result.add(Arrays.asList(nums[0]));

        for (int i = 1; i < nums.length; i++) {
            List<List<Integer>> newResult = new ArrayList<>();
            for (List<Integer> cur : result) {
                for (int j = 0; j <= i; j++) {
                    List<Integer> newCur = new ArrayList<>(cur);
                    newCur.add(j, nums[i]);
                    newResult.add(newCur);
                }
            }
            result = newResult;
        }

        return result;
    }
}




// Recursive Backtracking using visited array




/**
 * Recursive Backtracking using visited array.
 *
 * Time Complexity: O(N * N!). Number of permutations = P(N,N) = N!. Each
 * permutation takes O(N) to construct
 *
 * T(n) = n*T(n-1) + O(n)
 * T(n-1) = (n-1)*T(n-2) + O(n)
 * ...
 * T(2) = (2)*T(1) + O(n)
 * T(1) = O(n)
 *
 * Above equations can be added together to get:
 * T(n) = n (1 + n + n*(n-1) + ... + (n....2) + (n....1))
 *      = n (P(n,0) + P(n,1) + P(n,1) + ... + P(n,n-1) + P(n,n))
 *      = n * Floor(e*n!)
 *      = O(N * N!)
 *
 * Space Complexity: O(N). Recursion stack + visited array
 *
 * N = Length of input array.
 */
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null) {
            return result;
        }

        helper(result, new ArrayList<>(), nums, new boolean[nums.length]);
        return result;
    }

    private void helper(List<List<Integer>> result, List<Integer> temp, int[] nums, boolean[] visited) {
        if (temp.size() == nums.length) {
            result.add(new ArrayList<>(temp));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            temp.add(nums[i]);
            visited[i] = true;
            helper(result, temp, nums, visited);
            visited[i] = false;
            temp.remove(temp.size() - 1);
        }
    }
}

