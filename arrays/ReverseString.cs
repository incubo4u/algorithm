using System;

namespace arrays
{
    static class ReverseString
    {
        public static string Reverse(string str)
        {
            char[] charTab = str.ToCharArray();
            int len = charTab.Length;
            for (int i = 0; i < len/2; i++)
            {
                char temp = charTab[i];
                charTab[i] = charTab[len - 1 - i];
                charTab[len - 1 - i] = temp;
            }
            return new string(charTab);
        }
    }
}
