public class Solution
{
  public bool IsAnagram(string s, string t)
  {
    Dictionary<char, int> times = new Dictionary<char, int>();
    if (s.Length != t.Length) { return false; }
    for (int i = 0; i < s.Length; i++)
    {
      if (times.ContainsKey(s[i]))
      {
        times[s[i]]++;
      }
      else { times.Add(s[i], 1); }
    }
    for (int j = 0; j < t.Length; j++)
    {
      if (!times.ContainsKey(t[j]))
      {
        return false;
      }
      else
      {
        times[t[j]]--;
        if (times[t[j]] < 0) { return false; }
      }
    }
    return true;
  }
}