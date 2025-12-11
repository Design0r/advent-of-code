use std::{collections::HashSet, fs, time::Instant, vec};

use rayon::iter::{IntoParallelRefIterator, ParallelIterator};

fn part_1(points: &[Machine]) {
    let result = 0;

    println!("Day 10, Part 1: {}", result);
}

fn push_button_jolt(joltage: &[u32], buttons: &[u32]) -> Vec<u32> {
    let mut jlt = joltage.to_owned();
    for b in buttons {
        jlt[*b as usize] += 1;
    }

    jlt
}

fn calc(machine: &Machine) -> u32 {
    let mut button_presses = 0;
    let mut curr_joltage: HashSet<Vec<u32>> = HashSet::new();
    curr_joltage.insert(vec![0 as u32; machine.joltage.len()]);

    loop {
        let mut joltages: HashSet<Vec<u32>> = HashSet::new();
        for jlt in &curr_joltage {
            for btn in &machine.buttons {
                let new = push_button_jolt(jlt, btn);
                if new.iter().zip(&machine.joltage).any(|(a, b)| a > b) {
                    continue;
                }
                joltages.insert(new);
            }
        }

        curr_joltage = joltages;

        button_presses += 1;

        if curr_joltage.contains(&machine.joltage) {
            println!("completed {machine:?}");
            return button_presses;
        }
    }
}

fn part_2(machines: &[Machine]) {
    let result: u32 = machines.par_iter().map(|m| calc(m)).sum();

    println!("Day 10, Part 2: {}", result);
}

#[derive(Debug)]
struct Machine {
    buttons: Vec<Vec<u32>>,
    joltage: Vec<u32>,
}

impl Machine {
    fn new(buttons: Vec<Vec<u32>>, joltage: Vec<u32>) -> Self {
        Self { buttons, joltage }
    }
}

fn main() {
    let start = Instant::now();

    let file = fs::read_to_string("inputs/day_10.txt").expect("error reading file");
    let machines: Vec<Machine> = file
        .lines()
        .map(|l| {
            let split: Vec<&str> = l.split_whitespace().collect();

            let last = split.last().unwrap();
            let joltage: Vec<u32> = last[1..last.len() - 1]
                .split(",")
                .map(|n| n.parse::<u32>().unwrap())
                .collect();

            let buttons: Vec<Vec<u32>> = split[1..split.len() - 1]
                .into_iter()
                .map(|b| {
                    let buttons = b[1..b.len() - 1]
                        .split(",")
                        .map(|n| n.parse::<u32>().unwrap())
                        .collect();

                    buttons
                })
                .collect();

            Machine::new(buttons, joltage)
        })
        .collect();

    //part_1(&machines);
    part_2(&machines);

    println!("Finished in {}s", start.elapsed().as_secs());
}
