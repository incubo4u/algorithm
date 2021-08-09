using System;
using System.Collections.Generic;
namespace arrays
{
    static class SpaceUrlEncoding
    {
        //string has enough blanks at the end 
        //so that the length of the array does not need to be increased
        public static string Encode(string str, int realLen)
        {
            if (realLen == 0 || str.Length == 0) { return ""; }
            char[] input = str.ToCharArray();
            int rightIndex = str.Length - 1;
            int leftIndex = realLen - 1;
            while (leftIndex != 0)
            {
                if (input[leftIndex] == ' ')
                {
                    input[rightIndex] = '0';
                    input[rightIndex - 1] = '2';
                    input[rightIndex - 2] = '%';
                    rightIndex -= 3; leftIndex--;
                }
                else
                {
                    char temp = input[leftIndex];
                    input[leftIndex] = input[rightIndex];
                    input[rightIndex] = temp;
                    leftIndex--; rightIndex--;
                }
            }
            return new string(input);
        }
    }
}
