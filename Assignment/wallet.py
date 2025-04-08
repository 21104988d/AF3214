from web3 import Web3

def send_tran(amount):
    web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/011ab8a31fd24d838e4f3177a99fd447"))

    sender = "0x7EA89134469701cCC5BD7CD5f8c5a54207bc6257"
    receiver = "0x7cB9296519729521e51c9C5d1CB54A1C90BC6d02"

    key = "300dff190a719daf431ec5d6abb5ed6beac9f93d471595b04993d470a556cf15"

    sender_address = web3.to_checksum_address(sender)
    receiver_address = web3.to_checksum_address(receiver)

    nonce = web3.eth.get_transaction_count(sender_address)
    gas_price = web3.eth.gas_price
    value = web3.to_wei(amount / 1000000000000000000, "ether")

    tx = {
    "to": receiver_address,
    "value": value,
    "gas": 21000,
    "gasPrice": gas_price,
    "nonce": nonce,
    "chainId": 11155111,
    }

    signed_tx = web3.eth.account.sign_transaction(tx, key)
    tx_transaction = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    return web3.to_hex(tx_transaction), amount

def balance():
    web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/011ab8a31fd24d838e4f3177a99fd447"))

    address = "0x7EA89134469701cCC5BD7CD5f8c5a54207bc6257"
    balance = web3.eth.get_balance(address)
    
    return web3.from_wei(balance, "ether")