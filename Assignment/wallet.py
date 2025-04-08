from web3 import Web3
import csv
import pandas as pd

def send_tran(amount, receiver_name):
    web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/011ab8a31fd24d838e4f3177a99fd447"))

    wallet = pd.read_csv("user_key.csv")
    user_wallet = wallet['Wallet'].iloc[0]
    user_private_key = wallet['Private Key'].iloc[0]
    contact = pd.read_csv("contact.csv")
    receiver_wallet = contact.loc[contact['Receiver'] == receiver_name, 'Wallet'].iloc[0]

    sender = user_wallet
    receiver = receiver_wallet

    key = user_private_key

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
    history = pd.read_csv("transaction_history.csv")
    tx_transaction = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

    tg_messages = pd.read_csv("telegram_messages.csv")
    with open("transaction_history.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if tg_messages.iloc[-1]['Receive ID'] not in history['Receive ID'].values:
            receive_id = tg_messages.iloc[-1]['Receive ID']
            text = tg_messages.iloc[-1]['Message']
            amount_send = amount
            receiver_name_temp = receiver_name
            hex = web3.to_hex(tx_transaction)
            writer.writerow([receive_id, text, amount_send, receiver_name_temp, hex])
    
    return amount

def get_balance():
    web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/011ab8a31fd24d838e4f3177a99fd447"))

    address = "0x7EA89134469701cCC5BD7CD5f8c5a54207bc6257"
    balance = web3.eth.get_balance(address)
    
    return web3.from_wei(balance, "ether")