import fs from "fs/promises";

const input: string = await fs.readFile("inputs/day_02.txt", {
  encoding: "utf8",
});
const lines: string[] = input.split("\n");

function part_1() {
  const count = lines.map((l) => {
    const map: Record<string, number> = {};
    l.split("").forEach((e) => {
      if (map[e]) map[e]++;
      else map[e] = 1;
    });

    let hasTwo = 0;
    let hasThree = 0;

    Object.values(map).forEach((n) => {
      if (n === 2) hasTwo = 1;
      else if (n === 3) hasThree = 1;
    });

    return { 2: hasTwo, 3: hasThree };
  });

  let x = 0;
  let y = 0;
  count.forEach((e) => {
    x += e["2"];
    y += e["3"];
  });
  console.log("Day 02, Part 1:", x * y);
}

function diff(a: string, b: string): number {
  let diffCount = 0;
  for (let i = 0; i < a.length; i++) {
    if (diffCount > 1) return 2;
    if (a[i] != b[i]) diffCount++;
  }

  return diffCount;
}

function findCommon(a: string, b: string): string {
  const common: string[] = [];
  for (let i = 0; i < a.length; i++) {
    if (a[i] != b[i]) continue;
    common.push(a[i]);
  }

  return common.join("");
}

function part_2() {
  let result = "";
  for (const x of lines) {
    for (const y of lines) {
      const d = diff(x, y);
      if (d === 1) {
        result = findCommon(x, y);
        break;
      }
    }
  }

  console.log("Day 02, Part 2:", result);
}

part_1();
part_2();
