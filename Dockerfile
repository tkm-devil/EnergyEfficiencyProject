# Use the official Python base image with Python 3.10
FROM python:3.10-slim-buster

# Set environment variable to ensure Python outputs everything directly to the console
ENV PYTHONUNBUFFERED 1

# Create a directory named /app inside the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to /app/requirements.txt inside the container
COPY requirements.txt /app/requirements.txt

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to /app inside the container
COPY . /app

# Expose the port on which your Flask application will run (replace 5000 with your specific port)
EXPOSE 5000

# Start the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "application:app"]