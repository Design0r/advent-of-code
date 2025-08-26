#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_SLOPES 4

typedef struct {
  int x, y;
} Vec2;

char *read_file(const char *file_path) {
  FILE *file = fopen(file_path, "r");
  fseek(file, 0, SEEK_END);
  size_t length = ftell(file);
  rewind(file);

  char *content = malloc(sizeof(char) * length);
  fread(content, sizeof(char), length, file);
  fclose(file);

  return content;
}

Vec2 get_dimensions(char *input) {
  int width = 0, height = 0;
  size_t i = 0;
  while (1) {
    if (input[i] == '\n')
      break;
    i++;
  }

  width = i;
  height = (strlen(input) / width) - 1;

  return (Vec2){.x = width, .y = height};
}

int count_trees(const char *input, Vec2 dimensions, Vec2 offset) {
  int x = 0, y = 0, trees = 0;

  while (y < dimensions.y) {
    // width + 1 to account for \n;
    int idx = ((y * (dimensions.x + 1)) + (x % dimensions.x));
    if (input[idx] == '#') {
      trees++;
    }

    x += offset.x;
    y += offset.y;
  }

  return trees;
}

int main() {
  char *input = read_file("inputs/day_03.txt");
  Vec2 dimensions = get_dimensions(input);

  const Vec2 slopes[NUM_SLOPES] = {{1, 1}, {5, 1}, {7, 1}, {1, 2}};

  size_t trees = count_trees(input, dimensions, (Vec2){.x = 3, .y = 1});
  printf("Day 3, Part 1: %zu\n", trees);

  for (int i = 0; i < NUM_SLOPES; i++) {
    trees *= (size_t)count_trees(input, dimensions, slopes[i]);
  }
  printf("Day 3, Part 2: %zu\n", trees);

  return 0;
}
