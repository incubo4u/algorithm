using System;
using System.Collections.Generic;

namespace stackAndQueues
{
    public class Stack
    {
        Node top;
        public class Node<T>
        {
            T data;
            Node next = null;
            public Node(T d)
            {
                data = d;
            }
        }
        public T Pop(){
            if(top != null){
                T item = top.data;
                top = top.next;
                return item;
            }
            return null;
        }
        public void Push(T item){
            Node node = new Node(item);
            node.next = top;
            top = node;
        }
        public T Peek(){
            return top.data;
        }
    }
}