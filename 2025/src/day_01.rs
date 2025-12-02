use std::{char, fs};

fn part_1(lines: &Vec<(char, i16)>) {
    let mut result = 0;
    let mut dial = 50;

    for (dir, num) in lines {
        dial = (dial + (if *dir == 'L' { -1 } else { 1 } * num)) % 100;
        if dial == 0 {
            result += 1;
        }
    }

    println!("Day 01, Part 1: {}", result);
}

fn part_2(lines: &Vec<(char, i16)>) {
    let mut result = 0;
    let mut dial = 50;

    for (dir, num) in lines {
        for _ in 0..*num {
            dial = (dial + (if *dir == 'L' { -1 } else { 1 })) % 100;
            if dial == 0 {
                result += 1;
            }
        }
    }
    println!("Day 01, Part 2: {}", result);
}

fn main() {
    let file = fs::read_to_string("inputs/day_01.txt").expect("error reading file");
    let lines: Vec<(char, i16)> = file
        .lines()
        .map(|l| {
            let num = l[1..].parse::<i16>().unwrap();
            return (l.chars().next().unwrap(), num);
        })
        .collect();

    part_1(&lines);
    part_2(&lines);
}
