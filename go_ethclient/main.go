package main

import (
	"context"
	"fmt"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/ethclient"
	"math/big"
)

func main() {
	conn, err := ethclient.Dial("http://127.0.0.1:8545")
	if err != nil {
		fmt.Errorf("Failed to connect to the Ethereum client: %v", err)
	}

	ctx := context.Background()
	block, _ := conn.BlockByNumber(ctx, big.NewInt(123))
	fmt.Printf("block: %v\n", block)

	addr := common.HexToAddress("0xafe8d48DeFC7B96912C638C8900CB71dDB1acEC4")
	balance, _ := conn.BalanceAt(ctx, addr, nil)
	fmt.Printf("balance of addr: %v\n", balance)

	// tx := new(types.Transaction)
	// err = conn.SendTransaction(ctx, tx)

	progress, _ := conn.SyncProgress(ctx)
	fmt.Printf("progress: %v", progress)

	//fmt.Println(conn)
}
