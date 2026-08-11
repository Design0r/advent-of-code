#include <cstdio>
#include <cstdlib>

#define DIAL_VALUES 100

int rotate(int curr, char dir, int amount) {
  int dir_mul = dir == 'L' ? -1 : 1;
  int new_val = curr + (amount * dir_mul);

  return new_val % DIAL_VALUES;
}

int main() {
  FILE *f = fopen("inputs/day_01.txt", "r");
  int pointer = 50;
  int pointer_2 = 50;
  int result_1 = 0;
  int result_2 = 0;

  char buf[16];
  while (fgets(buf, sizeof(buf), f)) {
    char dir = buf[0];
    int amount = (int)strtol(buf + 1, nullptr, 10);
    pointer = rotate(pointer, dir, amount);
    if (pointer == 0)
      result_1++;

    int dir_amount = dir == 'L' ? -1 : 1;
    for (int i = 0; i < amount; i++) {
      pointer_2 = (pointer_2 + dir_amount) % DIAL_VALUES;
      if (pointer_2 == 0)
        result_2++;
    }
  }

  printf("Day 01, Part 1: %d\n", result_1);
  printf("Day 01, Part 2: %d\n", result_2);

  return 0;
}
