use std::{collections::HashSet, fs};

fn part_1(ranges: &Vec<(u64, u64)>, items: &Vec<u64>) {
    let mut result = 0;

    for (min, max) in ranges {
        for item in items {
            if min <= item && item <= max {
                result += 1;
            }
        }
    }
    println!("Day 05, Part 1: {}", result);
}

fn part_2(ranges: &Vec<(u64, u64)>) {
    let mut result = 0;

    for (min, max) in ranges {
        result += max + 1 - min
    }
    println!("Day 05, Part 2: {}", result);
}

fn merge_ranges(mut ranges: Vec<(u64, u64)>) -> Vec<(u64, u64)> {
    ranges.sort_unstable_by_key(|r| r.0);

    let mut merged: Vec<(u64, u64)> = Vec::new();

    for (start, end) in ranges {
        if let Some(last) = merged.last_mut() {
            if start <= last.1 {
                if end > last.1 {
                    last.1 = end;
                }
            } else {
                merged.push((start, end));
            }
        } else {
            merged.push((start, end));
        }
    }

    return merged;
}

fn main() {
    let file = fs::read_to_string("inputs/day_05.txt").expect("error reading file");
    let lines: Vec<&str> = file.split("\n\n").collect();
    let ranges: Vec<(u64, u64)> = lines[0]
        .split_whitespace()
        .map(|line| {
            let mut split = line.split("-");
            let num1 = split.next().unwrap().parse::<u64>().unwrap();
            let num2 = split.next().unwrap().parse::<u64>().unwrap();
            return (num1, num2);
        })
        .collect();

    let merged = merge_ranges(ranges);

    let items: Vec<u64> = lines[1]
        .split_whitespace()
        .map(|line| {
            let mut split = line.split("-");
            let num = split.next().unwrap().parse::<u64>().unwrap();
            return num;
        })
        .collect();

    part_1(&merged, &items);
    part_2(&merged);
}
