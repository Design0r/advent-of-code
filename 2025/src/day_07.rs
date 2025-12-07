use std::{
    collections::{HashMap, HashSet},
    fs,
    time::Instant,
};

use glam::IVec2;

fn part_1(splitter: &HashSet<IVec2>, start_pos: IVec2, bounds: IVec2) {
    let mut result = 0;

    let mut beams: HashSet<IVec2> = HashSet::new();
    beams.insert(start_pos);
    let mut old_beams: Vec<IVec2> = Vec::new();
    let mut new_beams: Vec<IVec2> = Vec::new();

    'outer: loop {
        for beam in &beams {
            let next = beam + IVec2::Y;
            if next.y >= bounds.y {
                break 'outer;
            }

            if splitter.contains(&next) {
                result += 1;
                let left = next + IVec2::NEG_X;
                let right = next + IVec2::X;
                old_beams.push(*beam);
                new_beams.push(left);
                new_beams.push(right);
            } else {
                new_beams.push(next);
                old_beams.push(*beam);
            }
        }

        for beam in &old_beams {
            beams.remove(beam);
        }
        old_beams.clear();

        for beam in &new_beams {
            beams.insert(*beam);
        }
        new_beams.clear();
    }

    println!("Day 07, Part 1: {}", result);
}

fn simulate(
    splitter: &HashSet<IVec2>,
    beam: IVec2,
    bounds: IVec2,
    cache: &mut HashMap<IVec2, u64>,
) -> u64 {
    if let Some(&res) = cache.get(&beam) {
        return res;
    }

    let mut curr = beam;
    loop {
        let next = curr + IVec2::Y;

        if next.y >= bounds.y {
            cache.insert(beam, 1);
            return 1;
        }

        if splitter.contains(&next) {
            let left = next + IVec2::NEG_X;
            let right = next + IVec2::X;

            let l = simulate(splitter, left, bounds, cache);
            let r = simulate(splitter, right, bounds, cache);
            let result = l + r;

            cache.insert(beam, result);
            return result;
        }

        curr = next;
    }
}

fn part_2(splitter: &HashSet<IVec2>, start_pos: IVec2, bounds: IVec2) {
    let mut cache: HashMap<IVec2, u64> = HashMap::new();
    let result = simulate(splitter, start_pos, bounds, &mut cache);

    println!("Day 07, Part 2: {}", result);
}

fn main() {
    let start = Instant::now();

    let file = fs::read_to_string("inputs/day_07.txt").expect("error reading file");

    let mut start_pos = IVec2::new(0, 0);
    let mut splitter: HashSet<IVec2> = HashSet::new();

    for (y, line) in file.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            match c {
                '^' => {
                    splitter.insert(IVec2::new(x as i32, y as i32));
                }
                'S' => {
                    start_pos = IVec2::new(x as i32, y as i32);
                }
                _ => {}
            }
        }
    }

    let bounds = IVec2::new(
        file.lines().last().unwrap().len() as i32,
        file.lines().count() as i32,
    );

    part_1(&splitter, start_pos, bounds);
    part_2(&splitter, start_pos, bounds);

    println!("Finished in {}µs", start.elapsed().as_micros());
}
