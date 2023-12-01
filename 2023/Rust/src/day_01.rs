use std::fs;

#[cfg(windows)]
const LINE_ENDING: &'static str = "\r\n";
#[cfg(not(windows))]
const LINE_ENDING: &'static str = "\n";

fn main() {
    let file = fs::read_to_string("samples/day_01.txt").expect("error reading file");
    let split: Vec<String> = file
        .split(LINE_ENDING)
        .map(|line| {
            line.chars()
                .filter_map(|c| match c.is_numeric() {
                    true => Some(String::from(c)),
                    false => None,
                })
                .enumerate()
                .filter_map(|(index, value)| {
                    if index == 0 || index == value.len() - 1 {
                        Some(value)
                    } else {
                        None
                    }
                })
                .collect::<Vec<String>>()
                .join("")
        })
        .collect();

    println!("{:?}", split)
}
