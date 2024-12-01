package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

func getNum(line string) (int, error) {
	var left, right string
	for i := 0; i < len(line); i++ {
		for _, char := range line {
			if char >= '0' && char <= '9' {
				left = string(char)
				break
			}
		}

		for i := len(line) - 1; i >= 0; i-- {
			char := line[i]
			if char >= '0' && char <= '9' {
				right = string(char)
				break
			}
		}

	}

	if left == "" || right == "" {
		return 0, errors.New("Failed to find number")
	}

	strNum := strings.Join([]string{left, right}, "")
	num, err := strconv.Atoi(strNum)
	if err != nil {
		log.Fatal(err)
	}

	return num, nil
}

func parse(path string) *[]string {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	return &lines
}

func part1(lines *[]string) {
	result := 0

	for _, line := range *lines {
		num, err := getNum(line)
		if err != nil {
			log.Printf("Error: %v", err)
		}
		result += num
	}

	fmt.Printf("Day 1, Part 1: %d\n", result)
}

func part2(lines *[]string) {
}

func main() {
	startTime := time.Now()
	lines := parse("inputs/day_01.txt")
	fmt.Printf("Finished parsing in %v\n", time.Since(startTime))
	part1(lines)
	fmt.Printf("Finished part 1 in %v\n", time.Since(startTime))
	part2(lines)
	fmt.Printf("Finished part 2 in %v\n", time.Since(startTime))
}
