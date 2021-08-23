using System;
using System.Text;
namespace arrays
{
    public static class IsRotation
    {
        public static bool StringRotationCheckV2(string s1, string s2)
        {
            int len = s1.Length;
            if (len == s2.Length && len > 0)
            {
                string s1s1 = s1 + s2;
                return s1s1.Contains(s2);
            }
            return false;
        }

        //my first but worse solution
        public static bool StringRotationCheck(string s1, string s2)
        {
            if (s1.Length != s2.Length) { return false; }
            char[] str1 = s1.ToCharArray();
            char[] str2 = s2.ToCharArray();
            int index1 = 0;
            for (int index2 = s2.Length - 1; index2 > 0; index2--)
            {
                if (str2[index2] == str1[index1])
                {
                    int dif = s2.Length - 1 - index2;
                    for (; index1 < dif; index1++)
                    {
                        if (str1[index1] != str2[index2])
                        {
                            break;
                        }
                        index2++;
                    }
                    if (index1 == dif)
                    {
                        return s2.Contains(s1.Substring(index1 + 1));
                    }
                }
            }
            return false;
        }
    }
}