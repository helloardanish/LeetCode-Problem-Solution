'''

The idea is to keep 2 pointers for current and next node and then iterate through nodes and reconnect nodes. 
The best way to understand this solution is to take some small list, 
for example 1 -> 2 -> 3 -> 4 -> None and see what is going on on the each step.

In the beginning curr = None, nxt = 1.
On the first step we have: tmp = 2, nxt.next = None, 
curr = 1, nxt = 2. So what we have is the following: None <- 1 2 -> 3 -> 4 -> None. 
That is we cut one link between 1 and 2 and create new link 1 -> None.
On the next step we have None <- 1 <- 2 3 -> 4 -> None and so on.
Try to draw it on the paper, step by step, it is the best way to feel it.

Complexity:
Time complexity is O(n), space is O(1).


'''



class Solution:
    def reverseList(self, head):
        curr = None
        nxt = head
        while nxt:
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
            
        return curr
      
      


# Iterative


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
      
      
# Recursive


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
      
      
      
## minimised


class Solution:
    def reverseList(self, head, last = None):
        if not head:
            return last
        next = head.next
        head.next = last
        return self.reverseList(next, head)
      
      
      
## another

class Solution:
    def reverseList(self, head):
        prev = None
        while head: head.next, head, prev = prev, head.next, head
        return prev
      
      
## another

class Solution:
    def reverseList(self, head):
        prev = None
        while head: head.next, prev, head = prev, head, head.next
        return prev
      
      
      
