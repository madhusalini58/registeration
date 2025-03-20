# Use an official Python image as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file separately first
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a different port
EXPOSE 5000

# Define the command to run the app on port 5001
CMD ["python", "app.py", "--port=5000"]
