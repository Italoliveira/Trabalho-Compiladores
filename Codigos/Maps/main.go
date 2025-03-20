package main

import "fmt"

func exec() {

    nums := []int{1, 2, 3, 4, 5}
    nums = append(nums, 6)

    fmt.Println("Slice:", nums)

    pessoas := map[string]int{
        "Alice":  25,
        "Carlos": 30,
    }

    pessoas["Bruno"] = 28

    for nome, idade := range pessoas {
        fmt.Printf("%s tem %d anos.\n", nome, idade)
    }
}
