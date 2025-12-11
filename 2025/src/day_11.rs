use rustc_hash::FxHashMap;
use std::{collections::HashMap, fs, time::Instant};

fn part_1(list: &FxHashMap<&str, Vec<&str>>) {
    let mut result = 0;
    let out = "out";

    let mut stack: Vec<&str> = vec!["you"];
    loop {
        if stack.len() == 0 {
            break;
        }
        let curr = stack.pop().unwrap();
        if curr == out {
            result += 1;
            continue;
        }

        if let Some(outputs) = list.get(curr) {
            for o in outputs {
                stack.push(o);
            }
        }
    }

    println!("Day 11, Part 1: {}", result);
}

fn walk(
    list: &FxHashMap<&str, Vec<&str>>,
    curr: &str,
    fft: bool,
    dac: bool,
    cache: &mut FxHashMap<(String, bool, bool), u64>,
) -> u64 {
    if let Some(&cached) = cache.get(&(curr.to_string(), fft, dac)) {
        return cached;
    }

    let mut local_fft = fft;
    let mut local_dac = dac;
    if curr == "out" && fft && dac {
        return 1;
    } else if curr == "fft" {
        local_fft = true
    } else if curr == "dac" {
        local_dac = true
    }

    if let Some(outputs) = list.get(curr) {
        let result: u64 = outputs
            .iter()
            .map(|o| walk(list, o, local_fft, local_dac, cache))
            .sum();
        cache.insert((curr.to_string(), fft, dac), result);
        return result;
    }

    0
}

fn part_2(list: &FxHashMap<&str, Vec<&str>>) {
    let mut cache: FxHashMap<(String, bool, bool), u64> = FxHashMap::default();
    let result = walk(list, "svr", false, false, &mut cache);

    println!("Day 11, Part 2: {}", result);
}

fn main() {
    let start = Instant::now();

    let file = fs::read_to_string("inputs/day_11.txt").expect("error reading file");
    let lines: Vec<&str> = file.lines().collect();

    let mut map: FxHashMap<&str, Vec<&str>> = FxHashMap::default();

    for l in &lines {
        let mut split = l.split(": ").into_iter();
        let key = split.next().unwrap();

        let outputs: Vec<&str> = split
            .flat_map(|s| s.split_whitespace().collect::<Vec<&str>>())
            .collect();

        map.insert(key, outputs);
    }

    part_1(&map);
    part_2(&map);

    println!("Finished in {}µs", start.elapsed().as_micros());
}
