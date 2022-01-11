public class Solution
{
  public bool IsAnagram(string s, string t)
  {
    Dictionary<char, int> times = new Dictionary<char, int>();
    if (s.Length != t.Length) { return false; }
    foreach (var letter in s)
    {
      if (times.ContainsKey(letter))
      {
        times[letter]++;
      }
      else { times.Add(letter, 1); }
    }
     foreach (var letter in t)
    {
      if (!times.ContainsKey(letter))
      {
        return false;
      }
      else
      {
        times[letter]--;
        if (times[letter] < 0) { return false; }
      }
    }
    return true;
  }
}