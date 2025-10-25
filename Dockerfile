FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory inside container 
RUN mkdir -p /app/pipeline

# Set the working directory
WORKDIR /app/pipeline

# Copy all project files into /app/pipeline/ in the container
COPY . /app/pipeline/

# Install pip dependencies
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn scikit-learn scipy requests

# Start an interactive bash shell when the container runs
CMD ["bash"]

