package aoc

import (
	"log"
)

func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func Assert(expr bool, message string) {
	if !expr {
		log.Fatal(message)
	}
}
