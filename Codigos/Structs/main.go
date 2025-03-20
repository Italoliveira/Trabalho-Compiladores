package main

import "fmt"

type Pessoa struct {
    Nome  string
    Idade int
}

func (p Pessoa) Apresentar() {
    fmt.Printf("Olá, meu nome é %s e eu tenho %d anos.\n", p.Nome, p.Idade)
}

func main() {
    p := Pessoa{"João", 30}
    p.Apresentar()
}
