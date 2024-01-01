impl Solution {
    pub fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
        let s_len = s.len();
        let g_len = g.len();
        let mut ans = 0;
        let mut gi = 0;
        g.sort();
        s.sort();
        for si in 0..s_len {
            if gi < g_len && s[si] >= g[gi] {
                ans += 1;
                gi += 1;
            }
        }
        return ans;
    }
}
