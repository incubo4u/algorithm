using System;

namespace linkedList
{
    public static class RemoveNodeHeadless
    {
        public static bool RemoveNodeInPlace(Node node)
        {
            if (node == null && node.next == null)
            {
                return false;
            }
            node.data = node.next.data;
            node.next = node.next.next;
            return true;
        }
    }
}