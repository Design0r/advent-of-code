import fs from "fs/promises";

const input = await fs.readFile("inputs/day_03.txt", {
  encoding: "utf8",
});
const lines = input.trimEnd().split("\n");
const boxes = lines.map((b) => {
  const [coord, size] = b.split(" @ ")[1].split(": ");
  const [x, y] = coord.split(",").map(Number);
  const [w, h] = size.split("x").map(Number);
  return { x, y, w, h };
});

const bounds = getBounds(boxes);
const grid = Array.from({ length: bounds.y }).map(() =>
  Array.from({ length: bounds.x }, () => 0),
);

function getBounds(boxes: Box[]): Vec2 {
  let maxW = 0;
  let maxH = 0;
  for (const b of boxes) {
    maxW = Math.max(maxW, b.x + b.w);
    maxH = Math.max(maxH, b.y + b.w);
  }

  return { x: maxW, y: maxH };
}

type Box = { x: number; y: number; w: number; h: number };
type Vec2 = { x: number; y: number };

function fillGrid(grid: number[][], box: Box) {
  for (let y = 0; y < box.h; y++) {
    for (let x = 0; x < box.w; x++) {
      grid[box.y + y][box.x + x] += 1;
    }
  }
}

function hasOverlap(grid: number[][], box: Box): boolean {
  for (let y = 0; y < box.h; y++) {
    for (let x = 0; x < box.w; x++) {
      if (grid[box.y + y][box.x + x] > 1) return true;
    }
  }

  return false;
}

function part_1() {
  boxes.forEach((b) => fillGrid(grid, b));
  const result = grid
    .flat()
    .reduce((acc, curr) => (curr > 1 ? acc + 1 : acc), 0);
  console.log("Day 03, Part 01:", result);
}

function part_2() {
  for (let i = 0; i < boxes.length; i++) {
    if (!hasOverlap(grid, boxes[i])) console.log("Day 03, Part 02:", i + 1);
  }
}

part_1();
part_2();
