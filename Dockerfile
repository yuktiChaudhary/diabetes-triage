
# Using a reasonable size Docker contanier
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install requirements for python 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code 
COPY app/ ./app/
# This is required because main.py imports DiabetesFeatures from src.data
COPY src/ ./src/

# Copy model files
# COPY artifacts/ ./artifacts/ (This is wrong)
# the trained model is saved under models/ and the API expects that path
COPY models/ ./models/ 
ARG MODEL_VERSION=v0.1
ENV MODEL_VERSION=${MODEL_VERSION}

# API listens on port 80
EXPOSE 80

# Start API on port 80 inside Docker container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
