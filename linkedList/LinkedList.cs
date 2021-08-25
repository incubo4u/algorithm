using System;

namespace linkedList
{
    public class Node
    {
        Node next = null;
        int data;
        Node(int d)
        {
            data = d;
        }
        public void AppendToTail(int d){
            Node end = new Node(d);
            Node n = this;
            while(n.next!=null){
                n = n.next;
            }
            n.next = end;
        }
    }
}
