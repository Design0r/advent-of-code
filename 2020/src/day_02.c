#include <stdio.h>
#include <string.h>

#define PW_LEN 64

int count_char(const char *string, char c) {
  int count = 0;
  for (int i = 0; i < strlen(string); i++) {
    if (string[i] == c)
      count++;
  }

  return count;
}

int main() {

  FILE *file = fopen("inputs/day_02.txt", "r");
  int lower, upper = 0;
  char rule = 0;
  char pw[PW_LEN];

  int result_p1 = 0;
  int result_p2 = 0;

  while (fscanf(file, "%d-%d %c: %s/n", &lower, &upper, &rule, pw) == 4) {
    int occ = count_char(pw, rule);
    if (occ >= lower && occ <= upper)
      result_p1++;

    char l = pw[lower - 1];
    char u = pw[upper - 1];
    if ((l == rule && u != rule) || (l != rule && u == rule))
      result_p2++;
  }

  printf("Day 2, Part 1: %d\n", result_p1);
  printf("Day 2, Part 2: %d\n", result_p2);

  fclose(file);
  return 0;
}
