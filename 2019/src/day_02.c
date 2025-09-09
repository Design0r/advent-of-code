#include "array.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define CHUNK 4

typedef struct {
  int *items;
  size_t length;
  size_t capacity;
} IntArray;

typedef struct {
  int op, a, b, pos;
} Program;

void simulate(IntArray *nums, int noun, int verb) {
  da_set(nums, 1, noun);
  da_set(nums, 2, verb);

  int prog_count = 0;
  Program p = {0};
  for (size_t i = 0; i < nums->length; i++) {
    switch (prog_count) {
    case 0:
      p.op = nums->items[i];
      prog_count++;
      break;
    case 1:
      p.a = nums->items[i];
      prog_count++;
      break;
    case 2:
      p.b = nums->items[i];
      prog_count++;
      break;
    case 3:
      p.pos = nums->items[i];
      if (p.op == 99)
        return;
      else if (p.op == 1) {
        nums->items[p.pos] = da_get(nums, p.a) + da_get(nums, p.b);
      } else if (p.op == 2) {
        nums->items[p.pos] = da_get(nums, p.a) * da_get(nums, p.b);
      } else {
        return;
      }
      prog_count = 0;

      break;
    default:
      assert(0);
      break;
    }
  }
}

int main() {
  FILE *f = fopen("inputs/day_02.txt", "rb");
  IntArray inputs = {0};
  int num = 0;
  while (fscanf(f, "%d,", &num) == 1) {
    da_append(&inputs, num);
  }

  IntArray part1 = {.length = inputs.length};
  da_alloc(&part1, inputs.length);
  memcpy(part1.items, inputs.items, sizeof(*inputs.items) * inputs.length);

  simulate(&part1, 12, 2);
  printf("Day 02, Part 01: %d\n", da_get(&part1, 0));

  IntArray part2 = {.length = inputs.length};
  da_alloc(&part2, inputs.length);

  for (int i = 0; i <= 99; i++) {
    for (int j = 0; j <= 99; j++) {
      memcpy(part2.items, inputs.items, sizeof(*inputs.items) * inputs.length);
      simulate(&part2, i, j);

      if (da_get(&part2, 0) == 19690720) {
        printf("Day 02, Part 02: %d\n", (100 * i) + j);
        return 0;
      }
    }
  }
  return 0;
}
