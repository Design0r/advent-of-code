import fs from "fs/promises";

const input = await fs.readFile("inputs/day_01.txt", { encoding: "utf8" });
const lines = input
  .split("\n")
  .slice(0, -1)
  .map((v) => Number.parseInt(v.trim()));

function part_1() {
  const result = lines.reduce((sum, curr) => sum + curr, 0);
  console.log("Day 01, Part 1:", result);
}

function part_2() {
  const seen = new Set<number>();
  let freq = 0;
  let idx = 0;

  while (true) {
    if (idx === lines.length) idx = 0;
    freq += lines[idx];
    if (seen.has(freq)) break;
    seen.add(freq);
    idx++;
  }

  console.log("Day 01, Part 2:", freq);
}

part_1();
part_2();
