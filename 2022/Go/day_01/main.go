package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func checkErr(err error) {
	if err != nil {
		fmt.Printf("error %v", err)
	}
}

func sum(list []int) int {
	res := 0
	for _, v := range list {
		res += v
	}
	return res
}

func max(num1 int, num2 int) int {
	if num1 > num2 {
		return num1
	} else {
		return num2
	}
}

func main() {
	val, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Printf("error reading file: %v", err)
	}

	str := strings.Split(string(val), "\n")

	currentCount := 0
	var bagpack []int

	for _, v := range str {
		if v == "" {
			bagpack = append(bagpack, currentCount)
			currentCount = 0
			continue
		}

		num, err := strconv.Atoi(v)
		checkErr(err)
		currentCount += num
	}

	slices.Sort(bagpack)
	fmt.Printf("Part 1: %v\n", bagpack[len(bagpack)-1])
	fmt.Printf("Part 2: %v\n", sum(bagpack[len(bagpack)-3:]))
}
