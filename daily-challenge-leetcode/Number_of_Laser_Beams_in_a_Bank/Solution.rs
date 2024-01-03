impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut beams = 0;
        let mut last_devices = 0;
        for b in bank {
            let curr_devices: i32 = b.chars().map(|ch| ch.to_digit(2).unwrap() as i32).sum();
            if curr_devices == 0 {
                continue;
            }
            beams += last_devices * curr_devices;
            last_devices = curr_devices;
        }
        beams
    }
}
