'''

For simplicity, create a dummy node to which we attach nodes from lists. 
Iterate over lists using two-pointers and build up a resulting list so that values are monotonically increased.

Time: O(n)
Space: O(1)

'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
      
      
      
### without dummy

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
      
##same logic


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = ListNode()
        get = lambda x,y: x if x.val < y.val else y
        while l1 and l2:
            prev.next = prev = (mini := get(l1,l2))
            if mini == l1: l1 = l1.next
            else: l2 = l2.next
        prev.next = l1 or l2
        return head.next
      
      
      
## iteratively

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
      
      
      
# recursively  

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
          
          
          
'''

If both lists are non-empty, I first make sure a starts smaller, 
use its head as result, and merge the remainders behind it. 
Otherwise, i.e., if one or both are empty, I just return what's there.


'''

class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
      
      
      

      
'''

First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.


'''


class Solution:
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a
      
      
