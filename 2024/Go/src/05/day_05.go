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

type Data struct {
	Rules   []Rule
	Updates [][]string
}

type Rule struct {
	First  string
	Second string
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	input := strings.Split(stripped, "\n\n")
	rules := strings.Split(input[0], "\n")
	updates := strings.Split(input[1], "\n")

	ruleSet := []Rule{}
	updateSet := [][]string{}

	for _, rule := range rules {
		s := strings.Split(rule, "|")
		ruleSet = append(ruleSet, Rule{s[0], s[1]})
	}

	for _, update := range updates {
		updateSet = append(updateSet, strings.Split(update, ","))
	}

	return &Data{ruleSet, updateSet}
}

func isValidUpdate(updateSet []string, rules []Rule) bool {
	return slices.IsSortedFunc(updateSet, func(a string, b string) int {
		for _, rule := range rules {
			if a == rule.Second && b == rule.First {
				return 1
			}
		}
		return -1
	})
}

func getMiddle(input []string) int {
	middle := input[(len(input) / 2)]
	if num, err := strconv.Atoi(middle); err == nil {
		return num
	}

	return 0
}

func orderUpdates(updates *[]string, rules []Rule) {
	slices.SortFunc(*updates, func(a string, b string) int {
		for _, rule := range rules {
			if a == rule.Second && b == rule.First {
				return -1
			}
		}
		return 1
	})
}

func part1(data *Data) {
	result := 0

	for _, updateSet := range data.Updates {
		if isValidUpdate(updateSet, data.Rules) {
			result += getMiddle(updateSet)
		}
	}

	fmt.Printf("Day 05: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	for _, updateSet := range data.Updates {
		if isValidUpdate(updateSet, data.Rules) {
			continue
		}
		orderUpdates(&updateSet, data.Rules)
		result += getMiddle(updateSet)

	}
	fmt.Printf("Day 05: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_05.txt")
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
