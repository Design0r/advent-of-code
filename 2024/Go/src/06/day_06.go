package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strings"
	"time"
)

type Grid = [][]string

type Point struct {
	X int
	Y int
}

type Data struct {
	Grid    Grid
	Start   Point
	Dir     Point
	visited *map[Point]Point
}

var rotate map[Point]Point = map[Point]Point{
	{0, -1}: {1, 0},
	{1, 0}:  {0, 1},
	{0, 1}:  {-1, 0},
	{-1, 0}: {0, -1},
}

var dirMap map[string]Point = map[string]Point{"^": {0, -1}, ">": {1, 0}, "v": {0, 1}, "<": {-1, 0}}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	startDir := Point{}
	startPoint := Point{}
	grid := Grid{}
	for y, line := range lines {
		grid = append(grid, strings.Split(line, ""))
		for dir, point := range dirMap {
			if x := strings.Index(line, dir); x != -1 {
				startPoint = Point{x, y}
				startDir = point
			}
		}
	}

	return &Data{grid, startPoint, startDir, nil}
}

func printGrid(grid Grid, visited map[Point]Point) {
	for y, line := range grid {
		newLine := slices.Clone(line)
		for x := range line {
			if _, exists := visited[Point{x, y}]; exists {
				newLine[x] = "X"
			}
		}
		fmt.Println(newLine)
	}
	fmt.Println("====================================================")
}

func walk(pos Point, dir Point, grid Grid, visited map[Point]Point, part2 bool) bool {
	if part2 {
		if visited[pos] == dir {
			return true
		}
	}
	visited[pos] = dir
	// printGrid(grid, visited)

	nextPos := Point{pos.X + dir.X, pos.Y + dir.Y}
	if nextPos.X < 0 || nextPos.X >= len(grid[0]) || nextPos.Y < 0 || nextPos.Y >= len(grid) {
		return false
	}

	if grid[nextPos.Y][nextPos.X] == "#" || grid[nextPos.Y][nextPos.X] == "O" {
		nextDir := dir
		for i := 0; i < 4; i++ {
			nextDir = rotate[nextDir]
			newPos := Point{pos.X + nextDir.X, pos.Y + nextDir.Y}

			if newPos.X < 0 || newPos.X >= len(grid[0]) || newPos.Y < 0 || newPos.Y >= len(grid) {
				continue
			}

			if grid[newPos.Y][newPos.X] != "#" && grid[newPos.Y][newPos.X] != "O" {
				return walk(newPos, nextDir, grid, visited, part2)
			}
		}
		return false
	}

	return walk(nextPos, dir, grid, visited, part2)
}

func part1(data *Data) {
	result := 0
	visited := map[Point]Point{}
	walk(data.Start, data.Dir, data.Grid, visited, false)
	result = len(visited)
	data.visited = &visited

	fmt.Printf("Day 06: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	for pos := range *data.visited {
		value := data.Grid[pos.Y][pos.X]
		data.Grid[pos.Y][pos.X] = "O"
		visited := map[Point]Point{}
		if walk(data.Start, data.Dir, data.Grid, visited, true) {
			result += 1
		}
		data.Grid[pos.Y][pos.X] = value
	}
	fmt.Printf("Day 06: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_06.txt")
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
