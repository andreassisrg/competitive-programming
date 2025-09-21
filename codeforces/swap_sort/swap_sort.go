package main

import (
    "bufio"
    "fmt"
    "os"
)

type swap struct { i, j int }

func main() {
    var n int
    fmt.Scan(&n)

    numbers := make([]int, 0, n)

    scanner := bufio.NewScanner(os.Stdin)
    scanner.Split(bufio.ScanWords)

    for i := 0; i < n; i++ {
        scanner.Scan()
        var x int
        fmt.Sscan(scanner.Text(), &x)
        numbers = append(numbers, x)
    }
    
    swap_num := 0
    swaps := []swap{}
    for i, num := range numbers {
        min_i := i
        min := num
        for j := i; j < len(numbers); j++ {
            if numbers[j] < min {
                min = numbers[j]
                min_i = j
            }
        }

        if i != min_i {
            numbers[i], numbers[min_i] = numbers[min_i], numbers[i]
            swap_num++
            swaps = append(swaps, swap{i, min_i})
        }
    }

    fmt.Println(swap_num)
    for _, s := range swaps {
        fmt.Println(s.i, s.j)
    }
}
