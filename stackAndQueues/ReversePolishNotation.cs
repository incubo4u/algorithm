using System;
using System.Collections.Generic;

namespace stackAndQueues
{
  public class RPN
  {
    Stack<int> stack = new Stack<int>();
    bool isDigitPresent;
    int operand;
    int secondOperand;
    public int EvalRPN(string[] tokens)
    {
      for (int i = 0; i < tokens.GetLength(0); i++)
      {
        isDigitPresent = tokens[i].Any(c => char.IsDigit(c));
        if (isDigitPresent)
        {
          stack.Push(int.Parse(tokens[i]));
        }
        else
        {
          secondOperand = stack.Pop();
          operand = stack.Pop();
          switch (tokens[i])
          {
            case "+":
              stack.Push(operand + secondOperand);

              break;
            case "-":
              stack.Push(operand - secondOperand);
              break;
            case "*":
              stack.Push(operand * secondOperand);
              break;
            case "/":
              stack.Push((operand / secondOperand));
              break;
            default:
              continue;
          }
        }
      }
      return stack.Pop();
    }
  }
}