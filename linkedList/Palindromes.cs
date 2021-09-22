using System;

namespace linkedList
{
    public static class Palindrome
    {
        public static int GetLenght(Node head)
        {
            int len = 1;
            while (head.next != null)
            {
                len++;
                head = head.next;
            }
            return len;
        }
        public static Node Reverse(Node head)
        {
            Node next = null;
            Node prev = null;
            while (head != null)
            {
                next = head.next;
                head.next = prev;
                prev = head;
                head = next;
            }
            return prev;
        }
        public static bool IsPalindrome(Node head)
        {
            if (head == null) { return false; }
            if (head.next == null) { return true; }
            if (head.next.data != head.data && head.next.next == null) { return false; }
            if (head.next.data == head.data && head.next.next == null) { return true; }
            Node pointer = head;
            int len = GetLenght(head);
            if (len == 3) { return head.next.next.data == head.data; }
            for (int i = 0; i < (len / 2) - 1; i++) { pointer = pointer.next; }
            if (len % 2 != 0) { pointer = pointer.next; }
            Node smallHead = pointer.next;
            pointer.next = null;
            pointer = smallHead;
            smallHead = Reverse(pointer);
            while (head != null && smallHead != null)
            {
                if (head.data == smallHead.data)
                {
                    head = head.next;
                    smallHead = smallHead.next;
                }
                else { return false; }
            }
            return true;
        }
    }
}