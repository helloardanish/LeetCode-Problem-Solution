'''

While slow moves one step forward, fast moves two steps forward.
Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
For example, head = [1, 2, 3, 4, 5], I bolded the slow and fast in the list.
step 0: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
step 1: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
step 2: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
end because fast cannot move forward anymore and return [3, 4, 5]


'''
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
      
      
########### Reducing code #####################



class Solution:
    def middleNode(self, head):
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head

