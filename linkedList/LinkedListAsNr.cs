using System;
using System.Text;

namespace linkedList
{
    public static class NrFromLinkedList
    {
        public static Node AddRec(Node l1, Node l2, int carry)
        {
            if (l1 == null && l2 == null && carry == 0) { return null; }
            Node result = new Node(0);
            int value = carry;
            if (l1 != null)
            {
                value += l1.data;
            }
            if (l2 != null)
            {
                value += l2.data;
            }
            result.data = value % 10;
            if (l1 != null || l2 != null)
            {
                Node subsequent = AddRec(l1.next == null ? null : l1.next,
                                         l2.next == null ? null : l2.next,
                                         value >= 10 ? 1 : 0);
                result.next = subsequent;
            }
            return result;
        }
    }
}