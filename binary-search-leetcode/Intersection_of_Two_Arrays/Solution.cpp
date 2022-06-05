#include <stdlib.h>
#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> intersection(std::vector<int> &nums1, std::vector<int> &nums2) {
        std::unordered_set<int> one;
        for (int i = 0; i < nums1.size(); ++i) {
            one.insert(nums1[i]);
        }
        std::unordered_set<int> intersection;
        if (one.size() > 0) {
            for (int j = 0; j < nums2.size(); ++j) {
                if (one.count(nums2[j]) == 1 && intersection.count(nums2[j]) == 0) {
                    intersection.insert(nums2[j]);
                }
            }
        }
        return std::vector<int>(intersection.begin(), intersection.end());
    }
};