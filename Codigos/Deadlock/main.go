package main

import (
	"fmt"
	"sort"
	"sync"
	"time"
)

type Jogador struct {
	nome      string
	pontuacao int
	mutex     sync.Mutex
}

func incrementePontuacao(jogadores []*Jogador, incremento int, id int, wg *sync.WaitGroup) {
	defer wg.Done()

	sort.Slice(jogadores, func(i, j int) bool {
		return jogadores[i].nome < jogadores[j].nome
	})

	for _, jogador := range jogadores {
		fmt.Printf("Goroutine %d tentando travar %s\n", id, jogador.nome)
		jogador.mutex.Lock()
		fmt.Printf("Goroutine %d travou %s\n", id, jogador.nome)
		time.Sleep(1 * time.Second)
	}

	for _, jogador := range jogadores {
		jogador.pontuacao += incremento
	}

	for _, jogador := range jogadores {
		jogador.mutex.Unlock()
		fmt.Printf("Goroutine %d liberou %s\n", id, jogador.nome)
	}
}

func main() {
	jogador1 := &Jogador{nome: "Jogador1", pontuacao: 0}
	jogador2 := &Jogador{nome: "Jogador2", pontuacao: 0}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		incrementePontuacao([]*Jogador{jogador1, jogador2}, 1, 1, &wg)
		fmt.Println("Goroutine 1 concluída")
	}()

	go func() {
		time.Sleep(100 * time.Millisecond)
		incrementePontuacao([]*Jogador{jogador2, jogador1}, 1, 2, &wg)
		fmt.Println("Goroutine 2 concluída")
	}()

	wg.Wait()
	fmt.Println("Fim do programa")
}