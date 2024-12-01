#!/bin/bash

#
# vast.ai on start script
#

tmux set-option -g mouse on
tmux set-option -g set-titles on
tmux set-option -g set-titles-string "Voice Cloning"

cd /app
python3 main.py &
tensorboard --logdir=/app/data/tensorboard

