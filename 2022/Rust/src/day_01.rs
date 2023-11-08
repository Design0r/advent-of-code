use std::fs;

#[cfg(windows)]
const LINE_ENDING: &'static str = "\r\n\r\n";
#[cfg(not(windows))]
const LINE_ENDING: &'static str = "\n\n";

fn main() {
    let mut backpack: Vec<u32> = fs::read_to_string("inputs/day_01.txt")
        .expect("error reading file")
        .split(LINE_ENDING)
        .map(|blocks| {
            blocks
                .lines()
                .filter_map(|line| line.parse::<u32>().ok())
                .sum()
        })
        .collect();

    backpack.sort();
    backpack.reverse();

    println!("Day 1, Part 1: {:?}", &backpack.first().unwrap());
    println!("Day 1, Part 2: {:?}", &backpack[..3].iter().sum::<u32>());
}
