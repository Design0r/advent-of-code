import fs from "fs/promises";

const file = await fs.readFile("input.txt", { encoding: "utf-8" });
const run = (sum: number) =>
  file
    .split("\n\n")
    .map((bagpack: string) =>
      bagpack
        .split("\n")
        .filter((item: string) => item !== "")
        .map((item: string) => parseInt(item))
        .reduce((acc: number, curr: number) => acc + curr),
    )
    .sort((a: number, b: number) => b - a)
    .slice(0, sum)
    .reduce((acc: number, curr: number) => acc + curr);

console.log(run(1));
console.log(run(3));
