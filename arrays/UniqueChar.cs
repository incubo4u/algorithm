using System;
// implement an algorithm that checks whether a string contains only unique characters
// without additional data structures
namespace arrays
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            System.Console.WriteLine(HaveOnlyUniqueChar(str));
        }

        private static bool HaveOnlyUniqueChar(string str)
        {
            char[] charTab = str.ToCharArray();
            Array.Sort(charTab);
            int len = charTab.Length;
            int i = 1;
            while (i < len)
            {
                if (charTab[i - 1] == charTab[i])
                {
                    return false;
                }
                i++;
            }
            return true;
        }
    }
}
