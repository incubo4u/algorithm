using System;

namespace linkedList
{
    public static class FindFromTheEnd
    {
        public static Node FindNode(Node head, int k)
        {
            if(k<=0){ throw new IndexOutOfRangeException();}
            if (k == 1) { return head; }
            int lenght = 0;
            var node = head;
            while (node != null)
            {
                lenght++;
                node = node.next;
            }
            node = head;
            if (k > lenght) { throw new IndexOutOfRangeException(); }
            for (int i = 1; i < lenght - k; i++)
            {
                node = node.next;
            }
            return node;
        }
    }
}