#include <stdio.h>

int rec_fuel(int num, int *start) {
  int temp = (num / 3) - 2;
  if (temp < 0) {
    return *start;
  }
  *start += temp;
  return rec_fuel(temp, start);
}

int main() {
  FILE *f = fopen("inputs/day_01.txt", "rb");
  int num = 0;
  int result = 0;
  int result2 = 0;
  int start = 0;

  while (fscanf(f, "%d\n", &num) == 1) {
    result += (num / 3) - 2;
    result2 += rec_fuel(num, &start);
    start = 0;
  }

  printf("Day 01, Part 1: %d\n", result);
  printf("Day 01, Part 2: %d\n", result2);

  return 0;
}
