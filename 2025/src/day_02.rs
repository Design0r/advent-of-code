use std::fs;

fn is_valid(val: &String) -> bool {
    let middle = val.len() / 2;
    let start = &val[..middle];
    let end = &val[middle..];

    return start != end;
}

fn is_valid2(val: &String) -> bool {
    for idx in 1..val.len() {
        let slice = &val[0..idx];
        let count = val
            .as_bytes()
            .chunks(idx)
            .filter(|&s| s == slice.as_bytes())
            .count();

        let (div, rem) = (val.len() / slice.len(), val.len() % slice.len());

        if count == div && rem == 0 {
            return false;
        }
    }

    return true;
}

fn part_1(lines: &Vec<(u64, u64)>) {
    let mut result: u64 = 0;

    for (start, end) in lines {
        for id in *start..=*end {
            let id_str = id.to_string();
            if id_str.len() % 2 != 0 {
                continue;
            }
            if !is_valid(&id_str) {
                result += id as u64;
            }
        }
    }

    println!("Day 2, Part 1: {result}");
}

fn part_2(lines: &Vec<(u64, u64)>) {
    let mut result: u64 = 0;

    for (start, end) in lines {
        for id in *start..=*end {
            if !is_valid2(&id.to_string()) {
                result += id as u64;
            }
        }
    }

    println!("Day 2, Part 2: {result}");
}

fn main() {
    let file = fs::read_to_string("inputs/day_02.txt").unwrap();
    let lines: Vec<_> = file
        .split(",")
        .map(|s| {
            let mut split = s.split("-");
            let start = split.next().unwrap();
            let end = split.next().unwrap();
            let start_num = start.parse::<u64>().unwrap();
            let end_num = end.parse::<u64>().unwrap();

            return (start_num, end_num);
        })
        .collect();

    part_1(&lines);
    part_2(&lines);
}
