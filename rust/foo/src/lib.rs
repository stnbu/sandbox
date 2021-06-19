extern crate web3;

// #[cfg(test)]
// mod tests {
//     use super::*;
//     fn it_works() {
//     }
// }


#[tokio::main]
async fn main() -> web3::Result<()> {
    let transport = web3::transports::Http::new("http://10.8.0.2:8545")?;
    let web3 = web3::Web3::new(transport);

    println!("Calling accounts.");
    let mut accounts = web3.eth().accounts().await?;
    println!("Accounts: {:?}", accounts);
    accounts.push("0xafe8d48DeFC7B96912C638C8900CB71dDB1acEC4".parse().unwrap());

    println!("Calling balance.");
    for account in accounts {
        let balance = web3.eth().balance(account, None).await?;
        println!("Balance of {:?}: {}", account, balance);
    }

    Ok(())
}
