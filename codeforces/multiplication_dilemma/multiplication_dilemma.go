package main

import (
    "fmt"
    "strings"
)

func main() {
    var t int
    fmt.Scan(&t)

    for i := 0; i < t; i++ {
        var a, b int
        fmt.Scanln(&a, &b)
    
        a_decomposition, b_decomposition := getDecomposition(a), getDecomposition(b)
        
        var terms []string
        for i, _ := range a_decomposition {
            for j, _ := range b_decomposition {
                term := fmt.Sprintf("%d x %d", a_decomposition[i], b_decomposition[j])
                terms = append(terms, term)
            }
        }

        fmt.Println(strings.Join(terms, " + "))
    }
}

func getDecomposition(x int) []int {
    var x_decomposition []int
    position := 1

    for x > 0 {
        digit := x % 10
        
        if digit != 0 {
            x_decomposition = append([]int{digit * position}, x_decomposition...)
        }
    
        x /= 10
        position *= 10
    }

    return x_decomposition
}
