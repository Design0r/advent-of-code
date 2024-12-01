package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
	"time"

	"aoc/src/aoc"
)

type Data struct {
	Lines []string
	Left  []int
	Right []int
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
		aoc.Assert(len(res) == 2, fmt.Sprintf("expected list length of 2, got: %v", len(res)))

		numLeft, _ := strconv.Atoi(res[0])
		numRight, _ := strconv.Atoi(res[1])
		left = append(left, numLeft)
		right = append(right, numRight)
	}

	aoc.Assert(
		len(left) == len(right),
		fmt.Sprintf("uneven list length: \tleft: %v, \tright: %v\n", len(left), len(right)),
	)

	return &Data{Lines: lines, Left: left, Right: right}
}

func part1(data *Data) {
	result := 0
	left := slices.Clone(data.Left)
	right := slices.Clone(data.Right)
	slices.Sort(left)
	slices.Sort(right)

	for i := 0; i < len(left); i++ {
		result += aoc.AbsInt(left[i] - right[i])
	}

	fmt.Printf("Day 01: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0

	occurrence := map[int]int{}
	for _, r := range data.Right {
		occurrence[r] += 1
	}

	for _, l := range data.Left {
		result += l * occurrence[l]
	}

	fmt.Printf("Day 01: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_01.txt")
	parseTime := time.Since(startTime)
	part1StartTime := time.Now()
	part1(lines)
	part1Time := time.Since(part1StartTime)
	part2StartTime := time.Now()
	part2(lines)
	part2Time := time.Since(part2StartTime)

	fmt.Printf("====================================\n")
	fmt.Printf("Finished Parsing in %v\n", parseTime)
	fmt.Printf("Finished Part 1 in %v\n", part1Time)
	fmt.Printf("Finished Part 2 in %v\n", part2Time)
	fmt.Printf("Total %v\n", time.Since(startTime))
	fmt.Printf("------------------------------------\n")
}
