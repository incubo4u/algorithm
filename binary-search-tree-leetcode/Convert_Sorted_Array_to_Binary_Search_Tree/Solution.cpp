#include <stdlib.h>
#include <vector>
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    std::vector<int> nums;
    TreeNode *sortedArrayToBST(std::vector<int> &Nums)
    {
        nums = Nums;
        return helper(0, nums.size() - 1);
    }
    TreeNode *helper(int l, int r)
    {
        if (l > r) return nullptr;
        int mid = l + (r - l) / 2;
        TreeNode *root = new TreeNode(nums[mid]);
        root->left = helper(l, mid - 1);
        root->right = helper(mid + 1, r);
        return root;
    }
};
int main(){
    
}