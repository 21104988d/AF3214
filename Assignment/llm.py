from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
import csv

def user_action():
    model = OllamaLLM(model="llama3.2")

    template = """
    You are an assistant of a bank to analyze what the client is going to do.
    Here are some historial conversations with the client: {chat_history}
    Here is the new conversation with the client: {new_conversation}
    Please analyze the new conversation and answer me the action of the client.
    You only need to answer with one word, choosing from:
    transaction: the client is going to do a transaction
    info: the client is going to adjust its contact information
    error: the clinet is going to do something else which is not trasaction or info
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    tg_messages = pd.read_csv("telegram_messages.csv")
    history = pd.read_csv("llm_history.csv")
    question = tg_messages.iloc[-1]['Message']

    result = chain.invoke({"chat_history": history,
                       "new_conversation": question})

    with open("llm_history.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if tg_messages.iloc[-1]['Receive ID'] not in history['Receive ID'].values:
            receive_id = tg_messages.iloc[-1]['Receive ID']
            text = question
            action = result
            writer.writerow([receive_id, text, action])
    
    return result

def extract_amount():
    model = OllamaLLM(model="llama3.2")

    template = """
    You are an assistant of to analyze the amount of the transaction.
    Here are some historial conversations with the client: {chat_history}
    Here is the new conversation with the client: {new_conversation}
    Please analyze the new conversation and answer me the amount of the transaction.
    You only need to answer with one word, which is the amount of the transaction.
    If the amount is not mentioned in the conversation, please answer me 100.
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    tg_messages = pd.read_csv("telegram_messages.csv")
    history = pd.read_csv("transaction_history.csv")
    question = tg_messages.iloc[-1]['Message']

    result = chain.invoke({"chat_history": history,
                           "new_conversation": question})
    
    return result

def extract_receiver():
    model = OllamaLLM(model="llama3.2")

    template = """
    You are an assistant of to analyze the receiver of the transaction.
    Here are some historial conversations with the client: {chat_history}
    Here is the new conversation with the client: {new_conversation}
    Here is the contact list of the client: {contact_name}
    Please analyze the new conversation match the exact receiver of the transaction.
    You only need to answer with one word.
    If the receiver is not in the contact list, please answer me error.
    If the receiver is in the contact list, please answer me the name of the receiver.
    You need to choose the name from the contact list.
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    tg_messages = pd.read_csv("telegram_messages.csv")
    history = pd.read_csv("transaction_history.csv")
    question = tg_messages.iloc[-1]['Message']
    receiver = pd.read_csv("contact.csv")
    name = receiver['Receiver'].tolist()

    result = chain.invoke({"chat_history": history,
                           "new_conversation": question,
                           "contact_name": name})
    
    if result != name:
        result = "error"
    
    return result