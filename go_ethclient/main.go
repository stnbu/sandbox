package main

import (
	"fmt"

	"github.com/ethereum/go-ethereum/ethclient"
)


func main() {
	conn, err := ethclient.Dial("http://127.0.0.1:8545")

	if err != nil {
		fmt.Errorf("Failed to connect to the Ethereum client: %v", err)
	}
	fmt.Println(conn)
}
