import yaml
import json
import logging
import sqlite3
import time
import os
import sys

# Update logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stdout)

def load_config():
    # First, check if the CONFIG_PATH environment variable is set. If it is, use its value (which, in your case, is /app/config/config.yaml as specified in the docker-compose.yml file).
    # If the CONFIG_PATH environment variable is not set, fall back to the default value 'config/config.yaml'.
    config_path = os.environ.get('CONFIG_PATH', 'config/config.yaml')
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        logging.info("Configuration loaded successfully.")
        return config
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        return None

def read_data():
    try:
        with open("data/data.json", "r") as file:
            data = json.load(file)
        logging.info("Data read successfully.")
        return data
    except FileNotFoundError:
        logging.info("data.json not found. Creating a new one.")
        return {}
    except Exception as e:
        logging.error(f"Error reading data: {e}")
        return None

def write_data(data):
    try:
        with open("data/data.json", "w") as file:
            json.dump(data, file, indent=4)
        logging.info("Data written successfully.")
    except Exception as e:
        logging.error(f"Error writing data: {e}")

def connect_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        logging.info("Connected to the database successfully.")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.commit()
        return conn
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        return None

def main():
    config = load_config()
    if not config:
        return

    data = read_data()
    if data is None:
        return

    data["name"] = config["name"]
    write_data(data)

    db_conn = connect_db(config["database"]["path"])
    if db_conn:
        cursor = db_conn.cursor()
        cursor.execute('INSERT INTO users (name) VALUES (?)', (config["name"],))
        db_conn.commit()
        db_conn.close()

    logging.info(f"Hello, {config['name']}!")

if __name__ == "__main__":
    main()
    while True:
        time.sleep(60)