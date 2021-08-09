using System;
using System.Text;
namespace arrays
{
    static class CountBasedCompression
    {

        public static string Compress(string str)
        {
            char[] input = str.ToCharArray();
            int len = input.Length;
            int lenAfret = GetAfterCompressionLenght(input);
            if (lenAfret > len) { return str; }
            var sb = new StringBuilder();
            char currentLetter = input[0];
            int count = 1;
            for (int i = 1; i < len; i++)
            {
                if (currentLetter == input[i])
                {
                    count++;
                }
                else
                {
                    sb.Append(currentLetter);
                    sb.Append(count);
                    currentLetter = input[i];
                    count = 1;
                }
            }
            sb.Append(currentLetter);
            sb.Append(count);
            return sb.ToString();
        }

        public static int GetAfterCompressionLenght(char[] str)
        {
            if (str.Length == 0 || str.Length == 1) { return str.Length; }
            int count = 1;
            int size = 0;
            char currentLetter = str[0];
            for (int i = 0; i < str.Length; i++)
            {
                char letter = str[i];
                if (letter == currentLetter) { count++; }
                else
                {
                    size += 1 + count.ToString().Length;
                    count = 1;
                    currentLetter = str[i];
                }
            }
            size += 1 + count.ToString().Length;
            return size;
        }
    }
}