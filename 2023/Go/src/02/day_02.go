package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"time"
)

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
	fmt.Printf("Day 0: Part 1: %v\n", result)
}

func part2(lines *[]string) {
	result := 0
	fmt.Printf("Day 0: Part 2: %v\n", result)
}

func main() {
	startTime := time.Now()
	lines := parse("inputs/day_02.txt")
	fmt.Printf("Finished parsing in %v\n", time.Since(startTime))
	part1(lines)
	fmt.Printf("Finished Part 1 in %v\n", time.Since(startTime))
	part2(lines)
	fmt.Printf("Finished Part 2 in %v\n", time.Since(startTime))
}
