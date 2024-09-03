import pika
import json
import time
import os
from faker import Faker

fake = Faker()

def generate_data():
    return {
        "timestamp": time.time(),
        "user_id": fake.uuid4(),
        "action": fake.random_element(elements=('login', 'logout', 'purchase', 'view')),
        "value": fake.random_number(digits=2)
    }

def main():
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue='raw_data')

    while True:
        data = generate_data()
        channel.basic_publish(exchange='', routing_key='raw_data', body=json.dumps(data))
        print(f"Sent: {data}")
        time.sleep(1)

if __name__ == "__main__":
    main()