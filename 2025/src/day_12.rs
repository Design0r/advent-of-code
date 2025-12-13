use std::{fs, time::Instant};

fn part_1(presents: &Vec<u8>, grids: &Vec<Grid>) {
    let result = grids.iter().fold(0, |acc, g| {
        let area: u16 = g.width as u16 * g.height as u16;
        let packed_presents =
            g.presents
                .iter()
                .enumerate()
                .fold(0, |acc, (present_type, present_count)| {
                    let present_size: u16 =
                        (presents[present_type] as u16) * (*present_count as u16);
                    if area > present_size {
                        return acc + present_size;
                    }

                    acc
                });

        if packed_presents <= area {
            return acc + 1;
        }

        acc
    });

    println!("Day 12, Part 1: {}", result);
}

#[derive(Debug)]
struct Grid {
    width: u8,
    height: u8,
    presents: Vec<u8>,
}

fn main() {
    let start = Instant::now();

    let file = fs::read_to_string("inputs/day_12.txt").expect("error reading file");
    let sections: Vec<&str> = file.split("\n\n").collect();
    let presents: Vec<u8> = sections[0..sections.len() - 1]
        .iter()
        .map(|&l| {
            let mut lines = l.lines();
            lines.next().unwrap();
            lines
                .map(|l| {
                    l.chars()
                        .filter(|c| match c {
                            '#' => true,
                            '.' => false,
                            _ => unreachable!(),
                        })
                        .count() as u8
                })
                .sum()
        })
        .collect();

    let grids: Vec<Grid> = sections
        .last()
        .unwrap()
        .lines()
        .map(|l| {
            let mut split = l.split(": ");
            let mut size = split
                .next()
                .unwrap()
                .split("x")
                .map(|s| s.parse::<u8>().unwrap());
            let presents: Vec<u8> = split
                .next()
                .unwrap()
                .split_whitespace()
                .map(|s| s.parse::<u8>().unwrap())
                .collect();

            Grid {
                width: size.next().unwrap(),
                height: size.next().unwrap(),
                presents: presents,
            }
        })
        .collect();

    part_1(&presents, &grids);

    println!("Finished in {}µs", start.elapsed().as_micros());
}
