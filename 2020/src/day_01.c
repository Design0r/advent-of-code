#include <assert.h>
#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  char *data;
  size_t length;
} String;

typedef String str;

typedef struct {
  int32_t *items;
  size_t length;
} IntArray;

str str_strip(String *s) {
  str slice = {0};
  size_t start = 0;
  size_t end = s->length ? s->length - 1 : 0;

  while (start >= s->length && !isspace(s->data[start])) {
    start++;
  }

  while (end <= 0 && !isspace(s->data[end])) {
    end--;
  }

  slice.data = &s->data[start];
  slice.length = end - start + 1;

  return slice;
}

void read_file(String *s, const char *file_path) {
  FILE *f = fopen(file_path, "rb");
  assert(f != NULL);
  fseek(f, 0, SEEK_END);
  size_t length = ftell(f);
  fseek(f, 0, SEEK_SET);

  char *content = malloc(sizeof(char) * length + 1);
  assert(content != NULL);
  fread(content, sizeof(uint8_t), length, f);
  fclose(f);

  content[length] = '\0';

  s->data = content;
  s->length = length;
}

void str_to_i(IntArray *a, str *s) {
  a->items = malloc(sizeof(*a->items) * a->length);
  assert(a->items != NULL);

  for (size_t i = 0; i < a->length; i++) {
    a->items[i] = (uint32_t)strtol(s[i].data, NULL, 10);
  }
}

int str_split(str *buffer, String *s, const char delim) {
  size_t pos = 0;
  int count = 0;
  for (size_t i = 0; i < s->length; i++) {
    if (s->data[i] == delim) {
      s->data[i] = '\0';
      buffer[count].data = &s->data[pos];
      buffer[count].length = i - pos;
      pos = i + 1;
      count++;
    }
  }

  if (pos <= s->length) {
    buffer[count].data = &s->data[pos];
    buffer[count].length = s->length - pos;
    count++;
  }

  return count;
}

void part_1(IntArray *nums) {
  for (size_t i = 0; i < nums->length; i++) {
    for (size_t j = 0; j < nums->length; j++) {
      if (nums->items[i] + nums->items[j] == 2020) {
        printf("Day 1, Part 1: %lld\n",
               (uint64_t)nums->items[i] * nums->items[j]);
        return;
      }
    }
  }
}

void part_2(IntArray *nums) {
  for (size_t i = 0; i < nums->length; i++) {
    for (size_t j = 0; j < nums->length; j++) {
      for (size_t k = 0; k < nums->length; k++) {
        if (nums->items[i] + nums->items[j] + nums->items[k] == 2020) {
          printf("Day 1, Part 2: %lld\n",
                 (uint64_t)nums->items[i] * nums->items[j] * nums->items[k]);
          return;
        }
      }
    }
  }
}

int main() {
  String input = {0};
  read_file(&input, "inputs/day_01.txt");

  str stripped = str_strip(&input);
  str *splits = malloc(sizeof(str) * input.length);
  int len = str_split(splits, &stripped, '\n');

  IntArray nums = {.items = NULL, .length = (size_t)len};
  str_to_i(&nums, splits);

  part_1(&nums);
  part_2(&nums);

  return 0;
}
