public class Solution
{
  public int CharacterReplacement(string s, int k)
  {
    if (s.Length == 1) return 1;
    if (k == 0) return LongestSequenceOfSameChars(s);
    int windowStart = 0;
    int maxFreq = 0;
    int result = 0;
    Dictionary<char, int> charFreq = new Dictionary<char, int>();
    for (int windowEnd = 0; windowEnd < s.Length; windowEnd++)
    {
      if (charFreq.ContainsKey(s[windowEnd]))
      {
        charFreq[s[windowEnd]]++;
      }
      else
      {
        charFreq.Add(s[windowEnd], 1);
      }
      maxFreq = Math.Max(maxFreq, charFreq[s[windowEnd]]);
      while (windowEnd - windowStart + 1 - maxFreq > k)
      {
        charFreq[s[windowStart]]--;
        windowStart++;
      }
      result = Math.Max(windowEnd - windowStart + 1, result);
    }
    return result;
  }
  public int LongestSequenceOfSameChars(string s)
  {
    char current = s[0];
    int count = 0;
    int result = 0;
    for (int i = 0; i < s.Length; i++)
    {
      if (current == s[i])
      {
        count++;
      }
      else
      {
        count = 1;
        current = s[i];
      }
      result = Math.Max(result, count);
    }
    return result;
  }
}