from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

mongodb_host = os.environ.get('MONGODB_HOST', 'localhost')
client = MongoClient(f'mongodb://{mongodb_host}:27017/')
db = client['analytics_db']
collection = db['processed_data']

@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}).sort('timestamp', -1).limit(100))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)