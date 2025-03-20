package main

import "fmt"

func main() {
    x := 10

    if x > 5 {
        fmt.Println("x é maior que 5")
    } else {
        fmt.Println("x é menor ou igual a 5")
    }

    switch x {
    case 10:
        fmt.Println("x é 10")
    default:
        fmt.Println("x não é 10")
    }

    for i := 0; i < 5; i++ {
        fmt.Println("Loop:", i)
    }
}
