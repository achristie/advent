package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, err := os.OpenFile("./input.txt", os.O_RDONLY, 0644)
	if err != nil {
		fmt.Println(err)
	}

	scanner := bufio.NewScanner(f)
	var total, total2 = 0, 0
	for scanner.Scan() {
		text := scanner.Text()
		slice := strings.Split(text, " ")
		total += calcScore(slice[0], slice[1])
		total2 += calcScore2(slice[0], slice[1])
	}
	fmt.Printf("Total Score: %d\n", total)
	fmt.Printf("Total Score pt2: %d\n", total2)
}

func calcScore(x, y string) int {
	switch y {
	case "X":
		switch x {
		case "A":
			return 4 // draw + 1
		case "B":
			return 1 // loss + 1
		case "C":
			return 7 // win + 1
		}
	case "Y":
		switch x {
		case "A":
			return 8 // win + 2
		case "B":
			return 5 // draw + 2
		case "C":
			return 2 // loss + 2
		}
	case "Z":
		switch x {
		case "A":
			return 3 // loss + 3
		case "B":
			return 9 // win + 3
		case "C":
			return 6 // draw + 3
		}
	}
	fmt.Println("error. no matches")
	return 0
}

func calcScore2(x, y string) int {
	switch x {
	case "A":
		switch y {
		case "X":
			return 3 // loss + 3
		case "Y":
			return 4 // draw + 1
		case "Z":
			return 8 // win + 2
		}
	case "B":
		switch y {
		case "X":
			return 1 // loss + 1
		case "Y":
			return 5 // draw + 2
		case "Z":
			return 9 // win + 3
		}
	case "C":
		switch y {
		case "X":
			return 2 // loss + 2
		case "Y":
			return 6 // draw + 3
		case "Z":
			return 7 // win + 1
		}
	}
	fmt.Println("error. no matches")
	return 0
}
