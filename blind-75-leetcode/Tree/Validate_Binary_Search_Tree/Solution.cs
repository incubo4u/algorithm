public class Solution
{
  public bool IsValidBST(TreeNode root)
  {
    if (root.left == null && root.right == null) { return true; }
    return IsValidBSTRec(root);
  }
  public bool IsValidBSTRec(TreeNode root, int? leftLimit = null, int? rightLimit = null)
  {
    if (root == null) { return true; }
    if ((leftLimit == null || root.val > leftLimit) && (rightLimit == null || root.val < rightLimit))
    {
      if (root.left != null)
      {
        if (!IsValidBSTRec(root.left, leftLimit, root.val)) { return false; }
      }
      if (root.right != null)
      {
        if (!IsValidBSTRec(root.right, root.val, rightLimit)) { return false; }
      }
    }
    else
    {
      return false;
    }
    return true;
  }
}