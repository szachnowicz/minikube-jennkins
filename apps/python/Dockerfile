# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/app.py .

# Expose the application's port
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]