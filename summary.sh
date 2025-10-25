#!/bin/bash
# Summary script for Docker pipeline
# Copies all results to host and cleans up the container

# define variables
CONTAINER_NAME="myappcontainer"
HOST_RESULTS_DIR="./results"

# create host results directory if it doesn’t exist
mkdir -p $HOST_RESULTS_DIR

# copy results from container to host
echo " copying results from container to host..."
docker cp ${CONTAINER_NAME}:/app/pipeline/data_raw.csv $HOST_RESULTS_DIR/ 2>/dev/null
docker cp ${CONTAINER_NAME}:/app/pipeline/data_preprocessed.csv $HOST_RESULTS_DIR/ 2>/dev/null
docker cp ${CONTAINER_NAME}:/app/pipeline/insight1.txt $HOST_RESULTS_DIR/ 2>/dev/null
docker cp ${CONTAINER_NAME}:/app/pipeline/insight2.txt $HOST_RESULTS_DIR/ 2>/dev/null
docker cp ${CONTAINER_NAME}:/app/pipeline/insight3.txt $HOST_RESULTS_DIR/ 2>/dev/null
docker cp ${CONTAINER_NAME}:/app/pipeline/summary_plot.png $HOST_RESULTS_DIR/ 2>/dev/null
docker cp ${CONTAINER_NAME}:/app/pipeline/clusters.txt $HOST_RESULTS_DIR/ 2>/dev/null

echo " All available results copied to: $HOST_RESULTS_DIR"

# Stop the container
echo "Stopping container..."
docker stop $CONTAINER_NAME

# Remove the container
echo "Removing container..."
docker rm $CONTAINER_NAME