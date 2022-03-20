// Tree traversal

public class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return null;
        
        int val = (t1 == null ? 0 : t1.val) + (t2 == null ? 0 : t2.val);
        TreeNode newNode = new TreeNode(val);
        
        newNode.left = mergeTrees(t1 == null ? null : t1.left, t2 == null ? null : t2.left);
        newNode.right = mergeTrees(t1 == null ? null : t1.right, t2 == null ? null : t2.right);
        
        return newNode;
    }
}


// Shared node


class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null) return t2;
        if (t2 == null) return t1;

        TreeNode node = new TreeNode(t1.val + t2.val);
        node.left = mergeTrees(t1.left, t2.left);
        node.right = mergeTrees(t1.right, t2.right);
        return node;
    }
}


// Recursive

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Recursive Solution
    // Time: O(n)
    // Space: O(height)
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
      if (t1 == null) {
        return t2;
      }

      if (t2 != null) {
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
      }

      return t1;
    }
}



// DFS


class Solution {
    // Iterative DFS
    // Time: O(n)
    // Space: O(height)
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
      if (t1 == null) {
        return t2;
      }
      // Use stack to help DFS
      Deque<TreeNode[]> stack = new LinkedList<>();
      stack.offerLast(new TreeNode[] {t1, t2});
      while (!stack.isEmpty()) {
        TreeNode[] cur = stack.pollLast();
        // no need to merge t2 into t1
        if (cur[1] == null) {
          continue;
        }
        // merge t1 and t2
        cur[0].val += cur[1].val;
        // if node in t1 == null, use node in t2 instead
        // else put both nodes in stack to merge
        if (cur[0].left == null) {
          cur[0].left = cur[1].left;
        } else {
          stack.offerLast(new TreeNode[] {cur[0].left, cur[1].left});
        }
        if (cur[0].right == null) {
          cur[0].right = cur[1].right;
        } else {
          stack.offerLast(new TreeNode[] {cur[0].right, cur[1].right});
        }
      }
      return t1;
    }
}




// Iterative BFS




class Solution {
    // Iterative BFS
    // Time: O(n)
    // Space: O(n)
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
      if (t1 == null) {
        return t2;
      }
      // Use stack to help DFS
      Queue<TreeNode[]> queue = new LinkedList<>();
      queue.offer(new TreeNode[] {t1, t2});
      while (!queue.isEmpty()) {
        TreeNode[] cur = queue.poll();
        // no need to merge t2 into t1
        if (cur[1] == null) {
          continue;
        }
        // merge t1 and t2
        cur[0].val += cur[1].val;
        // if node in t1 == null, use node in t2 instead
        // else put both nodes in stack to merge
        if (cur[0].left == null) {
          cur[0].left = cur[1].left;
        } else {
          queue.offer(new TreeNode[] {cur[0].left, cur[1].left});
        }
        if (cur[0].right == null) {
          cur[0].right = cur[1].right;
        } else {
          queue.offer(new TreeNode[] {cur[0].right, cur[1].right});
        }
      }
      return t1;
    }
}





// Another solution


class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return null;
        } else if (t2 == null) {
            return t1;
        } else if (t1 == null) {
            return t2;
        } else {
            TreeNode t = new TreeNode(t1.val + t2.val);
            t.left = mergeTrees(t1.left, t2.left);
            t.right = mergeTrees(t1.right, t2.right);
            return t;
        }
    }
}



// Another solution


class Solution {
    
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return null;
        if (t1 == null) return t2;
        if (t2 == null) return t1;
        
        TreeNode new_node = new TreeNode(t1.val + t2.val);
        
        new_node.left = mergeTrees(t1.left, t2.left);
        new_node.right = mergeTrees(t1.right, t2.right);
        
        return new_node;
    }
}



