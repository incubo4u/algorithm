using System;

namespace linkedList
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
    public static class Solution
    {
        public static ListNode MergeTwoLists(ListNode l1, ListNode l2)
        {
            if (l1 == null && l2 == null) { return null; }
            if (l1 == null) { return l2; }
            if (l2 == null) { return l1; }
            ListNode head = l1;
            ListNode toInsert = l2;
            if (l2.val < l1.val)
            {
                head = l2;
                toInsert = l1;
            }
            ListNode node = head;
            while (toInsert != null)
            {
                while (node.next != null && toInsert.val >= node.next.val)
                {
                    node = node.next;
                }
                if (node.next != null)
                {
                    var nextNodeOfInsertList = toInsert.next;
                    var temp = node.next;
                    node.next = toInsert;
                    node.next.next = temp;
                    toInsert = nextNodeOfInsertList;
                    node = node.next;
                    continue;
                }
                node.next = toInsert;
                break;
            }
            return head;
        }
    }
}