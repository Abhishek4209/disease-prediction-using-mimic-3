# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt setup.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (Flask default)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
