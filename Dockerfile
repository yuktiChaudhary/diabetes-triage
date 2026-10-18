
# Using a reasonable size Docker contanier
FROM python: 3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install requirements for python 
COPY requirements .txt .
RUN pip install --no-cache-dir -r requirements.tt

# Copy app code 
COPY app/ ./app/

# Copy model files
COPY artifacts/ ./artifacts/

# API listens on port 80
EXPOSE 80

# Start API on port 80 inside Docker container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
