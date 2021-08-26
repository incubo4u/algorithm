using System;

namespace linkedList
{
    public static class RemoveDuplicatesNoBuffer
    {
        public static void RemoveDuplicates(Node head)
        {
            var current = head;
            var compared = current.next;
            while (current != null)
            {
                while (compared.next != null)
                {
                    if (compared.next.data == current.data)
                    {
                        compared.next = compared.next.next;
                    }
                    else
                    {
                        compared = compared.next;
                    }
                }
                compared = current.next;
            }
        }
    }
}