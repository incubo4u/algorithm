public class Solution
{
  public bool IsPalindrome(string s)
  {
    int start = 0;
    int end = s.Length - 1;
    while (start < end)
    {
      if (!char.IsLetterOrDigit(s[start]))
      {
        start++;
      }
      else if (!char.IsLetterOrDigit(s[end]))
      {
        end--;
      }
      else if (char.ToLower(s[start]) != char.ToLower(s[end])) { return false; }
      else
      {
        start++;
        end--;
      }
    }
    return true;
  }
}