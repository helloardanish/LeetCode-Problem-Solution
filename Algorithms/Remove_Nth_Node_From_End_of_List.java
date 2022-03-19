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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode start = new ListNode(0);
        ListNode slow = start, fast = start;
        slow.next = head;

        //Move fast in front so that the gap between slow and fast becomes n
        for(int i=1; i<=n+1; i++)   {
            fast = fast.next;
        }
        //Move fast to the end, maintaining the gap
        while(fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        //Skip the desired node
        slow.next = slow.next.next;
        return start.next;
    }
}


// Another solution



public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode newHead = new ListNode(0);
       newHead.next = head;
       ListNode p = newHead;
       ListNode runner = newHead;
       while(n>0){
           runner = runner.next;
           n--;
       }
       while(runner.next!=null){
           runner = runner.next;
           p=p.next;
       }
       p.next = p.next.next;
       return newHead.next;
    }
    
}




// Another solution



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
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode headNode = new ListNode(9527);
        headNode.next = head;
        ListNode fastNode = headNode;
        ListNode slowNode = headNode;
        while(fastNode.next != null){
        	if(n <= 0)
        		slowNode = slowNode.next;
        	fastNode = fastNode.next;
        	n--;
        }
        if(slowNode.next != null)
        	slowNode.next = slowNode.next.next;
        return headNode.next;
    }
}
