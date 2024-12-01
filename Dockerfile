FROM python:3.10.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Install FFmpeg and clean up APT cache
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Optional: ensures Python output is shown in Docker logs
ENV PYTHONUNBUFFERED=1

# Command to run your application
CMD ["python3", "main.py"]
