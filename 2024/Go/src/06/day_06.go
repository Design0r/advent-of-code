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
	Grid  Grid
	Start Point
	Dir   Point
}

var rotate map[Point]Point = map[Point]Point{
	{0, -1}: {1, 0},
	{1, 0}:  {0, 1},
	{0, 1}:  {-1, 0},
	{-1, 0}: {0, -1},
}
var	dirMap map[string]Point = map[string]Point{"^": {0, -1}, ">": {1, 0}, "v": {0, 1}, "<": {-1, 0}}

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

	return &Data{grid, startPoint, startDir}
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

func walk(pos Point, dir Point, grid Grid, visited map[Point]Point) int {
	visited[pos] = dir
	// printGrid(grid, visited)

	nextPos := Point{pos.X + dir.X, pos.Y + dir.Y}
	if nextPos.X < 0 || nextPos.X >= len(grid[0]) || nextPos.Y < 0 || nextPos.Y >= len(grid) {
		return len(visited)
	}

	if grid[nextPos.Y][nextPos.X] == "#" {
		nextDir := rotate[dir]
		nextPos = Point{pos.X + nextDir.X, pos.Y + nextDir.Y}
		return walk(nextPos, nextDir, grid, visited)
	}

	return walk(nextPos, dir, grid, visited)
}

func isLooping(pos Point, dir Point, grid Grid, visited map[Point]Point, newObstacle Point) bool {
	visited[pos] = dir
	// printGrid(grid, visited)

	if _, exists := visited[pos]; exists {
		return true
	}

	nextPos := Point{pos.X + dir.X, pos.Y + dir.Y}
	if nextPos.X < 0 || nextPos.X >= len(grid[0]) || nextPos.Y < 0 || nextPos.Y >= len(grid) {
		return false
	}

	if grid[nextPos.Y][nextPos.X] == "#" ||
		(nextPos.X == newObstacle.X) && (nextPos.Y == newObstacle.Y) {
		nextDir := rotate[dir]
		nextPos = Point{pos.X + nextDir.X, pos.Y + nextDir.Y}
		return isLooping(nextPos, nextDir, grid, visited, newObstacle)
	}

	return isLooping(nextPos, dir, grid, visited, newObstacle)
}

func isValidObstacle(grid Grid, point Point) bool{
    if data.Grid[point.Y][point.X] == "#"{
    return false
  } 
  if data.Grid[point.Y][point.X] == ""
}

func part1(data *Data) {
	result := 0
	visited := map[Point]Point{}
	result = walk(data.Start, data.Dir, data.Grid, visited)

	fmt.Printf("Day 06: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	visited := map[Point]Point{}
	for y, row := range data.Grid {
		for x := range row {
			if isLooping(data.Start, data.Dir, data.Grid, visited, Point{x, y}) {
			}
		}
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
