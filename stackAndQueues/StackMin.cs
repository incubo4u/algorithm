using System;
using System.Collections.Generic;

namespace stackAndQueues
{
    public class StackMinimal
    {
        Node top;
        Stack minValue = new Stack();
        public class Node<T>
        {
            T data;
            Node next = null;
            public Node(T d)
            {
                data = d; 
            }
        }
        public T Pop()
        {
            if (top != null)
            {
                if (top.data == minValue.Peek())
                {
                    minValue.Pop();
                }
                T item = top.data;
                top = top.next;
                return item;
            }
            return null;
        }
        public void Push(T item)
        {
            if (minValue.Peek() >= item)
            {
                minValue.Push(item);
            }
            Node node = new Node(item);
            node.next = top;
            top = node;
        }
        public T Peek()
        {
            return top.data == null ? int.MaxValue: top.data ;
        }
        public T Min()
        {
            return minValue.Peek();
        }
    }
}
