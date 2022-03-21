/*

The idea is to iteratively generate combinations for all lengths from 1 to k. 
We start with a list of all numbers <= n as combinations for k == 1. 
When we have all combinations of length k-1, 
we can get the new ones for a length k with trying to add to each one all elements that are <= n and greater 
than the last element of a current combination.

*/


public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        if (k == 0 || n == 0 || k > n) return Collections.emptyList();
        List<List<Integer>> combs = new ArrayList<>();
        for (int i = 1; i <= n; i++) combs.add(Arrays.asList(i));
        for (int i = 2; i <= k; i++) {
            List<List<Integer>> newCombs = new ArrayList<>();
            for (int j = i; j <= n; j++) {
                for (List<Integer> comb : combs) {
                    if (comb.get(comb.size()-1) < j) {
                        List<Integer> newComb = new ArrayList<>(comb);
                        newComb.add(j);
                        newCombs.add(newComb);
                    }
                }
            }
            combs = newCombs;
        }
        return combs;
    }
}





// Backtracking

class Solution {
    public static List<List<Integer>> combine(int n, int k) {
		List<List<Integer>> combs = new ArrayList<List<Integer>>();
		combine(combs, new ArrayList<Integer>(), 1, n, k);
		return combs;
	}
	public static void combine(List<List<Integer>> combs, List<Integer> comb, int start, int n, int k) {
		if(k==0) {
			combs.add(new ArrayList<Integer>(comb));
			return;
		}
		for(int i=start;i<=n;i++) {
			comb.add(i);
			combine(combs, comb, i+1, n, k-1);
			comb.remove(comb.size()-1);
		}
	}
}



// DFS


public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> rslt = new ArrayList<List<Integer>>();
        dfs(new Stack<Integer>(), 1, n, k, rslt);
        return rslt;
    }
    
    private void dfs(Stack<Integer> path, int index, int n, int k, List<List<Integer>> rslt){
        // ending case
        if(k==0){
            List<Integer> list = new ArrayList<Integer>(path);
            rslt.add(list);
            return;
        }
        // recursion case
        for(int i = index;i <= n;i++){
            path.push(i);
            dfs(path, i+1, n, k-1, rslt);
            path.pop();
        }
    }
}
