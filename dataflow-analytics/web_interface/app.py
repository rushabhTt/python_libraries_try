from flask import Flask, render_template, jsonify
import requests
import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

config = load_config()
api_gateway_config = config['api_gateway']
web_interface_config = config['web_interface']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    try:
        api_url = f"http://{api_gateway_config['host']}:{api_gateway_config['port']}/api/data"
        response = requests.get(api_url)
        data = response.json()
        return render_template('dashboard.html', data=data)
    except Exception as e:
        return jsonify({"error": str(e), "api_url": api_url}), 500

@app.route('/debug')
def debug():
    return jsonify({
        "config": config,
        "api_gateway_url": f"http://{api_gateway_config['host']}:{api_gateway_config['port']}/api/data"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=web_interface_config['port'], debug=True)