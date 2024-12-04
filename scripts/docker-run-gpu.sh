#!/bin/sh

docker run --user=$UID --gpus all -p 80:5000 -v$(pwd)/data:/app/data bitplane1/voice-cloning-app:nvidia
