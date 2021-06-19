use ethers::contract::Contract;

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
	let x = myfoo();
	assert_eq!(x, "xxx");
    }
}

pub fn myfoo() -> String {
    let contract = Contract::new(address.into(), BALANCESHEET_ABI.clone(), client);
}

// use ethers::{
//     contract::{
//         builders::{ContractCall, Event},
//         Contract, Lazy,
//     },
//     core::{
//         abi::{parse_abi, Abi, Detokenize, InvalidOutputType, Token, Tokenizable},
//         types::*,
//     },
//     providers::Middleware,
// };
