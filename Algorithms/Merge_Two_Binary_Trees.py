'''

Recursive solution.

If both trees are empty then we return empty.
Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
The right child is similar.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans
      
      
      
      
      
################ same recursive approach  #####################

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        return res
      
      
      
      
      
######### Another solution  #######################


class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
          
          
          
############   BFS   ####################



class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not (t1 and t2):
            return t1 or t2
        queue1, queue2 = collections.deque([t1]), collections.deque([t2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return t1
      
      
      
############## Same idea  ##########################


class Solution(object):
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2: return t1 or t2
        s = [(t1, t2)]
        while s:
            n1, n2 = s.pop()
            #nothing to add on
            if not n2: continue
            n1.val += n2.val
            #[#base]initialization, critical to check n2's corresponding child
            if not n1.left and n2.left: n1.left = TreeNode(0)
            if not n1.right and n2.right: n1.right = TreeNode(0)
            #[#stack] pairs, level by level add up
            s.append((n1.right, n2.right))
            s.append((n1.left, n2.left))
        return t1
      
      
      
############### iterative approach #############################



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        stack = []
        stack = [[t1,t2]]
        while stack:
            cur = stack.pop()
            if cur[0] == None or cur[1] == None:
                continue
            cur[0].val += cur[1].val
            if cur[0].left == None:
                cur[0].left = cur[1].left
            else:
                stack.append([cur[0].left,cur[1].left])
            if cur[0].right == None:
                cur[0].right = cur[1].right
            else:
                stack.append([cur[0].right,cur[1].right])
        return t1
      
      
      

      

################# Another solution #######################



class Solution(object):
    def mergeTrees(self, t1, t2):
        dummy = TreeNode(0)
        stack = [(t1, t2, dummy, 'l')]
        while stack:
            n1, n2, parent, lr = stack.pop()
            n = TreeNode((n1.val if n1 else 0 ) + (n2.val if n2 else 0 )) if n1 or n2 else None
            if lr == 'l': 
                parent.left = n 
            else:
                parent.right = n
                
            if n1 or n2:
                stack.append((n1 and n1.left, n2 and n2.left, n, 'l'))
                stack.append((n1 and n1.right, n2 and n2.right, n, 'r'))
            
        return dummy.left
      
      
      
      

      

############################## Python all in one solution ##################################


# Recursion pre-order
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        t = TreeNode(t1.val + t2.val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        
        return t

# Recursion in-order
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        tLeft = self.mergeTrees(t1.left, t2.left)
        t = TreeNode(t1.val + t2.val)
        t.left = tLeft
        t.right = self.mergeTrees(t1.right, t2.right)
        
        return t

# Recursion post-order
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        tLeft = self.mergeTrees(t1.left, t2.left)
        tRight = self.mergeTrees(t1.right, t2.right)
        t = TreeNode(t1.val + t2.val)
        t.left, t.right = tLeft, tRight
        
        return t

# Iterative pre-order
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        stack1 = [t1]
        stack2 = [t2]
        tRoot = TreeNode(t1.val + t2.val)
        stack = [tRoot]
        while len(stack) > 0:
            t1 = stack1.pop()
            t2 = stack2.pop()
            t = stack.pop()
            if t1.right is None and t2.right is None:
                pass
            elif t1.right is None:
                t.right = t2.right
            elif t2.right is None:
                t.right = t1.right
            else:
                t.right = TreeNode(t1.right.val + t2.right.val)
                stack1.append(t1.right)
                stack2.append(t2.right)
                stack.append(t.right)
            if t1.left is None and t2.left is None:
                pass
            elif t1.left is None:
                t.left = t2.left
            elif t2.left is None:
                t.left = t1.left
            else:
                t.left = TreeNode(t1.left.val + t2.left.val)
                stack1.append(t1.left)
                stack2.append(t2.left)
                stack.append(t.left)
        
        return tRoot

# Iterative in-order
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        stack1 = []
        stack2 = []
        stack = []
        tRoot = TreeNode(t1.val + t2.val)
        t = tRoot
        while len(stack1) > 0 or t1 is not None:
            while t1 is not None and t2 is not None:
                stack1.append(t1)
                stack2.append(t2)
                stack.append(t)
                # Note: need to delay going to left if one tree is null
                if t1.left is not None and t2.left is not None:
                    t.left = TreeNode(t1.left.val + t2.left.val)
                    t = t.left
                t1, t2 = t1.left, t2.left
            if t1 is not None:
                t.left = t1
            if t2 is not None:
                t.left = t2
            t1, t2, t = stack1.pop(), stack2.pop(), stack.pop()
            if t1.right is None and t2.right is None:
                t1 = t2 = None
            elif t1.right is None:
                t.right = t2.right
                t1 = t2 = None
            elif t2.right is None:
                t.right = t1.right
                t1 = t2 = None
            else:
                t.right = TreeNode(t1.right.val + t2.right.val)
                t1, t2, t = t1.right, t2.right, t.right            
        
        return tRoot

# BFS
from collections import deque
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        q1, q2, q = deque(), deque(), deque()
        tRoot = TreeNode(t1.val + t2.val)
        t = tRoot
        q1.append(t1)
        q2.append(t2)
        q.append(t)
        
        while len(q1) > 0:
            t1, t2, t = q1.popleft(), q2.popleft(), q.popleft()
            if t1.left is None and t2.left is None:
                pass
            elif t1.left is None:
                t.left = t2.left
            elif t2.left is None:
                t.left = t1.left
            else:
                t.left = TreeNode(t1.left.val + t2.left.val)
                q1.append(t1.left)
                q2.append(t2.left)
                q.append(t.left)
            if t1.right is None and t2.right is None:
                pass
            elif t1.right is None:
                t.right = t2.right
            elif t2.right is None:
                t.right = t1.right
            else:
                t.right = TreeNode(t1.right.val + t2.right.val)
                q1.append(t1.right)
                q2.append(t2.right)
                q.append(t.right)
        
        return tRoot
      
      
      
      
##########################  Minimized solution  #####################


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None
        
        if root1 is None:
            res = root2
        elif root2 is None:
            res = root1
        else:
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left, root2.left)
            res.right = self.mergeTrees(root1.right, root2.right)
            
        return res
      
      
      
      
######## Another solution

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root1.val  += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        else:
            return root1 or root2
