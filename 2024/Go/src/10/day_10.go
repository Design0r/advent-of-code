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
	Grid     Grid
	StartPos map[Point]struct{}
}

type Grid = [][]int

type Point struct {
	Y, X int
}

var DIRS []Point = []Point{
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1},
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	grid := [][]int{}
	startPos := make(map[Point]struct{})
	for y, row := range lines {
		temp := []int{}
		for x, col := range row {
			num, err := strconv.Atoi(string(col))
			if err != nil {
				continue
			}
			temp = append(temp, num)
			if num == 0 {
				startPos[Point{y, x}] = struct{}{}
			}
		}
		grid = append(grid, temp)
	}

	return &Data{Grid: grid, StartPos: startPos}
}

func score(pos Point, grid Grid) (int, int) {
	foundNines := 0
	completed := make(map[Point]struct{})
	todo := []Point{pos}

	for len(todo) > 0 {
		pt := todo[len(todo)-1]
		todo = todo[:len(todo)-1]
		value := grid[pt.Y][pt.X]

		if value == 9 {
			completed[pt] = struct{}{}
			foundNines++
			continue
		}

		for _, dir := range DIRS {
			next := Point{pt.Y + dir.Y, pt.X + dir.X}
			if next.Y < 0 || next.Y >= len(grid) || next.X < 0 || next.X >= len(grid[0]) {
				continue
			}
			if grid[next.Y][next.X] == value+1 {
				todo = append(todo, next)
			}
		}
	}

	return len(completed), foundNines
}

func part1(data *Data) {
	result := 0

	for start := range data.StartPos {
		r, _ := score(start, data.Grid)
		result += r
	}

	fmt.Printf("Day 10: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0

	for start := range data.StartPos {
		_, r := score(start, data.Grid)
		result += r
	}
	fmt.Printf("Day 10: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_10.txt")
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
