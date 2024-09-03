from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

storage_service_host = os.environ.get('STORAGE_SERVICE_HOST', 'localhost')

@app.route('/api/data', methods=['GET'])
def get_data():
    response = requests.get(f'http://{storage_service_host}:5000/data')
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)