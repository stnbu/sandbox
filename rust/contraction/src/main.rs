use ethers::{
    abi::Abi,
    types::Address,
    contract::Contract,
    providers::{Provider, Http},
};
use std::convert::TryFrom;

#[tokio::main]
async fn main() {
    // FIXME: It looks like addresses are not being checksummed (case ignored).
    let contract_address = "915AB0674D678E42E97eC3187d8DE5953b95C1DD".parse::<Address>().unwrap();
    let abi: Abi = serde_json::from_str(r#"[{"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "_address", "type": "address"}], "name": "AddressAbandoned", "type": "event"}, {"inputs": [{"internalType": "address", "name": "_address", "type": "address"}], "name": "abandonAddress", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_address", "type": "address"}], "name": "isAbandoned", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}]"#).unwrap();
    let client = Provider::<Http>::try_from("http://localhost:8545").unwrap();
    let contract = Contract::new(contract_address, abi, client);
    let check_address = "0xafe8d48DeFC7B96912C638C8900CB71dDB1acEC4".parse::<Address>().unwrap();
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
}

