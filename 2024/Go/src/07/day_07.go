package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
	"time"
)

type Data struct {
	Equations []Equation
}

type Combi struct {
	Length  int
	Symbols []string
}

type Equation struct {
	Result  int
	Numbers []int
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	eq := make([]Equation, len(lines))
	for i, line := range lines {
		split := strings.Split(line, ":")
		result, err := strconv.Atoi(split[0])
		if err != nil {
			log.Fatalf("Failed to parse to int: %v", err)
		}

		n := strings.Fields(split[1])
		nums := make([]int, len(n))
		for j, strNum := range n {
			num, err := strconv.Atoi(strNum)
			if err != nil {
				log.Fatalf("Failed to parse to int: %v", err)
			}
			nums[j] = num
		}

		eq[i] = Equation{result, nums}
	}

	return &Data{eq}
}

func combinations(symbols []string, length int, cache map[int][][]string) [][]string {
	if val, exists := cache[length]; exists {
		return val
	}

	s := len(symbols)
	if s == 0 || length < 1 {
		return nil
	}

	total := 1
	for i := 0; i < length; i++ {
		total *= s
	}

	result := make([][]string, total)

	for i := 0; i < total; i++ {
		combo := make([]string, length)
		x := i
		for pos := length - 1; pos >= 0; pos-- {
			combo[pos] = symbols[x%s]
			x /= s
		}
		result[i] = combo
	}
	cache[length] = result

	return result
}

func testCombi(c []string, nums []int, target int) bool {
	res := nums[0]
	for i := 1; i < len(nums); i++ {
		op := c[i-1]
		num := nums[i]
		if res > target {
			return false
		}

		switch op {
		case "+":
			res += num
		case "*":
			res *= num
		case "||":
			res = res*int(math.Pow10(numDigits(num))) + num
		default:
			return false
		}
	}
	return res == target
}

func numDigits(n int) int {
	if n == 0 {
		return 1
	}
	digits := 0
	for n > 0 {
		n /= 10
		digits++
	}
	return digits
}

func part1(data *Data) {
	result := 0
	cache := map[int][][]string{}
	symbols := []string{"+", "*"}
	for _, eq := range data.Equations {
		perm := combinations(symbols, len(eq.Numbers)-1, cache)
		for _, p := range perm {
			if testCombi(p, eq.Numbers, eq.Result) {
				result += eq.Result
				break
			}
		}
	}

	fmt.Printf("Day 07: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	cache := map[int][][]string{}
	symbols := []string{"+", "*", "||"}
	for _, eq := range data.Equations {
		perm := combinations(symbols, len(eq.Numbers)-1, cache)
		for _, p := range perm {
			if testCombi(p, eq.Numbers, eq.Result) {
				result += eq.Result
				break
			}
		}
	}
	fmt.Printf("Day 07: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_07.txt")
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
