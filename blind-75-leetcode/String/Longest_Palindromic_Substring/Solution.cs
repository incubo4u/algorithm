using System.Text;
public class Solution
{
  public static string LongestPalindrome(string s)
  {
    string result = "";
    for (int i = 0; i < s.Length; i++)
    {
      string oddSub = FindPalindrome(s, i, i);
      string evenSub = FindPalindrome(s, i, i + 1);
      if (oddSub.Length > result.Length) { result = oddSub; }
      if (evenSub.Length > result.Length) { result = evenSub; }
    }
    return result;
  }
  public static string FindPalindrome(string s, int l, int r)
  {
    while (l >= 0 && r < s.Length && s[l] == s[r])
    {
      l--; r++;
    }
    l++; r--;
    return s.Substring(l, r - l + 1);
  }
}