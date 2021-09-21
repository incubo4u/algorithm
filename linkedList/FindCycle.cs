using System;


namespace linkedList
{
    public static class Cycle
    {
        public static bool HasCycle(Node head)
        {
            if (head == null || head.next == null) { return false; }
            Node stepOne = head;
            Node stepTwo = head;
            while (stepOne != null && stepTwo != null)
            {
                stepOne = stepOne.next == null ? null : stepOne.next;
                stepTwo = stepTwo.next == null ||
                          stepTwo.next.next == null ? null : stepTwo.next.next;
                if (stepOne == stepTwo) { return true; }
            }
            return false;
        }
        public static Node FindCycle(Node head)
        {
            if (head == null || head.next == null) { return null; }
            Node stepOne = head;
            Node stepTwo = head;
            int steps = 0;
            while (stepOne != null && stepTwo != null)
            {
                steps++;
                stepOne = stepOne.next == null ? null : stepOne.next;
                stepTwo = stepTwo.next == null ||
                          stepTwo.next.next == null ? null : stepTwo.next.next;
                if (stepOne == stepTwo) { 
                    stepOne = head;
                    for (int i = 0; i < steps; i++)
                    {
                        stepOne = stepOne.next;
                        stepTwo = stepTwo.next;
                    }
                    if(stepOne == stepTwo){ return stepOne.next; }
                }
            }
            return null;
        }
    }
}