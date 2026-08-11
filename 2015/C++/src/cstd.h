#pragma once

#ifndef CSTD_DEF
#define CSTD_DEF
#endif

#ifdef __cplusplus
#define STRUCT_LIT(type) type
#else
#define STRUCT_LIT(type) (type)
#endif

#ifdef __cplusplus
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#else
#include <assert.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#endif

// ========
// String
// ========

struct Str;
struct String;

typedef struct String {
	size_t len;
	const char *data;

#ifdef __cplusplus
	size_t length();
	bool startswith(Str slice);
	Str to_str();
	void free();
	static String from(const char *cstr);
	static String from(char *cstr);
#endif
} String;

typedef struct Str {
	size_t len;
	const char *data;

#ifdef __cplusplus
	[[nodiscard]] Str trim_left() const;
	[[nodiscard]] Str trim_right() const;
	[[nodiscard]] Str trim() const;
	[[nodiscard]] size_t length() const;
	int split(char delim, Str *out, int out_size) const;
	int split_str(Str delim, Str *out, int out_size) const;
	[[nodiscard]] bool eq(Str b) const;
	[[nodiscard]] bool startswith_str(Str b) const;
	bool startswith_cstr(const char *cstr) const;
	[[nodiscard]] String to_string() const;
	void to_cstr(char *buf) const;
	[[nodiscard]] char *to_cstr() const;
	static Str from(const char *cstr);
	static Str from(char *cstr);
#endif
} Str;

// ========
// Math
// ========

#define VEC2_FMT "Vec2: x: %f, y: %f"
#define VEC2_SPREAD(vec) vec.x, vec.y

#define VEC3_FMT "Vec3: x: %f, y: %f, z: %f"
#define VEC3_SPREAD(vec) vec.x, vec.y, vec.z

#define MAX(x, y) ((x) > (y)) ? (x) : (y)
#define MIN(x, y) ((x) < (y)) ? (x) : (y)

typedef struct Vec2 {
	float x, y;

#ifdef __cplusplus
	float len() const;
	Vec2 normalize() const;
	Vec2 dir(Vec2 b) const;
	float angle() const;
	bool eq(Vec2 b, float delta) const;
	Vec2 max(float b) const;
	Vec2 max(Vec2 b) const;
	Vec2 min(float b) const;
	Vec2 min(Vec2 b) const;
	Vec2 invert() const;
	float dist_sq(Vec2) const;
	bool is_zero() const;
#endif
} Vec2;

typedef struct IVec2 {
	int x, y;
} IVec2;

typedef struct Vec3 {
	float x, y, z;

#ifdef __cplusplus
	float len() const;
	Vec3 normalize() const;
	Vec3 dir(Vec3 b) const;
	float angle_y() const;
	bool eq(Vec3 b, float delta) const;
	Vec3 max(float b) const;
	Vec3 max(Vec3 b) const;
	Vec3 min(float b) const;
	Vec3 min(Vec3 b) const;
	Vec3 invert() const;
	float dist_sq(Vec3) const;
	bool is_zero() const;
#endif
} Vec3;

// ========
// Dynamic Array
// ========

#ifndef DA_INIT_CAP
#define DA_INIT_CAP 256
#endif

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

#define da_pop(arr) (arr)->items[assert((arr)->length > 0), --(arr)->length]

#define da_remove(arr, idx)                                                    \
  do {                                                                         \
    assert((arr)->length > idx);                                               \
    (arr)->items[(idx)] = (arr)->items[--(arr)->length];                       \
  } while (0)

#define da_get(arr, idx)                                                       \
  (arr)->items[assert((arr)->length > (size_t)(idx)), (size_t)(idx)]

#define da_set(arr, idx, val)                                                  \
  (arr)->items[assert((arr)->length > (size_t)(idx)), (size_t)(idx)] = (val)

#define da_clear(arr)                                                          \
  do {                                                                         \
    (arr)->length = 0;                                                         \
  } while (0)

#define da_len(arr) (arr)->length

// ========
// Arena
// ========

typedef struct {
	size_t capacity;
	size_t cursor;
	uint8_t *memory;
} Arena;

// ========
// String
// ========

#define STR(s)                                                                 \
  (Str) { .len = sizeof(s) - 1, .data = s }
#define STRING(s)                                                              \
  (String) { .len = sizeof(s) - 1, .data = s }

#define STR_FMT "%.*s"
#define STR_ARG(s) (int)s.len, s.data

#define STR_FOR(s, i) for (size_t i = 0; i < s.len; i++)

const char WHITESPACE[] = " \r\t\n\0";
CSTD_DEF bool is_whitespace(char c);

CSTD_DEF String string_from_cstr(const char *cstr);
CSTD_DEF size_t string_len(String s);
CSTD_DEF bool string_startswith_str(String s, Str slice);
CSTD_DEF Str string_to_str(String s);
CSTD_DEF void string_free(String s);

// ========
// Str
// ========

CSTD_DEF Str str(const char *cstr, size_t len);
CSTD_DEF Str str_from_cstr(const char *cstr);
CSTD_DEF Str str_trim_left(Str s);
CSTD_DEF Str str_trim_right(Str s);
CSTD_DEF Str str_trim(Str s);
CSTD_DEF size_t str_len(Str s);
CSTD_DEF Str str_copy(Str s);
CSTD_DEF Str str_copy_offset(Str s, size_t offset);
CSTD_DEF int str_split(Str s, char delim, Str *out, int out_size);
CSTD_DEF int str_split_str(Str s, Str delim, Str *out, int out_size);
CSTD_DEF bool str_eq(Str a, Str b);
CSTD_DEF bool str_startswith_str(Str a, Str b);
CSTD_DEF bool str_startswith_cstr(Str a, const char *cstr);
CSTD_DEF String str_to_string(Str s);
CSTD_DEF void str_to_cstr(Str s, char *buf);
CSTD_DEF char *str_to_cstr_m(Str s);

// ==================================
// Vec 2
// ==================================

CSTD_DEF Vec2 vec2(float x, float y);
CSTD_DEF Vec2 vec2_add(Vec2 a, Vec2 b);
CSTD_DEF Vec2 vec2_addf(Vec2 a, float b);
CSTD_DEF Vec2 vec2_sub(Vec2 a, Vec2 b);
CSTD_DEF Vec2 vec2_subf(Vec2 a, float b);
CSTD_DEF Vec2 vec2_mul(Vec2 a, Vec2 b);
CSTD_DEF Vec2 vec2_mulf(Vec2 a, float b);
CSTD_DEF Vec2 vec2_div(Vec2 a, Vec2 b);
CSTD_DEF Vec2 vec2_divf(Vec2 a, float b);
CSTD_DEF float vec2_len(Vec2 v);
CSTD_DEF Vec2 vec2_normalize(Vec2 a);
CSTD_DEF Vec2 vec2_dir(Vec2 a, Vec2 b);
CSTD_DEF float vec2_angle(Vec2 a);
CSTD_DEF bool vec2_eq(Vec2 a, Vec2 b, float delta);
CSTD_DEF Vec2 vec2_max(Vec2 a, Vec2 b);
CSTD_DEF Vec2 vec2_maxf(Vec2 a, float b);
CSTD_DEF Vec2 vec2_min(Vec2 a, Vec2 b);
CSTD_DEF Vec2 vec2_minf(Vec2 a, float b);
CSTD_DEF Vec2 vec2_invert(Vec2 a);
CSTD_DEF float vec2_dist_sq(Vec2 a, Vec2);
CSTD_DEF bool vec2_is_zero(Vec2 a);

#ifdef __cplusplus
CSTD_DEF Vec2 operator+(Vec2 a, Vec2 b);
CSTD_DEF Vec2 operator+(Vec2 a, float b);
CSTD_DEF Vec2 operator+(float a, Vec2 b);
CSTD_DEF Vec2&operator+=(Vec2&a, Vec2 b);
CSTD_DEF Vec2&operator+=(Vec2&a, float b);

CSTD_DEF Vec2 operator-(Vec2 a, Vec2 b);
CSTD_DEF Vec2&operator-=(Vec2&a, Vec2 b);

CSTD_DEF Vec2 operator *(Vec2 a, Vec2 b);
CSTD_DEF Vec2 operator *(Vec2 a, float b);
CSTD_DEF Vec2 operator *(float a, Vec2 b);
CSTD_DEF Vec2&operator*=(Vec2&a, Vec2 b);
CSTD_DEF Vec2&operator*=(Vec2&a, float b);

CSTD_DEF Vec2 operator/(Vec2 a, Vec2 b);
CSTD_DEF Vec2 operator/(Vec2 a, float b);
CSTD_DEF Vec2 operator/(float a, Vec2 b);
CSTD_DEF Vec2&operator/=(Vec2&a, Vec2 b);
CSTD_DEF Vec2&operator/=(Vec2&a, float b);
#endif

// ==================================
// IVec 2
// ==================================

CSTD_DEF IVec2 ivec2(int x, int y);
CSTD_DEF IVec2 vec2_to_ivec2(Vec2 a);
CSTD_DEF Vec2 ivec2_to_vec2(IVec2 a);

// ==================================
// Vec 3
// ==================================

CSTD_DEF Vec3 vec3(float x, float y, float z);
CSTD_DEF Vec3 vec3_add(Vec3 a, Vec3 b);
CSTD_DEF Vec3 vec3_addf(Vec3 a, float b);
CSTD_DEF Vec3 vec3_sub(Vec3 a, Vec3 b);
CSTD_DEF Vec3 vec3_subf(Vec3 a, float b);
CSTD_DEF Vec3 vec3_mul(Vec3 a, Vec3 b);
CSTD_DEF Vec3 vec3_mulf(Vec3 a, float b);
CSTD_DEF Vec3 vec3_div(Vec3 a, Vec3 b);
CSTD_DEF Vec3 vec3_divf(Vec3 a, float b);
CSTD_DEF Vec3 vec3_max(Vec3 a, Vec3 b);
CSTD_DEF Vec3 vec3_maxf(Vec3 a, float b);
CSTD_DEF Vec3 vec3_min(Vec3 a, Vec3 b);
CSTD_DEF Vec3 vec3_minf(Vec3 a, float b);
CSTD_DEF Vec3 vec3_invert(Vec3 a);
CSTD_DEF float vec3_dist_sq(Vec3 a, Vec3 b);
CSTD_DEF float vec3_len(Vec3 a);
CSTD_DEF Vec3 vec3_normalize(Vec3 a);
CSTD_DEF Vec3 vec3_dir(Vec3 a, Vec3 b);
CSTD_DEF float vec3_angle_y(Vec3 a);
CSTD_DEF bool vec3_eq(Vec3 a, Vec3 b, float delta);
CSTD_DEF bool vec3_is_zero(Vec3 a);

#ifdef __cplusplus
CSTD_DEF Vec3 operator+(Vec3 a, Vec3 b);
CSTD_DEF Vec3 operator+(Vec3 a, float b);
CSTD_DEF Vec3 operator+(float a, Vec3 b);
CSTD_DEF Vec3&operator+=(Vec3&a, Vec3 b);
CSTD_DEF Vec3&operator+=(Vec3&a, float b);

CSTD_DEF Vec3 operator-(Vec3 a, Vec3 b);
CSTD_DEF Vec3&operator-=(Vec3&a, Vec3 b);

CSTD_DEF Vec3 operator *(Vec3 a, Vec3 b);
CSTD_DEF Vec3 operator *(Vec3 a, float b);
CSTD_DEF Vec3 operator *(float a, Vec3 b);
CSTD_DEF Vec3&operator*=(Vec3&a, Vec3 b);
CSTD_DEF Vec3&operator*=(Vec3&a, float b);

CSTD_DEF Vec3 operator/(Vec3 a, Vec3 b);
CSTD_DEF Vec3 operator/(Vec3 a, float b);
CSTD_DEF Vec3 operator/(float a, Vec3 b);
CSTD_DEF Vec3&operator/=(Vec3&a, Vec3 b);
CSTD_DEF Vec3&operator/=(Vec3&a, float b);
#endif

// ==================================
// Arena
// ==================================

CSTD_DEF void arena_init(Arena *a, size_t size, uint8_t *memory);
CSTD_DEF void arena_init_malloc(Arena *a, size_t size);
#define arena_alloc_type(arena, type) (type *)arena_alloc_aligned((arena), sizeof(type), _Alignof(type))

#define arena_alloc(arena, type, count) (type *)arena_alloc_aligned((arena), sizeof(type) * count, _Alignof(type))

CSTD_DEF uint8_t *arena_alloc_aligned(Arena *a, size_t size, size_t align);
CSTD_DEF void arena_free(Arena *a);
CSTD_DEF void arena_clear(Arena *a);

#ifdef CSTD_IMPLEMENTATION

// ========
// Utils
// ========

CSTD_DEF bool is_whitespace(const char c) {
	for (size_t i = 0; i < sizeof(WHITESPACE); i++) {
		if (c == WHITESPACE[i])
			return true;
	}

	return false;
}

// ========
// String
// ========

CSTD_DEF String string_from_cstr(const char *cstr) {
	size_t len = strlen(cstr);
	char *new_data = (char *) malloc(len);
	memcpy(new_data, cstr, len);
	return (String){.len = len, .data = new_data};
}

CSTD_DEF size_t string_len(const String s) { return s.len; }

CSTD_DEF bool string_startswith_str(const String s, const Str slice) {
	if (s.len < slice.len)
		return false;
	return memcmp(s.data, slice.data, slice.len) == 0;
}

CSTD_DEF Str string_to_str(const String s) {
	return (Str){.len = s.len, .data = s.data};
}

CSTD_DEF void string_free(String s) { free((void *) s.data); }

CSTD_DEF Str str(const char *cstr, size_t len) {
	return (Str){.len = len, .data = cstr};
}

// ========
// Str
// ========

CSTD_DEF Str str_trim_left(Str s) {
	for (size_t i = 0; i < s.len; i++) {
		if (!is_whitespace(s.data[i]))
			break;
		s.data++;
		s.len--;
	}

	return s;
}

CSTD_DEF Str str_trim_right(Str s) {
	for (size_t i = s.len - 1; i > 0; i--) {
		if (!is_whitespace(s.data[i]))
			break;
		s.len--;
	}

	return s;
}

CSTD_DEF Str str_trim(const Str s) {
	return str_trim_right(str_trim_left(s));
}

CSTD_DEF size_t str_len(const Str s) { return s.len; }

CSTD_DEF Str str_copy(const Str s) { return s; }

CSTD_DEF bool str_eq(const Str a, const Str b) {
	if (a.len != b.len)
		return false;
	return memcmp(a.data, b.data, a.len) == 0;
}

CSTD_DEF int str_split(const Str s, const char delim, Str *out,
                       int out_size) {
	int found = 0;
	size_t start = 0;

	STR_FOR(s, i) {
		if (s.data[i] == delim) {
			if (i > start) {
				if (found >= out_size)
					return found;
				out[found++] = (Str){.len = i - start, .data = s.data + start};
			}
			start = i + 1;
		}
	}

	if (s.len > start && found < out_size) {
		out[found++] = (Str){.len = s.len - start, .data = s.data + start};
	}

	return found;
}

CSTD_DEF int str_split_str(Str s, Str delim, Str *out, int out_size) {
	int found = 0;
	size_t start = 0;

	STR_FOR(s, i) {
		Str temp = str(s.data + i, delim.len);
		if (str_eq(temp, delim)) {
			if (i > start) {
				if (found >= out_size)
					return found;
				out[found++] = (Str){.len = i - start, .data = s.data + start};
			}
			start = i + delim.len;
		}
	}

	if (s.len > start && found < out_size) {
		out[found++] = (Str){.len = s.len - start, .data = s.data + start};
	}

	return found;
}

CSTD_DEF Str str_from_cstr(const char *cstr) {
	return (Str){.len = strlen(cstr), .data = cstr};
}

CSTD_DEF bool str_startswith_str(const Str a, const Str b) {
	if (a.len < b.len)
		return false;
	return memcmp(a.data, b.data, b.len) == 0;
}

CSTD_DEF bool str_startswith_cstr(Str a, const char *cstr) {
	size_t len = strlen(cstr);
	if (a.len < len)
		return false;
	return memcmp(a.data, cstr, len) == 0;
}

CSTD_DEF String str_to_string(Str s) {
	char *new_data = (char *) malloc(s.len);
	memcpy(new_data, s.data, s.len);
	return (String){.len = s.len, .data = new_data};
}

CSTD_DEF char *str_to_cstr_m(Str s) {
	char *new_data = (char *) malloc(s.len + 1);
	memcpy(new_data, s.data, s.len);
	new_data[s.len] = '\0';
	return new_data;
}

CSTD_DEF void str_to_cstr(Str s, char *buf) {
	memcpy(buf, s.data, s.len);
	buf[s.len] = '\0';
}

// ==================================
// Vec 2
// ==================================

CSTD_DEF Vec2 vec2(const float x, const float y) {
	return STRUCT_LIT(Vec2){.x = x, .y = y};
};

CSTD_DEF Vec2 vec2_add(Vec2 a, Vec2 b) {
	return vec2(a.x + b.x, a.y + b.y);
}

CSTD_DEF Vec2 vec2_addf(Vec2 a, float b) {
	return vec2(a.x + b, a.y + b);
}

CSTD_DEF Vec2 vec2_sub(Vec2 a, Vec2 b) {
	return vec2(a.x - b.x, a.y - b.y);
}

CSTD_DEF Vec2 vec2_subf(Vec2 a, float b) {
	return vec2(a.x - b, a.y - b);
}

CSTD_DEF Vec2 vec2_mul(Vec2 a, Vec2 b) {
	return vec2(a.x * b.x, a.y * b.y);
}

CSTD_DEF Vec2 vec2_mulf(Vec2 a, float b) {
	return vec2(a.x * b, a.y * b);
}

CSTD_DEF Vec2 vec2_div(Vec2 a, Vec2 b) {
	if (vec2_is_zero(b)) return vec2(0.0f, 0.0f);
	return vec2(a.x / b.x, a.y * b.y);
}

CSTD_DEF Vec2 vec2_divf(Vec2 a, float b) {
	if (b == 0.0f) return vec2(0.0f, 0.0f);
	return vec2(a.x * b, a.y * b);
}

CSTD_DEF float vec2_len(Vec2 v) {
	return sqrtf(v.x * v.x + v.y * v.y);
}

CSTD_DEF Vec2 vec2_normalize(Vec2 a) {
	const float len = vec2_len(a);

	if (len <= 0.00001f) {
		return vec2(0.0f, 0.0f);
	}

	return vec2(a.x / len, a.y / len);
}

CSTD_DEF Vec2 vec2_dir(Vec2 a, Vec2 b) {
	return vec2_normalize(vec2_sub(a, b));
}

CSTD_DEF float vec2_angle(Vec2 a) {
	return atan2f(a.y, a.x);
}

CSTD_DEF bool vec2_eq(Vec2 a, Vec2 b, float delta) {
	Vec2 sub = vec2_sub(a, b);
	return fabsf(sub.x) < delta && fabsf(sub.y) < delta;
}

CSTD_DEF Vec2 vec2_max(Vec2 a, Vec2 b) {
	return vec2(MAX(a.x, b.x), MAX(a.y, b.y));
}

CSTD_DEF Vec2 vec2_maxf(Vec2 a, float b) {
	return vec2(MAX(a.x, b), MAX(a.y, b));
}

CSTD_DEF Vec2 vec2_min(Vec2 a, Vec2 b) {
	return vec2(MIN(a.x, b.x), MIN(a.y, b.y));
}

CSTD_DEF Vec2 vec2_minf(Vec2 a, float b) {
	return vec2(MIN(a.x, b), MIN(a.y, b));
}

CSTD_DEF Vec2 vec2_invert(Vec2 a) {
	return vec2_mulf(a, -1.0f);
}

CSTD_DEF float vec2_dist_sq(const Vec2 a, const Vec2 b) {
	Vec2 diff = vec2_sub(a, b);
	return (diff.x * diff.x) + (diff.y * diff.y);
}

CSTD_DEF bool vec2_is_zero(Vec2 a) {
	return (a.x == 0.0f && a.y == 0.0f);
}

CSTD_DEF IVec2 vec2_to_ivec2(Vec2 a) {
	return ivec2((int) a.x, (int) a.y);
}

// ==================================
// IVec 2
// ==================================

CSTD_DEF IVec2 ivec2(const int x, const int y) {
	return STRUCT_LIT(IVec2){.x = x, .y = y};
}

CSTD_DEF Vec2 ivec2_to_vec2(IVec2 a) {
	return vec2((float) a.x, (float) a.y);
}

// ==================================
// Vec 3
// ==================================

CSTD_DEF Vec3 vec3(const float x, const float y, const float z) {
	return STRUCT_LIT(Vec3){.x = x, .y = y, .z = z};
};

CSTD_DEF Vec3 vec3_add(const Vec3 a, const Vec3 b) {
	return vec3(a.x + b.x, a.y + b.y, a.z + b.z);
}

CSTD_DEF Vec3 vec3_addf(const Vec3 a, const float b) {
	return vec3(a.x + b, a.y + b, a.z + b);
}

CSTD_DEF Vec3 vec3_sub(const Vec3 a, const Vec3 b) {
	return vec3(a.x - b.x, a.y - b.y, a.z - b.z);
}

CSTD_DEF Vec3 vec3_subf(const Vec3 a, const float b) {
	return vec3(a.x - b, a.y - b, a.z - b);
}

CSTD_DEF Vec3 vec3_mul(const Vec3 a, const Vec3 b) {
	return vec3(a.x * b.x, a.y * b.y, a.z * b.z);
}

CSTD_DEF Vec3 vec3_mulf(const Vec3 a, const float b) {
	return vec3(a.x * b, a.y * b, a.z * b);
}

CSTD_DEF Vec3 vec3_div(const Vec3 a, const Vec3 b) {
	if (vec3_is_zero(b)) return vec3(0.0f, 0.0f, 0.0f);
	return vec3(a.x / b.x, a.y / b.y, a.z / b.z);
}

CSTD_DEF Vec3 vec3_divf(const Vec3 a, const float b) {
	if (b == 0.0f) return vec3(0.0f, 0.0f, 0.0f);
	return vec3(a.x / b, a.y / b, a.z / b);
}

CSTD_DEF Vec3 vec3_max(const Vec3 a, const Vec3 b) {
	return vec3(MAX(a.x, b.x), MAX(a.y, b.y), MAX(a.z, b.z));
}

CSTD_DEF Vec3 vec3_maxf(const Vec3 a, const float b) {
	return vec3(MAX(a.x, b), MAX(a.y, b), MAX(a.z, b));
}

CSTD_DEF Vec3 vec3_min(const Vec3 a, const Vec3 b) {
	return vec3(MIN(a.x, b.x), MIN(a.y, b.y), MIN(a.z, b.z));
}

CSTD_DEF Vec3 vec3_minf(const Vec3 a, const float b) {
	return vec3(MIN(a.x, b), MIN(a.y, b), MIN(a.z, b));
}

CSTD_DEF float vec3_len(const Vec3 a) {
	return sqrtf(a.x * a.x + a.y * a.y + a.z * a.z);
}

CSTD_DEF Vec3 vec3_normalize(Vec3 a) {
	const float len = vec3_len(a);

	if (len <= 0.00001f) {
		return vec3(0.0f, 0.0f, 0.0f);
	}

	return vec3(a.x / len, a.y / len, a.z / len);
}

CSTD_DEF Vec3 vec3_dir(const Vec3 a, Vec3 b) { return vec3_normalize(vec3_sub(a, b)); }

CSTD_DEF float vec3_angle_y(Vec3 a) { return atan2f(a.x, a.z); }

CSTD_DEF float vec3_dot(const Vec3 a, const Vec3 b) {
	return (a.x * b.x) + (a.y * b.y) + (a.z * b.z);
}

CSTD_DEF bool vec3_eq(Vec3 a, Vec3 b, float delta) {
	Vec3 sub = vec3_sub(a, b);
	return fabsf(sub.x) < delta && fabsf(sub.y) < delta && fabsf(sub.z) < delta;
}

CSTD_DEF bool vec3_is_zero(Vec3 a) {
	return (a.x == 0.0f && a.y == 0.0f && a.z == 0.0f);
}

CSTD_DEF Vec3 vec3_invert(Vec3 a) {
	return vec3(-a.x, -a.y, -a.z);
}

CSTD_DEF float vec3_dist_sq(Vec3 a, Vec3 b) {
	Vec3 diff = vec3_sub(a, b);
	return (diff.x * diff.x) + (diff.y * diff.y) + (diff.z * diff.z);
}

#ifdef __cplusplus

CSTD_DEF size_t String::length() { return len; }
CSTD_DEF bool String::startswith(Str slice) {
	return string_startswith_str(*this, slice);
}

CSTD_DEF Str String::to_str() { return string_to_str(*this); }

CSTD_DEF void String::free() { return string_free(*this); }

CSTD_DEF String String::from(const char *cstr) {
	return string_from_cstr(cstr);
}

CSTD_DEF String String::from(char *cstr) { return string_from_cstr(cstr); }

CSTD_DEF Str Str::trim_left() const { return str_trim_left(*this); }

CSTD_DEF Str Str::trim_right() const { return str_trim_right(*this); }

CSTD_DEF Str Str::trim() const { return str_trim(*this); }

CSTD_DEF size_t Str::length() const { return str_len(*this); }

CSTD_DEF int Str::split(char delim, Str *out, int out_size) const {
	return str_split(*this, delim, out, out_size);
}

CSTD_DEF int Str::split_str(Str delim, Str *out, int out_size) const {
	return str_split_str(*this, delim, out, out_size);
}

CSTD_DEF bool Str::eq(Str b) const { return str_eq(*this, b); }

CSTD_DEF bool Str::startswith_str(Str b) const {
	return str_startswith_str(*this, b);
}

CSTD_DEF bool Str::startswith_cstr(const char *cstr) const {
	return str_startswith_cstr(*this, cstr);
}

CSTD_DEF String Str::to_string() const { return str_to_string(*this); }

CSTD_DEF void Str::to_cstr(char *buf) const { str_to_cstr(*this, buf); }

CSTD_DEF char *Str::to_cstr() const { return str_to_cstr_m(*this); }

CSTD_DEF Str Str::from(char *cstr) {
	return str_from_cstr(cstr);
}

CSTD_DEF Str Str::from(const char *cstr) {
	return str_from_cstr(cstr);
}

// ==================================
// Vec 2
// ==================================

CSTD_DEF float Vec2::len() const {
	return vec2_len(*this);
}

CSTD_DEF Vec2 Vec2::normalize() const {
	return vec2_normalize(*this);
}

CSTD_DEF Vec2 Vec2::dir(const Vec2 b) const {
	return vec2_dir(*this, b);
}

CSTD_DEF float Vec2::angle() const {
	return vec2_angle(*this);
}

CSTD_DEF bool Vec2::eq(const Vec2 b, const float delta) const {
	return vec2_eq(*this, b, delta);
}

CSTD_DEF Vec2 Vec2::max(const float b) const {
	return vec2_maxf(*this, b);
}

CSTD_DEF Vec2 Vec2::max(const Vec2 b) const {
	return vec2_max(*this, b);
}

CSTD_DEF Vec2 Vec2::min(const float b) const {
	return vec2_minf(*this, b);
}

CSTD_DEF Vec2 Vec2::min(const Vec2 b) const {
	return vec2_min(*this, b);
}

CSTD_DEF Vec2 Vec2::invert() const {
	return vec2_invert(*this);
}

CSTD_DEF float Vec2::dist_sq(const Vec2 b) const {
	return vec2_dist_sq(*this, b);
}

CSTD_DEF bool Vec2::is_zero() const {
	return vec2_is_zero(*this);
}

CSTD_DEF Vec2 operator+(Vec2 a, Vec2 b) {
	return vec2_add(a, b);
}

CSTD_DEF Vec2 operator+(Vec2 a, float b) {
	return vec2_addf(a, b);
}

CSTD_DEF Vec2 operator+(float a, Vec2 b) {
	return vec2_addf(b, a);
}

CSTD_DEF Vec2&operator+=(Vec2&a, Vec2 b) {
	a.x += b.x;
	a.y += b.y;
	return a;
}

CSTD_DEF Vec2&operator+=(Vec2&a, float b) {
	a.x += b;
	a.y += b;
	return a;
}

CSTD_DEF Vec2 operator-(Vec2 a, Vec2 b) {
	return vec2_sub(a, b);
}

CSTD_DEF Vec2&operator-=(Vec2&a, Vec2 b) {
	a.x -= b.x;
	a.y -= b.y;
	return a;
}

CSTD_DEF Vec2 operator *(Vec2 a, Vec2 b) {
	return vec2_mul(a, b);
}

CSTD_DEF Vec2 operator *(Vec2 a, float b) {
	return vec2_mulf(a, b);
}

CSTD_DEF Vec2 operator *(float a, Vec2 b) {
	return vec2_mulf(b, a);
}

CSTD_DEF Vec2&operator*=(Vec2&a, Vec2 b) {
	a.x *= b.x;
	a.y *= b.y;
	return a;
}

CSTD_DEF Vec2&operator*=(Vec2&a, float b) {
	a.x *= b;
	a.y *= b;
	return a;
}

CSTD_DEF Vec2 operator/(Vec2 a, Vec2 b) {
	return vec2_div(a, b);
}

CSTD_DEF Vec2 operator/(Vec2 a, float b) {
	return vec2_divf(a, b);
}

CSTD_DEF Vec2 operator/(float a, Vec2 b) {
	return vec2_divf(b, a);
}

CSTD_DEF Vec2&operator/=(Vec2&a, Vec2 b) {
	if (vec2_is_zero(b)) {
		a.x = 0;
		a.y = 0;
	} else {
		a.x /= b.x;
		a.y /= b.y;
	}

	return a;
}

CSTD_DEF Vec2&operator/=(Vec2&a, float b) {
	if (b == 0.0f) {
		a.x = 0;
		a.y = 0;
	} else {
		a.x /= b;
		a.y /= b;
	}

	return a;
}

// ==================================
// Vec 3
// ==================================

CSTD_DEF float Vec3::dist_sq(const Vec3 b) const {
	return vec3_dist_sq(*this, b);
}

CSTD_DEF bool Vec3::is_zero() const {
	return vec3_is_zero(*this);
}

CSTD_DEF float Vec3::len() const {
	return vec3_len(*this);
}

CSTD_DEF Vec3 Vec3::normalize() const {
	return vec3_normalize(*this);
}

CSTD_DEF Vec3 Vec3::dir(const Vec3 b) const {
	return vec3_dir(*this, b);
}

CSTD_DEF float Vec3::angle_y() const {
	return vec3_angle_y(*this);
}

CSTD_DEF bool Vec3::eq(const Vec3 b, const float delta) const {
	return vec3_eq(*this, b, delta);
}

CSTD_DEF Vec3 Vec3::max(const float b) const {
	return vec3_maxf(*this, b);
}

CSTD_DEF Vec3 Vec3::max(const Vec3 b) const {
	return vec3_max(*this, b);
}

CSTD_DEF Vec3 Vec3::min(const float b) const {
	return vec3_minf(*this, b);
}

CSTD_DEF Vec3 Vec3::min(const Vec3 b) const {
	return vec3_min(*this, b);
}

CSTD_DEF Vec3 Vec3::invert() const {
	return vec3_invert(*this);
}

CSTD_DEF Vec3 operator+(Vec3 a, Vec3 b) {
	return vec3_add(a, b);
}

CSTD_DEF Vec3 operator+(Vec3 a, float b) {
	return vec3_addf(a, b);
}

CSTD_DEF Vec3 operator+(float a, Vec3 b) {
	return vec3_addf(b, a);
}

CSTD_DEF Vec3&operator+=(Vec3&a, Vec3 b) {
	a.x += b.x;
	a.y += b.y;
	a.z += b.z;
	return a;
}

CSTD_DEF Vec3&operator+=(Vec3&a, float b) {
	a.x += b;
	a.y += b;
	a.z += b;
	return a;
}

CSTD_DEF Vec3 operator-(Vec3 a, Vec3 b) {
	return vec3_sub(a, b);
}

CSTD_DEF Vec3&operator-=(Vec3&a, Vec3 b) {
	a.x -= b.x;
	a.y -= b.y;
	a.z -= b.z;
	return a;
}

CSTD_DEF Vec3 operator *(Vec3 a, Vec3 b) {
	return vec3_mul(a, b);
}

CSTD_DEF Vec3 operator *(Vec3 a, float b) {
	return vec3_mulf(a, b);
}

CSTD_DEF Vec3 operator *(float a, Vec3 b) {
	return vec3_mulf(b, a);
}

CSTD_DEF Vec3&operator*=(Vec3&a, Vec3 b) {
	a.x *= b.x;
	a.y *= b.y;
	a.z *= b.z;
	return a;
}

CSTD_DEF Vec3&operator*=(Vec3&a, float b) {
	a.x *= b;
	a.y *= b;
	a.z *= b;
	return a;
}

CSTD_DEF Vec3 operator/(Vec3 a, Vec3 b) {
	return vec3_div(a, b);
}

CSTD_DEF Vec3 operator/(Vec3 a, float b) {
	return vec3_divf(a, b);
}

CSTD_DEF Vec3 operator/(float a, Vec3 b) {
	return vec3_divf(b, a);
}

CSTD_DEF Vec3&operator/=(Vec3&a, Vec3 b) {
	if (vec3_is_zero(b)) {
		a.x = 0;
		a.y = 0;
		a.z = 0;
	} else {
		a.x /= b.x;
		a.y /= b.y;
		a.z /= b.z;
	}

	return a;
}

CSTD_DEF Vec3&operator/=(Vec3&a, float b) {
	if (b == 0.0f) {
		a.x = 0;
		a.y = 0;
		a.z = 0;
	} else {
		a.x /= b;
		a.y /= b;
		a.z /= b;
	}

	return a;
}

// ==================================
// Arena
// ==================================

CSTD_DEF void arena_init(Arena *a, const size_t size, uint8_t *memory) {
	assert(memory && "arena initialized with memory nullptr");
	a->capacity = size;
	a->memory = memory;
	a->cursor = 0;
}

CSTD_DEF void arena_init_malloc(Arena *a, const size_t size) {
	a->capacity = size;
	a->memory = (uint8_t *) malloc(size);
	a->cursor = 0;
}

CSTD_DEF uint8_t *arena_alloc_aligned(Arena *a, const size_t size, const size_t align) {
	if (!a) return NULL;

	uintptr_t current = (uintptr_t) &a->memory[a->cursor];
	uintptr_t aligned = (current + (align - 1)) & ~(align - 1);
	size_t padding = aligned - current;

	if (a->cursor + padding + size > a->capacity) return NULL;

	a->cursor += padding;
	uint8_t *ptr = &a->memory[a->cursor];
	a->cursor += size;
	return ptr;
}

CSTD_DEF void arena_free(Arena *a) {
	if (!a) return;
	if (a->memory) free(a->memory);
}

CSTD_DEF void arena_clear(Arena *a) {
	a->cursor = 0;
}

#endif

#endif
