/*


This is a very quick, O(n) reversal that times at 0ms in Leetcode OJ. 
The trick is to think of the first element as the new last item in the list. 
After reversing, this must be true. 
Then, we just move the element that pivot .next points to (the initial head of the list) and we move it to become the new head. 
This essentially grows the list backwards until the initial pivot no longer has anything to move.

For example; if we have a list [1, 2, 3, 4], the algorithm will do the following:

Set pivot to 1, set frontier to 2, keep head at 1
We see that pivot still has items after it, so set pivots .next to .next.next, and move the pivot to be set to the current head
Now move the head back to point to the new head, which is the frontier node we just set
Now reset frontier to pivots .next and repeat.
So with each iteration of the loop the list becomes:

[1, 2, 3, 4]
[2, 1, 3, 4]
[3, 2, 1, 4]
[4, 3, 2, 1]
Then we return the new final head which points to 4.

*/


public class Solution {
    public ListNode reverseList(ListNode head) {
        // is there something to reverse?
        if (head != null && head.next != null)
        {
            ListNode pivot = head;
            ListNode frontier = null;
            while (pivot != null && pivot.next != null)
            {
                frontier = pivot.next;
                pivot.next = pivot.next.next;
                frontier.next = head;
                head = frontier;
            }
        }

        return head;
    }
}





// Iterative


class Solution {
    public ListNode reverseList(ListNode head) {
        /* iterative solution */
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
}





// Recursive


class Solution {
    public ListNode reverseList(ListNode head) {
        /* recursive solution */
        return reverseListInt(head, null);
    }

    private ListNode reverseListInt(ListNode head, ListNode newHead) {
        if (head == null)
            return newHead;
        ListNode next = head.next;
        head.next = newHead;
        return reverseListInt(next, head);
    }
}


// another recursive

public class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null || head.next==null)
            return head;
        ListNode nextNode=head.next;
        ListNode newHead=reverseList(nextNode);
        nextNode.next=head;
        head.next=null;
        return newHead;
    }
}



// another recursive


public class Solution {
    public static ListNode reverseList(ListNode head) {
		ListNode result = new ListNode(0);
		ListNode p = null;
		while (head != null) {
			p = head;
			head = head.next;
			p.next = result.next;
			result.next = p;
		}
        return result.next;
    }
}




// same logic using iterative


public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr = null;
        ListNode temp = head;
        ListNode prev = null;
        while(temp != null){
            prev = curr;
            curr = temp;
            temp = curr.next;
            curr.next = prev;
        }
        return curr; 
    }
}

