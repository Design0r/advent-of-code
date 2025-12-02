use std::fs;

fn part_1(lines: &Vec<(u64, u64)>) {
    let mut result: u64 = 0;

    for (start, end) in lines {
        for id in *start..=*end {
            let id_str = id.to_string();
            if id_str.len() % 2 != 0 {
                continue;
            }

            let middle = id_str.len() / 2;
            let start = &id_str[..middle];
            let end = &id_str[middle..];

            if start == end {
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
            let id_str = id.to_string();
            let half = id_str.len() / 2;
            for limit in 0..half {
                if id_str.len().rem_euclid(limit + 1) != 0 {
                    continue;
                }

                let all_match = id_str[0..=limit]
                    .chars()
                    .cycle()
                    .zip(id_str.chars())
                    .all(|(a, b)| a == b);

                if all_match {
                    result += id;
                    break;
                }
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
