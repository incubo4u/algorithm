public class Solution
{
  public int LengthOfLongestSubstring(string s)
  {
    HashSet<char> sub = new HashSet<char>();
    int p = 0;
    int longest = 0;
    if (s.Length == 0) { return 0; }
    if (s.Length == 1) { return 1; }
    sub.Add(s[0]);
    for (int i = 1; i < s.Length; i++)
    {
      char letter = s[i];
      if (!sub.Contains(letter))
      {
        sub.Add(letter);
        longest = Math.Max(longest,sub.Count);
      }
      else{
        longest = Math.Max(longest,sub.Count);
        while (s[p] != letter)
        {
          sub.Remove(s[p]);
          p++;
        }
        sub.Remove(s[p]);
        sub.Add(letter);
        p++;
      }
    }
    return longest;
  }
}
