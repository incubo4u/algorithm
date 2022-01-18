using System.Text;
public class Solution
{
  public IList<IList<string>> GroupAnagrams(string[] strs)
  {
    string dictKey;
    IList<IList<string>> result = new List<IList<string>>();
    var anagrams = new Dictionary<string, List<string>>();
    foreach (var word in strs)
    {
      dictKey = Hash(word);
      if (anagrams.ContainsKey(dictKey))
      {
        anagrams[dictKey].Add(word);
      }
      else
      {
        anagrams.Add(dictKey, new List<string>() { word });
      }
    }
    foreach (var list in anagrams.Values)
    {
      result.Add(list);
    }
    return result;
  }

  public string Hash(string word)
  {
    var letters = CountCharacters(word);
    var key = new StringBuilder();
    char a = 'a';
    for (int i = 0; i < 26; i++)
    {
      char asciiLetter = (char)((int)a + i);
      if (letters.ContainsKey(asciiLetter))
      {
        key.Append(asciiLetter);
        key.Append(letters[asciiLetter].ToString());
      }
    }
    return key.ToString();
  }

  public Dictionary<char, int> CountCharacters(string word)
  {
    char character;
    var letters = new Dictionary<char, int>();
    for (int i = 0; i < word.Length; i++)
    {
      character = word[i];
      if (letters.ContainsKey(character))
      {
        letters[character]++;
      }
      else
      {
        letters.Add(character, 1);
      }
    }
    return letters;
  }
}