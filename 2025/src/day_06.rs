use std::fs;

fn part_1(lines: &[&str], signs: &[&str]) {
    let rows = lines.len() - 1;
    let cols = signs.len();

    let mut results: Vec<u64> = vec![0; cols];

    for (row_idx, line) in lines[..rows].iter().enumerate() {
        for (col_idx, num_str) in line.split_whitespace().enumerate() {
            let num = num_str.parse::<u64>().unwrap();

            if row_idx == 0 {
                results[col_idx] = num;
            } else {
                match signs[col_idx] {
                    "+" => results[col_idx] += num,
                    "*" => results[col_idx] *= num,
                    _ => unreachable!(),
                }
            }
        }
    }

    println!("Day 06, Part 1: {}", results.iter().sum::<u64>());
}

fn part_2(lines: &[&str], signs: &[&str]) {
    let mut result = 0;
    let mut block = 0;
    let mut signs_iter = signs.iter();
    let mut curr_sign = signs_iter.next();
    for x in 0..lines[0].len() {
        if let Some(col) = parse_col(x, lines) {
            if let Some(s) = curr_sign {
                match *s {
                    "+" => block += col as u64,
                    "*" => {
                        if block == 0 {
                            block = col as u64
                        } else {
                            block *= col as u64
                        }
                    }
                    _ => unreachable!(),
                }
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

fn parse_col(col: usize, lines: &[&str]) -> Option<u16> {
    let mut value: u16 = 0;

    for &line in &lines[..lines.len() - 1] {
        let bytes = line.as_bytes();
        let b = bytes[col];

        if b.is_ascii_whitespace() {
            continue;
        }

        value = value * 10 + (b - b'0') as u16;
    }

    if value > 0 { Some(value) } else { None }
}

fn main() {
    let file = fs::read_to_string("inputs/day_06.txt").expect("error reading file");
    let lines: Vec<&str> = file.lines().collect();
    let signs: Vec<&str> = lines.last().unwrap().split_whitespace().collect();

    part_1(&lines, &signs);
    part_2(&lines, &signs);
}
