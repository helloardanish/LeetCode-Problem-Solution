// Recursion


public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }
        
        ListNode mergeHead;
        if(l1.val < l2.val){
            mergeHead = l1;
            mergeHead.next = mergeTwoLists(l1.next, l2);
        }
        else{
            mergeHead = l2;
            mergeHead.next = mergeTwoLists(l1, l2.next);
        }
        return mergeHead;
    }
}


// Recursion

public ListNode mergeTwoLists(ListNode l1, ListNode l2){
		if(l1 == null) return l2;
		if(l2 == null) return l1;
		if(l1.val < l2.val){
			l1.next = mergeTwoLists(l1.next, l2);
			return l1;
		} else{
			l2.next = mergeTwoLists(l1, l2.next);
			return l2;
		}
}






// Another using same recursive approach






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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        //  Base Case
        if(l1 == null) return l2;
        if(l2 == null) return l1;

        ListNode res;
        boolean l1_is_smaller = (l1.val<l2.val);

        if( l1_is_smaller ){
            res = l1;   
            res.next = mergeTwoLists(l1.next,l2);
        }
        else{ 
            res = l2;   
            res.next = mergeTwoLists(l1,l2.next);
        }   

        return res;

    }

    //                                  *LOGIC*                                 
    //  We use a recurisve approach here, it requires us to make two decisions.  

    //                  1.  When will we stop our recursion?
    //
    //  If l1 is null? Well we just want to return the rest of l2.
    //  If l2 is null? Well we just want to return the rest of l1.

    //                  2.  When will we call our function again?
    //
    //  Assume 'l1' is smaller between 'l1' and 'l2'
    //  We want to set our 'res' to 'l1' and now we want to 
    //  find which is smaller between 'l1.next' and 'l2'
    //  So we call :   
    //                  res = l1;
    //                  res.next = mergeTwoLists(l1.next,l2);
    //  If 'l1' is smaller.

    //  Similarly if 'l2' is smaller 
    //  We want to call : 
    //                  res = l2;
    //                  res.next = mergeTwoLists(l1,l2.next);
    //  If 'l2' is smaller.


    //  Eventually, l1 or l2 will be null, our base case will be true
    //  we will return back out of our recursion building res in the process.
}






// Recursion minimized


class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode head = l1.val < l2.val ? l1 : l2;
        ListNode nonHead = l1.val < l2.val ? l2 : l1;

        head.next = mergeTwoLists(head.next, nonHead);

        return head;
    }
}


