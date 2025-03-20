package main

import (
	"fmt"
	"time"
)

func contar(canal chan string) {
    for i := 1; i <= 5; i++ {
        canal <- fmt.Sprintf("Contando: %d", i)
        time.Sleep(time.Second)
    }
    close(canal)
}

func main() {
    canal := make(chan string)
    go contar(canal)

    for msg := range canal {
        fmt.Println(msg)
    }
}
