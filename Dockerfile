# Use an official Python image as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file separately first
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files


EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
