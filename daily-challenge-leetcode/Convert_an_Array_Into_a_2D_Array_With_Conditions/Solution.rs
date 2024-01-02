impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = Vec::new();
        let mut freq = vec![0; nums.len() + 1];
        for nr in nums {
            let i = nr as usize;
            if freq[i] >= ans.len() {
                ans.push(Vec::new())
            }
            ans[freq[i]].push(nr);
            freq[i] += 1;
        }
        ans
    }
}
