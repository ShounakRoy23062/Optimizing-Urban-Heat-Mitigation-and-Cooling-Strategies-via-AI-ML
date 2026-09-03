# Use official lightweight Python 3.11 image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first
# This helps Docker cache dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project into container
COPY . .

# Expose Flask application port
EXPOSE 5000

# Start Flask application when container runs
CMD ["python", "app.py"]