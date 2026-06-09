#include "array.h"
#include "ctype.h"
#include "limits.h"
#include "stdio.h"
#include "stdlib.h"
#include <math.h>

typedef struct {
  int *items;
  size_t length;
  size_t capacity;
} IntArray;

size_t read_file(const char *file_name, char **file) {
  FILE *f = fopen(file_name, "r");
  fseek(f, 0, SEEK_END);
  size_t len = ftell(f);

  rewind(f);

  void *buf = malloc(len);
  if (!buf) {
    fclose(f);
    return 0;
  }

  *file = buf;
  fread(buf, 1, len, f);
  fclose(f);

  return len;
}

int main() {
  char *file = NULL;
  size_t file_len = read_file("inputs/day_02.txt", &file);
  if (file_len == 0)
    return 1;

  size_t idx = file_len - 1;
  if (file[idx] == '\n' && idx > 0) {
    idx--;
  }

  int result = 0;
  IntArray line = {0};
  int result2 = 0;

  while (idx >= 0) {
    int min = INT_MAX;
    int max = 0;

    int digits = 0;
    int val = 0;

    while (1) {
      char curr = file[idx];

      if (isspace(curr)) {
        if (digits > 0) {
          da_append(&line, val);

          min = val < min ? val : min;
          max = val > max ? val : max;
          digits = 0;
          val = 0;
        }

        if (curr == '\n') {
          if (idx > 0)
            idx--;
          break;
        }

        if (idx == 0)
          break;
        idx--;
        continue;
      }

      int digit_val = (curr >= '0' && curr <= '9') ? (curr - '0') : 0;
      val += digit_val * (powl(10, digits));
      digits++;

      if (idx == 0) {
        if (digits > 0) {
          da_append(&line, val);
          min = val < min ? val : min;
          max = val > max ? val : max;
        }
        break;
      }
      idx--;
    }

    for (size_t i = 0; i < da_len(&line); i++) {
      for (size_t j = 0; j < da_len(&line); j++) {
        if (i == j)
          continue;
        int a = da_get(&line, i);
        int b = da_get(&line, j);

        if (b != 0 && a % b == 0) {
          result2 += a / b;
          goto loop_end;
        }
      }
    }

  loop_end:
    da_clear(&line);

    if (max >= min) {
      result += max - min;
    }

    if (idx == 0) {
      break;
    }
  }

  printf("Day 02, Part 1: %d\n", result);
  printf("Day 02, Part 2: %d\n", result2);

  free(file);
  return 0;
}
