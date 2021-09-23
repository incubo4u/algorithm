using System;
using System.Collections.Generic;

namespace stackAndQueues
{
    public class Queue
    {
        Node first;
        Node last;
        public class Node<T>
        {
            T data;
            Node next = null;
            public Node(T d)
            {
                data = d;
            }
        }
        public void Enqueue(T item)
        {
            if (first == null)
            {
                first = new Node(item);
                last = first;
            }
            else
            {
                last.next = new Node(item); ;
                last = last.next;
            }
        }
        public T Dequeue(){
            if( first != null ){
                T item = first.data;
                first = first.next;
                return item;
            }
            return null;
        }
    }
}