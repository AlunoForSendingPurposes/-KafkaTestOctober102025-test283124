from kafka import KafkaConsumer
import json
import sqlite3
import time

# Setup SQLite database
conn = sqlite3.connect('transactions.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (id TEXT, amount INTEGER, account_number INTEGER, timestamp INTEGER)''')

def detect_fraud(transaction):
    # Example rule: If transaction amount is greater than 500, flag as fraud
    if transaction['amount'] > 500:
        print(f"Fraud detected! Transaction: {transaction}")
        return True
    return False

def store_transaction(transaction):
    c.execute("INSERT INTO transactions (id, amount, account_number, timestamp) VALUES (?, ?, ?, ?)",
              (transaction['id'], transaction['amount'], transaction['account_number'], transaction['timestamp']))
    conn.commit()

def consumer():
    consumer = KafkaConsumer('transactions', bootstrap_servers='localhost:9092',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        transaction = message.value
        print(f"Received transaction: {transaction}")
        
        if detect_fraud(transaction):
            # Example alert: print fraud to the console
            print(f"ALERT: Fraud detected in transaction ID: {transaction['id']}")
        
        store_transaction(transaction)

if __name__ == "__main__":
    consumer()

