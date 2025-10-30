from kafka import KafkaProducer
import json
import random
import time
import uuid

def generate_transaction():
    transaction = {
        'id': str(uuid.uuid4()),
        'amount': random.randint(10, 1000),
        'account_number': random.randint(100000, 999999),
        'timestamp': int(time.time())
    }
    return transaction

def producer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        transaction = generate_transaction()
        producer.send('transactions', value=transaction)
        print(f"Sent transaction: {transaction}")
        time.sleep(3)

if __name__ == "__main__":
    producer()

