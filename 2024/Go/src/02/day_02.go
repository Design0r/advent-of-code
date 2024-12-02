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
	NumLines [][]int
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	nums := [][]int{}
	for _, line := range lines {
		lineNums := []int{}
		chars := strings.Split(line, " ")
		for _, char := range chars {
			num, err := strconv.Atoi(char)
			if err != nil {
				log.Fatal("expected number")
			}

			lineNums = append(lineNums, num)
		}
		nums = append(nums, lineNums)
	}

	return &Data{NumLines: nums}
}

func isContinuousLine(line []int) bool {
	set := map[int]int{}
	for i, num := range line {
		if i == 0 {
			continue
		}
		diff := num - line[i-1]
		if aoc.AbsInt(diff) < 1 || aoc.AbsInt(num-line[i-1]) > 3 {
			return false
		}
		if diff > 0 {
			set[1] = num
		} else {
			set[-1] = num
		}
	}
	return len(set) == 1
}

func checkWithTolerance(line []int) bool {
	if isContinuousLine(line) {
		return true
	}

	for i := range line {
		cloned := slices.Clone(line)
		newList := append(cloned[:i], cloned[i+1:]...)
		if isContinuousLine(newList) {
			return true
		}
	}

	return false
}

func part1(data *Data) {
	result := 0

	for _, line := range data.NumLines {
		r := isContinuousLine(line)
		if r {
			result += 1
		}
	}

	fmt.Printf("Day 0: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	for _, line := range data.NumLines {
		r := checkWithTolerance(line)
		if r {
			result += 1
		}
	}
	fmt.Printf("Day 0: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_02.txt")
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
