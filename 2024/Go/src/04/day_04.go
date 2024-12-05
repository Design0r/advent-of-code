package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"time"
)

var DIRECTIONS []Point = []Point{
	NewPoint(1, 0),
	NewPoint(-1, 0),
	NewPoint(0, 1),
	NewPoint(0, -1),
	NewPoint(1, 1),
	NewPoint(-1, -1),
	NewPoint(-1, 1),
	NewPoint(1, -1),
}

type Point struct {
	X, Y int
}

func NewPoint(x int, y int) Point {
	return Point{X: x, Y: y}
}

type Data struct {
	Lines []string
	XPos  []Point
	APos  []Point
	Grid  map[Point]rune
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	xPos := []Point{}
	aPos := []Point{}
	grid := map[Point]rune{}

	for row, line := range lines {
		for col, char := range line {
			pos := NewPoint(col, row)
			grid[pos] = char
			if char == 'X' {
				xPos = append(xPos, pos)
			} else if char == 'A' {
				aPos = append(aPos, pos)
			}
		}
	}

	return &Data{Lines: lines, XPos: xPos, APos: aPos, Grid: grid}
}

func getWord(grid map[Point]rune, start Point, dir Point, count int) string {
	word := []rune{}
	for i := range count {
		pos := NewPoint(start.X+(dir.X*i), start.Y+(dir.Y*i))
		if char, exists := grid[pos]; exists {
			word = append(word, char)
		}
	}

	return string(word)
}

func checkMasX(grid map[Point]rune, start Point) bool {
	topLeft := NewPoint(start.X-1, start.Y-1)
	dir := NewPoint(1, 1)
	word := getWord(grid, topLeft, dir, 3)
	if word != "MAS" && word != "SAM" {
		return false
	}

	bottomLeft := NewPoint(start.X-1, start.Y+1)
	dir = NewPoint(1, -1)
	word = getWord(grid, bottomLeft, dir, 3)
	if word != "MAS" && word != "SAM" {
		return false
	}

	return true
}

func part1(data *Data) {
	result := 0

	for _, pos := range data.XPos {
		for _, dir := range DIRECTIONS {
			if getWord(data.Grid, pos, dir, 4) == "XMAS" {
				result++
			}
		}
	}
	fmt.Printf("Day 04: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0
	for _, pos := range data.APos {
		if checkMasX(data.Grid, pos) {
			result++
		}
	}
	fmt.Printf("Day 04: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_04.txt")
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
