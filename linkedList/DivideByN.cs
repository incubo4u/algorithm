using System;

namespace linkedList
{

    public static class DivideBy
    {

        public static Node DivideByInt(int n, Node head)
        {
            if (head == null)
            {
                return head;
            }
            var node = head;
            while (node.next != null)
            {
                if (node.next.data < n)
                {
                    var temp = head;
                    head = node.next;
                    node.next = node.next.next;
                    head.next = temp;
                }
                else
                {
                    node = node.next;
                }
            }
            return head;
        }
    }
}