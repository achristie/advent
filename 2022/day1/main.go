package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	f, err := os.OpenFile("./input.txt", os.O_RDONLY, 0644)
	if err != nil {
		fmt.Println(err)
	}

	total := make(map[int]int)
	var count = 0
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		value := scanner.Text()
		if value == "" {
			count += 1
			continue
		}
		number, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println(err)
		}
		total[count] += number
	}
	var ranked []int
	for _, v := range total {
		ranked = append(ranked, v)
	}

	sort.Slice(ranked, func(i, j int) bool {
		return ranked[i] >= ranked[j]
	})

	fmt.Printf("Largest Calorie Count: %d\n", ranked[0])
	var sum int
	for _, j := range ranked[:3] {
		sum += j
	}
	fmt.Printf("Top 3 Calorie Count %d\n", sum)

}
