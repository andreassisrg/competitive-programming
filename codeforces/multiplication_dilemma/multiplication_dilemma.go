package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	var t int
	fmt.Scan(&t)

	var a, b int
	for i := 0; i < t; i++ {
		fmt.Scanln(&a, &b)
		aDecomposed, bDecomposed := decompose(a), decompose(b)

		var printLst []string
		for i, aDigit := range aDecomposed {
			if aDigit == 0 {
				continue
			}

			for j, bDigit := range bDecomposed {
				if bDigit == 0 {
					continue
				}

				printLst = append(printLst,
					fmt.Sprintf(
						"%d x %d",
						aDigit*int(math.Pow(10, float64(i))),
						bDigit*int(math.Pow(10, float64(j))),
					),
				)
			}
		}

		fmt.Println(strings.Join(printLst, " + "))
	}
}

func decompose(num int) []int {
	var numDecomposed []int

	for math.Abs(float64(num)) > 0 {
		numDecomposed = append(numDecomposed, num%10)
		num /= 10
	}

	return numDecomposed
}
