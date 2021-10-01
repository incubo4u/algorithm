using System;
using System.Collections.Generic;
namespace stackAndQueues
{
    public class QueueOfTwoStacks
    {
        Stack<int> PushStack = new Stack<int>();
        Stack<int> PopStack = new Stack<int>();
        public void Push(int x)
        {
            PushStack.Push(x);
        }
        public void PushAllToPopStack()
        {
            while (PushStack.Count != 0)
            {
                PopStack.Push(PushStack.Pop());
            }
        }
        public int Pop()
        {
            if (PopStack.Count == 0)
            {
                PushAllToPopStack();
            }
            return PopStack.Pop();
        }
        public int Peek()
        {
            if (PopStack.Count == 0)
            {
                PushAllToPopStack();
            }
            return PopStack.Peek();
        }
        public bool Empty()
        {
            if (PushStack.Count == 0 && PopStack.Count == 0)
            {
                return true;
            }
            return false;
        }
    }
}
