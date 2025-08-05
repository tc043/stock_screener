# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=10000", "--server.address=0.0.0.0"]
