#include <stddef.h>
#include <stdio.h>
#define CSTD_IMPLEMENTATION
#include "cstd.h"

Str read_file(const char *path) {
  Str result = {0};

  FILE *f = fopen(path, "rb");
  if (!f) {
    return result;
  }

  fseek(f, 0, SEEK_END);
  size_t size = ftell(f);
  fseek(f, 0, SEEK_SET);

  char *data = malloc(size + 1);
  fread(data, 1, size, f);

  fclose(f);

  data[size] = '\0';

  result.data = data;
  result.len = size;

  return result;
}

int part_01(Str content, int *code_length) {
  int code_len = 0;
  int mem_len = 0;
  size_t cursor = 0;

  while (cursor < content.len) {
    char curr = content.data[cursor++];
    code_len++;

    switch (curr) {
    case '\\': {
      char next = content.data[cursor++];
      code_len++;
      mem_len++;

      if (next == 'x') {
        cursor += 2;
        code_len += 2;
      }

    } break;

    case '"':
      break;
    case '\n': {
      code_len--;
    } break;

    default:
      mem_len++;
      break;
    }
  }

  *code_length = code_len;

  return code_len - mem_len;
}

int part_02(Str content, int code_len) {
  int escaped_len = 2;
  size_t cursor = 0;

  while (cursor < content.len) {
    char curr = content.data[cursor++];
    escaped_len++;

    switch (curr) {
    case '\\': {
      char next = content.data[cursor];
      escaped_len++;
      if (next == 'x') {
        cursor += 3;
        escaped_len += 3;
      }
    } break;

    case '"':
    case '\n': {
      escaped_len++;
    } break;
    }
  }

  return escaped_len - code_len;
}

int main(void) {
  Str content = read_file("inputs/day_08.txt");

  int code_len;

  printf("Day 08, Part 1: %d \n", part_01(content, &code_len));
  printf("Day 08, Part 2: %d \n", part_02(content, code_len));
  return 0;
}
