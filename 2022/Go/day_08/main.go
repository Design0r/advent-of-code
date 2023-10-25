package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

type Tree struct {
	height   int
	position [2]int
}

func NewTree(height int, position [2]int) Tree {
	return Tree{height, position}
}

type Forest struct {
	trees  []Tree
	width  int
	height int
}

func NewForest() *Forest {
	return &Forest{}
}

func (f *Forest) AddTree(tree Tree) {
	f.trees = append(f.trees, tree)
}

func (f *Forest) GetTrees() []Tree {
	return f.trees
}

func (f *Forest) GetInsideTrees() []Tree {
	insideTrees := make([]Tree, 0)

	for _, t := range f.GetTrees() {
		if 0 < t.position[0] && t.position[0] < f.height &&
			0 < t.position[1] && t.position[1] < f.width {
			insideTrees = append(insideTrees, t)
		}
	}

	return insideTrees
}

func (f *Forest) SetDimensions(width, height int) {
	f.width = width
	f.height = height
}

func (f *Forest) CheckVisibility(tree Tree) bool {
	var loop func([]Tree) bool
	loop = func(array []Tree) bool {
		visibility := false

		for _, t := range array {
			if tree.height > t.height {
				visibility = true
			} else {
				visibility = false
				break
			}
		}

		return visibility
	}

	treePos := tree.position
	horizontalList := make([]Tree, 0)
	verticalList := make([]Tree, 0)

	for _, t := range f.GetTrees() {
		if t.position[0] == treePos[0] {
			horizontalList = append(horizontalList, t)
		}
		if t.position[1] == treePos[1] {
			verticalList = append(verticalList, t)
		}
	}

	horizontalLeft := horizontalList[:treePos[1]]
	horizontalRight := horizontalList[treePos[1]+1:]
	verticalTop := verticalList[:treePos[0]]
	verticalBottom := verticalList[treePos[0]+1:]

	return loop(horizontalLeft) || loop(horizontalRight) ||
		loop(verticalTop) || loop(verticalBottom)
}

func (f *Forest) CheckScene(tree Tree) int {
	var loop func([]Tree) int
	loop = func(array []Tree) int {
		sceneScore := 0

		for idx, t := range array {
			sceneScore = idx + 1
			if t.height >= tree.height {
				break
			}
		}

		return sceneScore
	}

	treePos := tree.position
	horizontalList := make([]Tree, 0)
	verticalList := make([]Tree, 0)

	for _, t := range f.GetTrees() {
		if t.position[0] == treePos[0] {
			horizontalList = append(horizontalList, t)
		}
		if t.position[1] == treePos[1] {
			verticalList = append(verticalList, t)
		}
	}

	horizontalLeft := reverse(horizontalList[:treePos[1]])
	horizontalRight := horizontalList[treePos[1]+1:]
	verticalTop := reverse(verticalList[:treePos[0]])
	verticalBottom := verticalList[treePos[0]+1:]

	return loop(horizontalRight) * loop(horizontalLeft) *
		loop(verticalTop) * loop(verticalBottom)
}

func reverse(slice []Tree) []Tree {
	for i, j := 0, len(slice)-1; i < j; i, j = i+1, j-1 {
		slice[i], slice[j] = slice[j], slice[i]
	}
	return slice
}

func main() {
	start := time.Now()

	// Create a new forest
	forest := NewForest()

	// Read input from file
	input, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	inputLines := strings.Split(string(input), "\n")
	forest.SetDimensions(len(inputLines)-1, len(inputLines[0])-1)

	for rowIdx, line := range inputLines {
		for columnIdx, heightStr := range line {
			height := int(heightStr - '0') // Convert rune to int
			forest.AddTree(NewTree(height, [2]int{rowIdx, columnIdx}))
		}
	}

	insideTrees := forest.GetInsideTrees()

	visibilityCount := 0
	for _, tree := range insideTrees {
		if forest.CheckVisibility(tree) {
			visibilityCount++
		}
	}

	maxSceneScore := 0
	for _, tree := range insideTrees {
		score := forest.CheckScene(tree)
		if score > maxSceneScore {
			maxSceneScore = score
		}
	}

	fmt.Printf(
		"Number of visible Trees: %d found in %s\n",
		visibilityCount+(2*forest.width)+(2*forest.height),
		time.Since(start),
	)
	fmt.Printf("The highest scenic score is: %d found in %s\n", maxSceneScore, time.Since(start))
}
