use std::{collections::HashMap, fs};

#[cfg(windows)]
const LINE_ENDING: &'static str = "\r\n";
#[cfg(not(windows))]
const LINE_ENDING: &'static str = "\n";

fn part_1(split: &Vec<&str>) {
    let mut result = 0;

    for line in split {
        let nums: Vec<_> = line.chars().filter(|c| c.is_digit(10)).collect();
        let first_num = nums.first().unwrap().to_string();
        let last_num = nums.last().unwrap().to_string();
        let num = first_num + &last_num;
        result += num.parse::<u32>().unwrap();
    }

    println!("Day 01, Part 1: {}", result);
}

fn part_2(split: &Vec<&str>) {
    let alpha_num: HashMap<&str, u32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);
    let mut result = 0;

    for line in split {
        let mut nums: Vec<u32> = vec![];
        for (idx, char) in line.chars().enumerate() {
            let word_num = check_for_str_num(&alpha_num, line, idx);
            match word_num {
                Some(val) => nums.push(val),
                None => {
                    if char.is_digit(10) {
                        nums.push(char.to_digit(10).unwrap());
                    }
                }
            }
        }
        let first_num = nums.first().unwrap().to_string();
        let last_num = nums.last().unwrap().to_string();
        let num = first_num + &last_num;
        result += num.parse::<u32>().unwrap();
    }

    println!("Day 01, Part 2: {}", result);
}

fn check_for_str_num(alpha_num: &HashMap<&str, u32>, line: &str, index: usize) -> Option<u32> {
    for (k, v) in alpha_num.iter() {
        let word_len = k.len();
        if (index + word_len) > line.len() {
            return None;
        }
        let word = &line[index..index + word_len];
        if alpha_num.contains_key(&word) {
            println!("{}", word);
            return Some(*v);
        }
    }

    return None;
}

fn main() {
    let file = fs::read_to_string("inputs/day_01.txt").expect("error reading file");
    let split: Vec<&str> = file.split(LINE_ENDING).collect();
    part_1(&split);
    part_2(&split);
}
