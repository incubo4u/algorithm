from typing import List


class Solution:
    def distanceK(self, root, target, k) -> List[int]:
        ans = []
        if not k:
            return [target.val]

        def find_target(target, root, k):
            if not root or k < 0:
                return -1

            if target == root:
                get_k_child(k - 1, root.left)
                get_k_child(k - 1, root.right)
                return k - 1

            left = find_target(target, root.left, k)
            right = find_target(target, root.right, k)
            distance = max(left, right)
            if not distance:
                ans.append(root.val)
                return -1

            if right > 0:
                get_k_child(distance - 1, root.left)
            elif left > 0:
                get_k_child(distance - 1, root.right)

            return distance - 1

        def get_k_child(k, root):
            if not root:
                return
            if k == 0:
                ans.append(root.val)
                return
            get_k_child(k - 1, root.left)
            get_k_child(k - 1, root.right)

        find_target(target, root, k)
        return ans
