#!/bin/sh

docker build -t flask-container:latest .
docker run -d -p 5000:5000 flask-container