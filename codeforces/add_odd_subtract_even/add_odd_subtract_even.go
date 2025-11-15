package main

import "fmt"

func main() {
	var t int
	fmt.Scanln(&t)

	var a, b int
	for t > 0 {
		t = t - 1
		fmt.Scanln(&a, &b)

		if a == b {
			fmt.Println("0")
			continue
		}

		if a < b {
			if isEven(a) {
				if isEven(b) {
					fmt.Println("2")
					continue
				} else { // b is odd
					fmt.Println("1")
					continue
				}
			} else { // a is odd
				if isEven(b) {
					fmt.Println("1")
					continue
				} else { // b is odd
					fmt.Println("2")
					continue
				}
			}
		} else { // a > b
			if (isEven(a) && isEven(b)) || (!isEven(a) && !isEven(b)) {
				fmt.Println("1")
				continue
			} else { // a and b have different parity
				fmt.Println("2")
				continue
			}
		}
	}
}

func isEven(num int) bool {
	return num%2 == 0
}

// case a < b
// 2 4 = 2 (+(b-a) and +1)
// 2 5 = 1 (+(b-a))
// 1 3 = 2 (+1 and then we are in the case above)
// 1 4 = 1 (+(b-a))
//
// case a > b
// 4 2 = 1 (-(a-b))
// 5 2 = 2 (-1 before b, and then +1)
// 3 1 = 1 (-(a-b))
// 4 1 = 2 (-1 before b, and then +1)
