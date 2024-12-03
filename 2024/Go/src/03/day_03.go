package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

type Data struct {
	Input string
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))

	return &Data{Input: stripped}
}

func peak(start int, length int, input *string) string {
	if start+length > len(*input) {
		return ""
	}
	return string((*input)[start : start+length])
}

func parseNums(start int, input *string) (int, int) {
	in := *input

	num := []byte{}
	i := start
	for in[i] != ')' {
		curr := in[i]
		if i-start > 7 {
			return 0, 0
		}
		if curr >= '0' && curr <= '9' || curr == ',' {
			num = append(num, curr)
		}
		i++
	}

	split := strings.Split(string(num), ",")
	if len(split) != 2 {
		return 0, 0
	}

	num1, err := strconv.Atoi(split[0])
	if err != nil {
		log.Fatalf("failed to convert to int: %v", split[0])
	}
	num2, err := strconv.Atoi(split[1])
	if err != nil {
		log.Fatalf("failed to convert to int: %v", split[1])
	}

	return num1, num2
}

func part1(data *Data) {
	mul := "mul("
	result, cursor := 0, 0
	for cursor <= len(data.Input) {
		if window := peak(cursor, len(mul), &data.Input); window == mul {
			num1, num2 := parseNums(cursor+len(mul), &data.Input)
			result += num1 * num2
		}
		cursor++
	}
	fmt.Printf("Day 0: Part 1: %v\n", result)
}

func part2(data *Data) {
	mul, do, dont := "mul(", "do()", "don't()"
	result, cursor := 0, 0
	enabled := true
	for cursor <= len(data.Input) {
		window := peak(cursor, len(dont), &data.Input)
		if len(window) < len(mul) {
			break
		}

		if window[:len(mul)] == mul {
			num1, num2 := parseNums(cursor+len(mul), &data.Input)
			if enabled {
				result += num1 * num2
			}
		} else if window[:len(do)] == do {
			enabled = true
		} else if window == dont {
			enabled = false
		}
		cursor++
	}
	fmt.Printf("Day 0: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_03.txt")
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
