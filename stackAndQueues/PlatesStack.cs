using System;
using System.Collections.Generic;
namespace stackAndQueues
{
    public class DinnerPlates
    {
        int count = 0;
        int limit;
        List<int> free = new List<int>();
        Dictionary<int, Stack<int>> plates = new Dictionary<int, Stack<int>>();
        public DinnerPlates(int capacity)
        {
            limit = capacity;
        }
        public void Push(int val)
        {
            if (count == 0 || free.Count == 0)
            {
                Stack<int> s = new Stack<int>();
                s.Push(val);
                plates.Add(count, s);
                if (limit > 1) { free.Add(count); }
                count++;
            }
            else
            {
                free.Sort();
                int stackLen = plates[free[0]].Count;
                if (stackLen < limit)
                {
                    plates[free[0]].Push(val);
                    if (stackLen + 1 == limit) { free.RemoveAt(0); }
                }
            }
        }
        public int Pop()
        {
            int popResult;
            for (int i = count - 1; i >= 0; i--)
            {
                if (plates[i].TryPop(out popResult))
                {
                    free.Add(i);
                    return popResult;
                }
            }
            return -1;
        }
        public int PopAtStack(int index)
        {
            if (index > count) { return -1; }
            int popResult;
            if (plates[index].TryPop(out popResult))
            {
                if (!free.Contains(index)) { free.Add(index); }
                return popResult;
            }
            else { return -1; }
        }
    }
}