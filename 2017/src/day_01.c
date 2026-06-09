#include "stdio.h"
#include "stdlib.h"
#include <stdio.h>

size_t read_file(const char *file_name, char **file) {
  FILE *f = fopen(file_name, "r");
  fseek(f, 0, SEEK_END);
  size_t len = ftell(f)-1;

  rewind(f);

  void *buf = malloc(len);

  *file = buf;
  fread(buf, 1, len, f);

  return len;
}

int main() {
  char *file = NULL;
  size_t file_len = read_file("inputs/day_01.txt", &file);

  int result1 = 0;
  int result2 = 0;

  size_t jump_dist = file_len / 2;
  for (size_t i = 0; i < file_len; i++) {
    char curr = file[i];
    char next1 = (i == file_len -1) ? file[0] : file[i + 1];
    char next2 = file[(i + jump_dist) % file_len];

    if (curr == next1) result1 += curr - '0';
    if (curr == next2) result2 += curr - '0';
  }

  printf("Day 01, Part 1: %d\n", result1);
  printf("Day 01, Part 2: %d\n", result2);

  return 0;
}
