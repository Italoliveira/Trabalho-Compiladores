package main

import "fmt"

type Forma interface {
    Area() float64
}

type Quadrado struct {
    Lado float64
}

func (q Quadrado) Area() float64 {
    return q.Lado * q.Lado
}

type Circulo struct {
    Raio float64
}

func (c Circulo) Area() float64 {
    return 3.14 * c.Raio * c.Raio
}

func main() {
    var f Forma = Quadrado{4}
    fmt.Println("Área do quadrado:", f.Area())

    f = Circulo{3}
    fmt.Println("Área do círculo:", f.Area())
}
