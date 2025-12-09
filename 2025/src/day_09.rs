use std::{fs, time::Instant};

use glam::I64Vec2;

fn part_1(points: &Vec<I64Vec2>) {
    let result = points
        .iter()
        .flat_map(|a| {
            points.iter().map(move |b| {
                let diff = (a - b).abs() + 1;
                let area = diff.x * diff.y;
                area
            })
        })
        .max()
        .unwrap();

    println!("Day 09, Part 1: {}", result);
}

fn part_2(points: &Vec<I64Vec2>) {
    let mut result = 0;

    println!("Day 09, Part 2: {}", result);
}

fn main() {
    let start = Instant::now();

    let file = fs::read_to_string("inputs/day_09.txt").expect("error reading file");
    let points: Vec<I64Vec2> = file
        .lines()
        .map(|l| {
            I64Vec2::from_slice(
                &l.split(",")
                    .map(|x| x.parse::<i64>().unwrap())
                    .collect::<Vec<i64>>(),
            )
        })
        .collect();

    part_1(&points);
    part_2(&points);

    println!("Finished in {}µs", start.elapsed().as_micros());
}
