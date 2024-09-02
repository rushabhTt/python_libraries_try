FROM python:3.12-slim

# This command sets the working directory inside the Docker container to /app. It’s like running cd /app in a regular terminal, so any subsequent commands will be executed from this directory.
WORKDIR /app

# This command copies the contents of your local app directory (on your host machine) into the /app directory inside the Docker container.
COPY app /app

# The RUN pip install --no-cache-dir -r requirements.txt command runs inside the container, where the requirements.txt file is located in the /app directory.
RUN pip install --no-cache-dir -r requirements.txt

# like running python app.py
CMD ["python", "app.py"]