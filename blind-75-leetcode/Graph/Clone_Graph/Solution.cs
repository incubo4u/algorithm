public class Solution
{
  Dictionary<Node, Node> hasBeenCloned = new Dictionary<Node, Node>();
  public Node? CloneGraph(Node node)
  {
    if (node == null) { return null; }
    if (node.neighbors == null || node.neighbors.Count == 0) { return new Node(1, new List<Node>()); }
    return CloneNeighborsRec(node);
  }
  public Node CloneNeighborsRec(Node node)
  {
    Node clone;
    if (hasBeenCloned.ContainsKey(node))
    {
      clone = hasBeenCloned[node];
    }
    else
    {
      clone = new Node(node.val, new List<Node>());
      hasBeenCloned.Add(node, clone);
      foreach (var n in node.neighbors)
      {
        clone.neighbors.Add(CloneNeighborsRec(n));
      }
    }
    return clone;
  }
}