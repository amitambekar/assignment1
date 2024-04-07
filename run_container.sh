#!/bin/bash

# Build the Docker image
docker-compose build

# Run the Docker container in detached mode
docker-compose up -d
