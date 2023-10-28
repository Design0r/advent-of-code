use std::fs;

fn main() {
    let alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let file = fs::read_to_string("samples/day_03.txt").expect("error reading file");
    let halfes: Vec<_> = file.lines().map(|x| x.split_at(x.len() / 2)).collect();

    let res: u32 = halfes
        .iter()
        .filter_map(|(left, right)| {
            left.chars()
                .find(|&y| right.contains(y))
                .map(|z| alpha.find(z).unwrap() as u32 + 1)
        })
        .sum();

    println!("Day 3, Part 1: {:?}", res);
}
