# Use an official Python runtime as a parent image
FROM python:3.13-slim

ENV TZ="Asia/Kolkata"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional, not necessary for Telegram bot but for debugging)
EXPOSE 8080

# Run the bot when the container starts
ENTRYPOINT ["python", "main.py"]
