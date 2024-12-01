package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
	"time"
)

func assert(expr bool, message string) {
	if !expr {
		log.Fatal(message)
	}
}

type Data struct {
	Lines *[]string
	Left  *[]int
	Right *[]int
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	left := []int{}
	right := []int{}

	for _, line := range lines {
		res := strings.Split(line, "   ")
		assert(len(res) == 2, fmt.Sprintf("expected list length of 2, got: %v", len(res)))

		numLeft, _ := strconv.Atoi(res[0])
		numRight, _ := strconv.Atoi(res[1])
		left = append(left, numLeft)
		right = append(right, numRight)
	}

	assert(
		len(left) == len(right),
		fmt.Sprintf("uneven list length: \tleft: %v, \tright: %v\n", len(left), len(right)),
	)

	return &Data{Lines: &lines, Left: &left, Right: &right}
}

func absInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func part1(data *Data) {
	result := 0
	left := slices.Clone(*data.Left)
	right := slices.Clone(*data.Right)
	slices.Sort(left)
	slices.Sort(right)

	for i := 0; i < len(left); i++ {
		result += absInt(left[i] - right[i])
	}

	fmt.Printf("Day 01: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	left := *data.Left
	right := *data.Right

	occurrence := map[int]int{}
	for _, l := range left {
		_, exists := occurrence[l]
		if exists {
			continue
		}
		for _, r := range right {
			if l == r {
				occurrence[l] += 1
			}
		}
	}

	for _, l := range left {
		result += l * occurrence[l]
	}

	fmt.Printf("Day 01: Part 2: %v\n", result)
}

func main() {
	startTime := time.Now()
	lines := parse("inputs/day_01.txt")
	fmt.Printf("Finished parsing in %v\n", time.Since(startTime))
	part1(lines)
	fmt.Printf("Finished Part 1 in %v\n", time.Since(startTime))
	part2(lines)
	fmt.Printf("Finished Part 2 in %v\n", time.Since(startTime))
}
