use std::fs;

fn part_1(file: &String) {
    let nums: Vec<u32> = file.lines().filter_map(|x| x.parse::<u32>().ok()).collect();

    let result = nums.iter().zip(nums.iter().skip(1));

    println!("Day 0, Part 1: {:?}", result);
}

fn part_2(file: &String) {
    let result = 0;
    println!("Day 0, Part 2: {}", result);
}

fn main() {
    let file = fs::read_to_string("samples/day_01.txt").expect("error reading file");
    part_1(&file);
}
