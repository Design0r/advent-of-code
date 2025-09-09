#pragma once

#include <assert.h>
#include <stdlib.h>

#ifndef DA_INIT_CAP
#define DA_INIT_CAP 256
#endif

/*
 * Allocate memory for a dynamic array
 * */
#define da_alloc(arr, need)                                                    \
  do {                                                                         \
    if ((need) > (arr)->capacity) {                                            \
      if ((arr)->capacity == 0) {                                              \
        (arr)->capacity = DA_INIT_CAP;                                         \
      }                                                                        \
      while ((arr)->capacity < (need)) {                                       \
        (arr)->capacity *= 2;                                                  \
      }                                                                        \
      (arr)->items =                                                           \
          realloc((arr)->items, (arr)->capacity * sizeof(*(arr)->items));      \
      assert((arr)->items != NULL &&                                           \
             "Failed to reallocate dynamic array memory");                     \
    }                                                                          \
  } while (0)

#define da_append(arr, elem)                                                   \
  do {                                                                         \
    da_alloc((arr), (arr)->length + 1);                                        \
    (arr)->items[(arr)->length++] = (elem);                                    \
  } while (0)

#define da_free(arr)                                                           \
  do {                                                                         \
    free((arr).items);                                                         \
    (arr).length = 0;                                                          \
    (arr).capacity = 0;                                                        \
  } while (0)

#define da_last(arr) (arr)->items[assert((arr)->length > 0), (arr)->length - 1]

#define da_pop(arr) (arr)->items[(assert((arr)->length > 0)), --(arr)->length]

#define da_remove(arr, idx)                                                    \
  do {                                                                         \
    assert((arr)->length > idx);                                               \
    (arr)->items[(idx)] = (arr)->items[--(arr)->length];                       \
  } while (0)

#define da_get(arr, idx)                                                       \
  (arr)->items[assert((arr)->length > (size_t)(idx)), (size_t)(idx)]
#define da_set(arr, idx, val)                                                  \
  (arr)->items[assert((arr)->length > (size_t)(idx)), (size_t)(idx)] = (val)
