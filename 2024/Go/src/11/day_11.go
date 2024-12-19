package main

import (
	"container/list"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

type Data struct {
	Stones *list.List
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	fields := strings.Fields(stripped)

	ll := list.New()
	for _, strNum := range fields {
		num, err := strconv.Atoi(strNum)
		if err != nil {
			continue
		}
		ll.PushBack(num)
	}

	return &Data{Stones: ll}
}

func clone(original *list.List) *list.List {
	duplicate := list.New()

	for e := original.Front(); e != nil; e = e.Next() {
		duplicate.PushBack(e.Value)
	}

	return duplicate
}

func split(value string) (int, int, error) {
	left := value[:(len(value) / 2)]
	right := value[(len(value) / 2):]

	numLeft, err := strconv.Atoi(left)
	if err != nil {
		return 0, 0, err
	}
	numRight, err := strconv.Atoi(right)
	if err != nil {
		return 0, 0, err
	}

	return numLeft, numRight, nil
}

func printList(l *list.List) {
	for i := l.Front(); i != nil; i = i.Next() {
		fmt.Printf("%v, ", i.Value)
	}
	fmt.Println()
}

func blink(stones *list.List, count int) {
	for range count {
		// printList(data.Stones)
		for curr := stones.Front(); curr != nil; curr = curr.Next() {
			num := curr.Value.(int)
			digits := strconv.Itoa(num)

			if num == 0 {
				curr.Value = 1
			} else if len(digits)%2 == 0 {
				l, r, err := split(digits)
				if err != nil {
					continue
				}
				curr.Value = r
				stones.InsertBefore(l, curr)
			} else {
				curr.Value = num * 2024
			}
		}
	}
}

func recBlink(stone int, times int) int {
	cache := make(map[[2]int]int)
	var helper func(int, int) int
	helper = func(stone, times int) int {
		key := [2]int{stone, times}
		if val, ok := cache[key]; ok {
			return val
		}
		if times == 0 {
			return 1
		}
		result := 0
		if stone == 0 {
			result = helper(1, times-1)
		} else {
			strStone := strconv.Itoa(stone)
			if len(strStone)%2 == 0 {
				l, r, _ := split(strStone)
				result = helper(l, times-1) + helper(r, times-1)
			} else {
				result = helper(stone*2024, times-1)
			}
		}
		cache[key] = result
		return result
	}
	return helper(stone, times)
}

func part1(data *Data) {
	stones := clone(data.Stones)
	blink(stones, 25)
	result := stones.Len()

	fmt.Printf("Day 11: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	for curr := data.Stones.Front(); curr != nil; curr = curr.Next() {
		stone := curr.Value.(int)
		result += recBlink(stone, 75)

	}
	fmt.Printf("Day 11: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_11.txt")
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
