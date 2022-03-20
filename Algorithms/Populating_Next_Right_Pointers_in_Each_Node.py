'''

Since we are manipulating tree nodes on the same level, it's easy to come up with
a very standard BFS solution using queue. But because of next pointer, we actually
don't need a queue to store the order of tree nodes at each level, we just use a next
pointer like it's a link list at each level; In addition, we can borrow the idea used in
the Binary Tree level order traversal problem, which use cur and next pointer to store
first node at each level; we exchange cur and next every time when cur is the last node
at each level.

'''



class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        
        if not root:
            return None
        cur  = root
        next = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left
                
                
                

## Simply do it level by level, using the next-pointers of the current level to go through the current level and set the next-pointers of the next level.

def connect(self, root):
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            root = root.next
        root = next
        
        

        
## BFS

class Solution:
    def connect(self, root):
        if not root: return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root
      
      
      
## DFS

class Solution:
    def connect(self, root):
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root
      
      
      
##  BFS - Space-Optimized Appraoch


class Solution:
    def connect(self, root):
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next
                
        return head
      
      
      
      
############ Another solution  #######################



# Recursive
def connect(self, root):
    if root and root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
 
# BFS       
def connect(self, root):
    if not root:
        return 
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)
    
# DFS 
def connect(self, root):
    if not root:
        return 
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            stack.append(curr.right)
            stack.append(curr.left)
            
            
            
            
            
            
########### Another solution  #######################


class Solution:
    def connect(self, root):
        if not root or not root.left: return root
        
        self.connect(root.left)
        self.connect(root.right)
        
        lft = root.left
        rgh = root.right
        lft.next = rgh

        while lft.right: 
            lft = lft.right
            rgh = rgh.left
            lft.next = rgh
        
        return root
      
      
      
      
### next pointer ###


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None
        
        leftMost = root
        while leftMost.left:
            head = leftMost
            leftMost = head.left
            while head:
                head.left.next = head.right
                if head.next != None:
                    head.right.next = head.next.left
                head = head.next
        return root
      
      
