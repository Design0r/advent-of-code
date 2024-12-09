package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
	"time"
)

type Data struct {
	Disk    []*int
	FileMap map[int]int
}

func parse(path string) *Data {
	file, err := os.ReadFile(path)
	if err != nil {
		log.Fatalf("Error reading file %v", err)
	}
	stripped := strings.TrimSpace(string(file))

	disk := []*int{}
	counter := 0
	fileMap := map[int]int{}
	for i := 0; i <= len(stripped); i += 2 {
		fileSize, err := strconv.Atoi(string(stripped[i]))
		if err != nil {
			log.Fatalf("failed to parse to int: %v", err)
		}
		idx := counter
		for range fileSize {
			disk = append(disk, &idx)
		}
		fileMap[idx] = fileSize
		counter++

		if i >= len(stripped)-1 {
			break
		}

		emptySpace, err := strconv.Atoi(string(stripped[i+1]))
		if err != nil {
			log.Fatalf("failed to parse to int: %v", err)
		}
		for range emptySpace {
			disk = append(disk, nil)
		}
	}

	return &Data{Disk: disk, FileMap: fileMap}
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

	for i, val := range disk {
		if val == nil {
			break
		}
		result += i * *val
	}

	fmt.Printf("Day 09: Part 1: %v\n", result)
}

func findEmptySpace(disk []*int, size int) (int, error) {
	i := 0
	for i < len(disk) {
		if disk[i] != nil {
			i++
			continue
		}

		sizeCount := 0
		for sizeCount < size {
			if disk[i+sizeCount] != nil || i+sizeCount >= len(disk)-1 {
				break
			}
			sizeCount++
		}

		if sizeCount == size {
			return i, nil
		}
		i++
	}

	return 0, fmt.Errorf("No empty space found")
}

func deleteFile(fileId int, size int, disk []*int) {
	for i := len(disk) - 1; i >= 0; i-- {
		val := disk[i]
		if val == nil {
			continue
		}

		if *val == fileId {
			for j := 0; j < size; j++ {
				if i-j < 0 {
					return
				}
				disk[i-j] = nil
			}
		}

	}
}

func insertFile(idx int, fileID int, fileSize int, disk []*int) {
	for j := idx; j < idx+fileSize; j++ {
		disk[j] = &fileID
	}
}

func findFileIdx(disk []*int, fileId int) (int, error) {
	for i, v := range disk {
		if v != nil && *v == fileId {
			return i, nil
		}
	}

	return 0, errors.New("File not found")
}

func part2(data *Data) {
	result := 0

	disk := data.Disk
	for i := len(data.FileMap) - 1; i >= 0; i-- {
		fileSize := data.FileMap[i]
		emptySpaceIdx, err := findEmptySpace(disk, fileSize)
		if err != nil {
			continue
		}

		fileId, err := findFileIdx(disk, i)
		if err != nil {
			continue
		}

		if emptySpaceIdx >= fileId {
			continue
		}

		deleteFile(i, fileSize, disk)
		insertFile(emptySpaceIdx, i, fileSize, disk)
	}

	for i, val := range disk {
		if val == nil {
			continue
		}
		result += i * *val
	}

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
