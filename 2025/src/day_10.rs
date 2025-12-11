use rustc_hash::FxHashSet;
use std::{collections::HashSet, fs, time::Instant, vec};

use rayon::iter::{IntoParallelRefIterator, ParallelIterator};

fn part_1(points: &[Machine]) {
    let result = 0;

    println!("Day 10, Part 1: {}", result);
}

fn push_button_jolt(joltage: &[u16], buttons: &[u16]) -> Box<[u16]> {
    let mut jlt = joltage.to_vec();
    for b in buttons {
        jlt[*b as usize] += 1;
    }

    jlt.into_boxed_slice()
}

fn calc(machine: &Machine) -> u16 {
    let mut button_presses = 0 as u16;
    let mut curr_joltage: FxHashSet<Box<[u16]>> = FxHashSet::default();
    curr_joltage.insert(vec![0 as u16; machine.joltage.len()].into_boxed_slice());

    loop {
        let mut joltages: FxHashSet<Box<[u16]>> = FxHashSet::with_capacity_and_hasher(
            curr_joltage.len() * machine.buttons.len(),
            Default::default(),
        );
        for jlt in &curr_joltage {
            for btn in &machine.buttons {
                let new = push_button_jolt(jlt, btn);

                if new == machine.joltage {
                    println!("completed {machine:?}");
                    return button_presses;
                }

                if new.iter().zip(&machine.joltage).any(|(a, b)| a > b) {
                    continue;
                }
                joltages.insert(new);
            }
        }

        curr_joltage = joltages;
        println!("{}", curr_joltage.len());

        button_presses += 1;
    }
}

fn part_2(machines: &[Machine]) {
    let result: u16 = machines.par_iter().map(|m| calc(m)).sum();

    println!("Day 10, Part 2: {}", result);
}

#[derive(Debug)]
struct Machine {
    buttons: Vec<Vec<u16>>,
    joltage: Box<[u16]>,
}

impl Machine {
    fn new(buttons: Vec<Vec<u16>>, joltage: Box<[u16]>) -> Self {
        Self { buttons, joltage }
    }
}

fn main() {
    rayon::ThreadPoolBuilder::new()
        .num_threads(2)
        .build_global()
        .unwrap();

    let start = Instant::now();

    let file = fs::read_to_string("inputs/day_10.txt").expect("error reading file");
    let machines: Vec<Machine> = file
        .lines()
        .map(|l| {
            let split: Vec<&str> = l.split_whitespace().collect();

            let last = split.last().unwrap();
            let joltage: Vec<u16> = last[1..last.len() - 1]
                .split(",")
                .map(|n| n.parse::<u16>().unwrap())
                .collect();

            let buttons: Vec<Vec<u16>> = split[1..split.len() - 1]
                .into_iter()
                .map(|b| {
                    let buttons = b[1..b.len() - 1]
                        .split(",")
                        .map(|n| n.parse::<u16>().unwrap())
                        .collect();

                    buttons
                })
                .collect();

            Machine::new(buttons, joltage.into_boxed_slice())
        })
        .collect();

    //part_1(&machines);
    part_2(&machines);

    println!("Finished in {}s", start.elapsed().as_secs());
}
