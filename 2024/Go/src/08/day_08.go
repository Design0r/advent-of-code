package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"time"
)

type Point struct {
	X, Y int
}

type Data struct {
	Lines    []string
	Antennas map[rune][]Point
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))
	lines := strings.Split(stripped, "\n")

	antennas := map[rune][]Point{}
	for y, row := range lines {
		for x, col := range row {
			if col == '.' {
				continue
			}
			antennas[col] = append(antennas[col], Point{x, y})
		}
	}

	return &Data{lines, antennas}
}

func detectAntinodes(grid []string, points []Point, antinodes map[Point]struct{}) {
	for _, i := range points {
		for _, j := range points {
			if j.X == i.X && j.Y == i.Y {
				continue
			}
			antinode := Point{i.X + i.X - j.X, i.Y + i.Y - j.Y}
			if antinode.Y < 0 || antinode.Y >= len(grid) || antinode.X < 0 ||
				antinode.X >= len(grid[0]) {
				continue
			}
			_, exists := antinodes[antinode]
			if exists {
				continue
			}
			antinodes[antinode] = struct{}{}
		}
	}
}

func detectAntinodes2(grid []string, points []Point, antinodes map[Point]struct{}) {
	for _, i := range points {
		for _, j := range points {
			if j.X == i.X && j.Y == i.Y {
				antinodes[i] = struct{}{}
				continue
			}
			u := i
			v := j
			for {
				antinode := Point{u.X + u.X - v.X, u.Y + u.Y - v.Y}
				if antinode.Y < 0 || antinode.Y >= len(grid) || antinode.X < 0 ||
					antinode.X >= len(grid[0]) {
					break
				}
				if _, exists := antinodes[antinode]; !exists {
					antinodes[antinode] = struct{}{}
				}
				v = u
				u = antinode
			}
		}
	}
}

func printGrid(grid []string, antinodes map[Point]struct{}) {
	for y, row := range grid {
		for x, col := range row {
			p := Point{x, y}
			if _, exists := antinodes[p]; exists {
				fmt.Print("#")
			} else {
				fmt.Print(string(col))
			}
		}
		fmt.Println()
	}
}

func part1(data *Data) {
	result := 0

	antinodes := map[Point]struct{}{}
	for _, points := range data.Antennas {
		detectAntinodes(data.Lines, points, antinodes)
	}
	result = len(antinodes)

	fmt.Printf("Day 08: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0

	antinodes := map[Point]struct{}{}
	for _, points := range data.Antennas {
		detectAntinodes2(data.Lines, points, antinodes)
	}
	result = len(antinodes)
	// printGrid(data.Lines, antinodes)

	fmt.Printf("Day 08: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_08.txt")
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
