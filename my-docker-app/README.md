# Dockerized Python Application

This project demonstrates a simple Python application running in a Docker environment with a web interface. It includes database operations, configuration management, and a basic web server.

## Project Structure

```
my-docker-app/
│
├── app/
│   ├── app.py
│   └── requirements.txt
├── config/
│   └── config.yaml
├── data/
│   └── .gitkeep
├── web/
│   └── index.html
├── Dockerfile
├── docker-compose.yml
└── init.sh
```

## Components and Execution Flow

1. **Docker Compose (`docker-compose.yml`)**
   - Entry point for running the entire application
   - Defines two services: `app` (Python application) and `web` (Nginx server)
   - Sets up volumes and network connections

2. **Dockerfile**
   - Defines how to build the Docker image for the Python application
   - Copies application files, installs dependencies, and sets up the entry point

3. **Initialization Script (`init.sh`)**
   - First script to run when the `app` container starts
   - Creates the SQLite database file
   - Starts the Python application

4. **Python Application (`app/app.py`)**
   - Main application logic
   - Loads configuration from `config.yaml`
   - Connects to SQLite database
   - Reads and writes data to `data.json`
   - Runs in a continuous loop, performing operations every 60 seconds

5. **Configuration (`config/config.yaml`)**
   - Contains application settings
   - Read by the Python application on startup

6. **Web Interface (`web/index.html`)**
   - Simple HTML page served by the Nginx web server
   - Accessible at `http://localhost:8080` when the application is running

## Execution Order and Process

1. When you run `docker-compose up`:
   - Docker Compose reads `docker-compose.yml`
   - Builds the `app` service using the `Dockerfile`
   - Pulls the Nginx image for the `web` service

2. The `app` container starts:
   - `init.sh` runs first
   - Creates `app.db` in the `/app/data` directory
   - Starts the Python application (`app.py`)

3. The Python application (`app.py`) executes:
   - Loads configuration from `config.yaml`
   - Ensures the database exists and is initialized
   - Reads `data.json` (creates it if it doesn't exist)
   - Updates `data.json` with the name from the configuration
   - Inserts a record into the SQLite database
   - Logs "Hello, {name}!" (visible in Docker logs)
   - Enters a loop, sleeping for 60 seconds between iterations

4. The `web` container starts:
   - Nginx server begins running
   - Serves `index.html` from the `web` directory

5. The application continues running until stopped with `docker-compose down`

## Key Points

- Data Persistence: The `data` directory is mounted as a volume, ensuring that `app.db` and `data.json` persist between container restarts.
- Configuration: `config.yaml` can be modified without rebuilding the Docker image, allowing for easy configuration changes.
- Logs: Application logs can be viewed using `docker-compose logs app`.
- Web Interface: A basic web page is accessible at `http://localhost:8080`.

## Running the Application

1. Ensure Docker and Docker Compose are installed on your system.
2. Navigate to the project directory containing `docker-compose.yml`.
3. Run `docker-compose up --build` to start the application.
4. Access the web interface at `http://localhost:8080`.
5. View application logs with `docker-compose logs app`.
6. Stop the application with `docker-compose down`.

This README provides an overview of how the application works and how its components interact. For more detailed information on each component, refer to the comments within individual files.