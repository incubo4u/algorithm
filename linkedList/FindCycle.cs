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
            if (head.next == head) { return head; }
            Node stepOne = head;
            Node stepTwo = head;
            while (stepOne != null && stepTwo != null)
            {
                stepOne = stepOne.next == null ? null : stepOne.next;
                stepTwo = stepTwo.next == null ||
                          stepTwo.next.next == null ? null : stepTwo.next.next;
                if (stepOne == stepTwo)
                {
                    if (head.next == stepTwo) { return head; }
                    stepOne = head;
                    while (stepTwo != stepOne)
                    {
                        stepOne = stepOne.next;
                        stepTwo = stepTwo.next;
                    }
                    return stepOne;
                }
            }
            return null;
        }
    }
}