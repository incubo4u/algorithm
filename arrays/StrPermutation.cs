using System;
using System.Collections.Generic;
namespace arrays
{
    static class StrPermutation
    {
        public static bool IsPermutationOf(string s, string s1)
        {
            if (s.Length != s1.Length) { return false; }
            int len = s.Length;
            var dict = new Dictionary<char, int>();
            for (int i = 0; i < len; i++)
            {
                char letter = s[i];
                if (dict.ContainsKey(letter))
                {
                    dict[letter]++;
                }
                else
                {
                    dict.Add(letter, 1);
                }
            }
            for (int j = 0; j < len; j++)
            {
                char letter = s1[j];
                if (dict.ContainsKey(letter) && dict[letter] > 0)
                {
                    dict[letter]--;
                }
                else
                {
                    return false;
                }
            }
            return true;
        }
    }
}



