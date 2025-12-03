use core::fmt;
use std::{cmp::Ordering, fs};

fn part_1(lines: &Vec<&str>) {
    let mut result = 0;

    for line in lines {
        let (max_idx1, max1) = line[..line.len() - 1].chars().enumerate().max().unwrap();
        let max2 = &line[max_idx1 + 1..].chars().max().unwrap();

        let num = format!("{max1}{max2}").parse::<u32>().unwrap();
        result += num;
    }

    println!("Day 03, Part 1: {}", result);
}

fn part_2(lines: &Vec<&str>) {
    let mut result = 0;

    for line in lines {
        let len = line.chars().count();
        let mut start = 0;
        let nums_wanted = 12;

        for i in 0..nums_wanted {
            let remaining = nums_wanted - i;
            let end = len - remaining;

            let (max_idx, max) = line
                .chars()
                .enumerate()
                .filter(|(idx, _)| *idx >= start && *idx <= end)
                .max_by(|(_, a), (_, b)| a.cmp(b).then(Ordering::Greater))
                .unwrap();

            let max_num = max.to_string().parse::<u64>().unwrap();
            result += max_num * (10u64.pow((nums_wanted - 1 - i) as u32));
            start = max_idx + 1;
        }
    }
    println!("Day 03, Part 2: {}", result);
}

fn main() {
    let file = fs::read_to_string("inputs/day_03.txt").expect("error reading file");
    let lines: Vec<&str> = file.lines().collect();
    part_1(&lines);
    part_2(&lines);
}
