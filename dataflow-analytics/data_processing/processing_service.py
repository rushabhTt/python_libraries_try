import pika
import json
import os
from pymongo import MongoClient

def process_data(data):
    # Simple processing: add a 'processed' flag
    data['processed'] = True
    return data

def main():
    rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
    mongodb_host = os.environ.get('MONGODB_HOST', 'localhost')

    # RabbitMQ connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue='raw_data')

    # MongoDB connection
    client = MongoClient(f'mongodb://{mongodb_host}:27017/')
    db = client['analytics_db']
    collection = db['processed_data']

    def callback(ch, method, properties, body):
        data = json.loads(body)
        processed_data = process_data(data)
        collection.insert_one(processed_data)
        print(f"Processed and stored: {processed_data}")

    channel.basic_consume(queue='raw_data', on_message_callback=callback, auto_ack=True)
    print('Data Processing Service is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()