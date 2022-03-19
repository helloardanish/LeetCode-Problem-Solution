/*


While slow moves one step forward, fast moves two steps forward.
Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
For example, head = [1, 2, 3, 4, 5], I bolded the slow and fast in the list.
step 0: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
step 1: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
step 2: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
end because fast cannot move forward anymore and return [3, 4, 5]



*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}


// Another solution

/*

First, we find the length of linked list; then find the middle point and get that node.

*/


class Solution {
    public ListNode middleNode(ListNode head) {
        if(head == null) return head;

        int len = 0;
        ListNode current = head;
        while(current != null) {
            len++;
            current = current.next;
        }
        
        len /= 2;
        current = head;
        while(len > 0) {
            current = current.next;
            len--;
        }
        
        return current;
    }
}


// Same logic


public ListNode middleNode(ListNode head) {
    ListNode curr = head;
    
    int total = 0;
    while(curr != null){
        total++;
        curr = curr.next;
    }        
    
    //find the middle one
    total = total/2 + 1;
    
    ListNode cur = head;
    for(int i = 1; i < total; ++i){
        cur = cur.next;
    }
    
    return cur;
}
