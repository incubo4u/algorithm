public class Solution
{
  public int result = 0;
  public int MaxDepth(TreeNode root)
  {
    MaxDepthRec(root);
    return result;
  }
  public void MaxDepthRec(TreeNode root, int deepth = 1)
  {
    if (root == null) { return; }
    if (root.left == null && root.right == null)
    {
      this.result = Math.Max(result, deepth);
    }
    if (root.left != null)
    {
      MaxDepthRec(root.left, deepth + 1);
    }
    if (root.right != null)
    {
      MaxDepthRec(root.right, deepth + 1);
    }
  }
}