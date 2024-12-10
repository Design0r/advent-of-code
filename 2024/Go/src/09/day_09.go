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
	Disk       []*int
	FileMap    map[int]File
	EmptySpace []*Empty
}

type File struct {
	ID, Index, Size int
}

type Empty struct {
	Index, Size int
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))

	disk := []*int{}
	counter := 0
	fileMap := map[int]File{}
	emptyMap := []*Empty{}
	for i := 0; i <= len(stripped); i += 2 {
		fileSize, err := strconv.Atoi(string(stripped[i]))
		if err != nil {
			log.Fatalf("failed to parse to int: %v", err)
		}
		idx := counter
		fileMap[idx] = File{ID: idx, Index: len(disk), Size: fileSize}
		for range fileSize {
			disk = append(disk, &idx)
		}
		counter++

		if i >= len(stripped)-1 {
			break
		}

		emptySpace, err := strconv.Atoi(string(stripped[i+1]))
		if err != nil {
			log.Fatalf("failed to parse to int: %v", err)
		}
		emptyMap = append(emptyMap, &Empty{Index: len(disk), Size: emptySpace})
		for range emptySpace {
			disk = append(disk, nil)
		}

	}

	return &Data{Disk: disk, FileMap: fileMap, EmptySpace: emptyMap}
}

func printDisk(disk []*int) {
	for _, val := range disk {
		if val == nil {
			fmt.Print(". ")
			continue
		}
		fmt.Printf("%v ", *val)
	}

	fmt.Println()
}

func checksum(disk []*int) int {
	result := 0
	for i, val := range disk {
		if val == nil {
			continue
		}
		result += i * *val
	}

	return result
}

func findEmptySpace(emptySpace []*Empty, size int) (int, error) {
	for i := 0; i < len(emptySpace); i++ {
		space := emptySpace[i]
		if space == nil || space.Size < size {
			continue
		}

		idx := space.Index
		sizeDiff := space.Size - size
		if sizeDiff > 0 {
			emptySpace[i] = &Empty{space.Index + size, sizeDiff}
		} else {
			emptySpace[i] = nil
		}

		return idx, nil
	}

	return 0, fmt.Errorf("No empty space found")
}

func deleteFile(file File, disk []*int) {
	for i := file.Index; i < file.Index+file.Size; i++ {
		disk[i] = nil
	}
}

func insertFile(idx int, file File, disk []*int) {
	for j := idx; j < idx+file.Size; j++ {
		disk[j] = &file.ID
	}
}

func part1(data *Data) {
	result := 0

	disk := slices.Clone(data.Disk)
	reverseCounter := len(disk) - 1
	counter := 0
	for {
		if reverseCounter <= counter {
			break
		}
		val := disk[counter]
		if val != nil {
			counter++
			continue
		}
		reverseVal := disk[reverseCounter]
		if reverseVal == nil {
			reverseCounter--
			continue
		}

		disk[counter] = reverseVal
		disk = disk[:reverseCounter]
		reverseCounter--
		counter++
	}

	result = checksum(disk)

	fmt.Printf("Day 09: Part 1: %v\n", result)
}

func part2(data *Data) {
	result := 0

	for i := len(data.FileMap) - 1; i >= 0; i-- {
		file := data.FileMap[i]
		emptySpaceIdx, err := findEmptySpace(data.EmptySpace, file.Size)
		if err != nil || emptySpaceIdx >= file.Index {
			continue
		}

		deleteFile(file, data.Disk)
		insertFile(emptySpaceIdx, file, data.Disk)
	}

	result = checksum(data.Disk)

	fmt.Printf("Day 09: Part 2: %v\n", result)
}

func main() {
	fmt.Printf("------------------------------------\n")
	startTime := time.Now()
	lines := parse("inputs/day_09.txt")
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
