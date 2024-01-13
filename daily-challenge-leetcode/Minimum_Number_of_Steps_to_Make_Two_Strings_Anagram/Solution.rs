impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut freq: [i32; 26] = [0; 26];
        for c in s.chars() {
            let i = c as u32 - 'a' as u32;
            freq[i as usize] += 1;
        }
        for c in t.chars() {
            let i = c as u32 - 'a' as u32;
            freq[i as usize] -= 1;
        }
        let mut ans = 0;
        for f in freq {
            ans += f.abs();
        }
        ans / 2
    }
}
