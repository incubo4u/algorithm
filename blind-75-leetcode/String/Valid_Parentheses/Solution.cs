public class Solution
{
  public bool IsValid(string s)
  {
    var inp = s.ToList();
    var stack = new Stack<char>();
    var open = new Dictionary<char,char>{{'}','{'},{']','['},{')','('}};
    char poped = ' ';
    bool popResult = true;
    foreach (var c in inp)
    {
      switch (c)
      {
        case '{':
          stack.Push(c);
          break;
        case '(':
          stack.Push(c);
          break;
        case '[':
          stack.Push(c);
          break;
        case ']':
          popResult = stack.TryPop(out poped);
          popResult = open[']'] == poped;
          break;
        case ')':
          popResult = stack.TryPop(out poped);
          popResult = open[')'] == poped;
          break;
        case '}':
          popResult = stack.TryPop(out poped);
          popResult = open['}'] == poped;
          break;
        default:
          break;
      }
      if (!popResult) { return false; }
    }
    return stack.Count() == 0;
  }
}