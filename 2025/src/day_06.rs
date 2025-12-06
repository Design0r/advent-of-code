use std::fs;

fn part_1(lines: &Vec<&str>, signs: &Vec<&str>) {
    let nums: Vec<u64> = lines[0..lines.len() - 1]
        .iter()
        .flat_map(|l| {
            l.split_whitespace()
                .filter_map(|num| num.parse::<u64>().ok())
                .collect::<Vec<u64>>()
        })
        .collect();

    let cols = lines[0].split_whitespace().count();

    let result = (0..cols).fold(0 as u64, |acc, x| {
        acc + (0..lines.len() - 1).fold(0 as u64, |a, y| {
            let idx = y * cols + x;
            let num = nums[idx];
            let sign = signs[x];
            let is_first_row = y == 0;

            if is_first_row {
                return num;
            }

            match sign {
                "+" => a + num,
                "*" => a * num,
                _ => unreachable!(),
            }
        })
    });

    println!("Day 06, Part 1: {}", result);
}

fn part_2(lines: &Vec<&str>, signs: &Vec<&str>) {
    let chars: Vec<Vec<char>> = lines[0..lines.len() - 1]
        .iter()
        .map(|l| l.chars().collect())
        .collect();

    let mut result = 0;
    let mut block = 0;
    let mut signs_iter = signs.iter();
    let mut curr_sign = signs_iter.next();
    for x in 0..lines[0].len() {
        if let Some(col) = parse_col(x, &chars) {
            match curr_sign {
                Some(s) => match *s {
                    "+" => block += col,
                    "*" => {
                        if block == 0 {
                            block = col
                        } else {
                            block *= col
                        }
                    }
                    _ => {}
                },
                None => (),
            }
        } else {
            result += block;
            block = 0;
            curr_sign = signs_iter.next();
        }
    }

    result += block;

    println!("Day 06, Part 2: {}", result);
}

fn parse_col(col: usize, grid: &Vec<Vec<char>>) -> Option<u64> {
    let mut str: Vec<char> = Vec::new();
    for x in 0..grid.len() {
        let item = grid[x][col];
        if item.is_whitespace() {
            continue;
        }
        str.push(item)
    }

    if str.len() == 0 {
        return None;
    }

    let coll: String = str.into_iter().collect();

    Some(coll.parse::<u64>().unwrap())
}

fn main() {
    let file = fs::read_to_string("inputs/day_06.txt").expect("error reading file");
    let lines: Vec<&str> = file.lines().collect();
    let signs: Vec<&str> = lines.last().unwrap().split_whitespace().collect();

    part_1(&lines, &signs);
    part_2(&lines, &signs);
}
