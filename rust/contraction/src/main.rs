
#[tokio::main]
async fn main() {
    use ethers::{
	abi::Abi,
	utils::Solc,
	types::{Address, H256},
	contract::Contract,
	providers::{Provider, Http},
	signers::Wallet,
    };
    use std::convert::TryFrom;

    // this is a fake address used just for this example
    let address = "915AB0674D678E42E97eC3187d8DE5953b95C1DD".parse::<Address>().unwrap();
    //let address = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee".parse::<Address>().unwrap();

    // (ugly way to write the ABI inline, you can otherwise read it from a file)
    let abi: Abi = serde_json::from_str(r#"[{"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "_address", "type": "address"}], "name": "AddressAbandoned", "type": "event"}, {"inputs": [{"internalType": "address", "name": "_address", "type": "address"}], "name": "abandonAddress", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_address", "type": "address"}], "name": "isAbandoned", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}]"#).unwrap();

    // connect to the network
    let client = Provider::<Http>::try_from("http://localhost:8545").unwrap();

    // create the contract object at the address
    let contract = Contract::new(address, abi, client);

    println!("contract: {:?}", contract);

    let check_address = "0xafe8d48DeFC7B96912C638C8900CB71dDB1acEC4".parse::<Address>().unwrap();

    // Calling constant methods is done by calling `call()` on the method builder.
    // (if the function takes no arguments, then you must use `()` as the argument)
    let is_abandoned: bool = contract
	.method::<_, bool>("isAbandoned", check_address)
	.unwrap()
	.call()
	.await
	.unwrap();

    if is_abandoned {
	println!("IS abandoned: {:?}", check_address);
    } else {
	println!("IS NOT abandoned: {:?}", check_address);
    }

    // // Non-constant methods are executed via the `send()` call on the method builder.
    // let call = contract
    // 	.method::<_, H256>("setValue", "hi".to_owned())?;
    // let pending_tx = call.send().await?;

    // // `await`ing on the pending transaction resolves to a transaction receipt
    // let receipt = pending_tx.confirmations(6).await?;
}
