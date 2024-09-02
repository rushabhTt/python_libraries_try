import yaml
import json
import logging
import sqlite3
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_config():
    try:
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
            logging.info("Configuration loaded successfully.")
            return config
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        return None

def read_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            logging.info("Data read successfully.")
            return data
    except Exception as e:
        logging.error(f"Error reading data: {e}")
        return None

def write_data(data):
    """Write data to a JSON file."""
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        logging.info("Data written successfully.")
    except Exception as e:
        logging.error(f"Error writing data: {e}")


def connect_db(db_path):
    """Connect to the SQLite database and initialize it."""
    try:
        conn = sqlite3.connect(db_path)
        logging.info("Connected to the database successfully.")
        cursor = conn.cursor()
        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        # Insert data into the table
        cursor.execute('''
            INSERT INTO users (name) VALUES (?)
        ''', (config['name'],))
        conn.commit()
        return conn
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        return None


def main():
    # Load configuration
    config = load_config()
    if not config:
        return

    # Read data
    data = read_data()
    if not data:
        data = {}

    # Update data
    data['name'] = config['name']

    # Write updated data
    write_data(data)

    # Connect to the database
    db_conn = connect_db(config['database']['path'])
    if db_conn:
        db_conn.close()

    # Print a greeting message
    print(f"Hello, {config['name']}!")


if __name__ == "__main__":
    main()

    while True:
        time.sleep(60)
