#!/bin/bash

# Check driver & Install CUDA
if ! command -v nvidia-smi &> /dev/null
then
    echo "You must first install an NVIDIA driver"
fi

PYTHON_VERSION=3.11

# Install python
if ! python3 --version 2>&1 | grep "$PYTHON_VERSION";
then
    echo "Installing Python 3.11"
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt-get update --fix-missing
    sudo apt-get install -y python$PYTHON_VERSION python$PYTHON_VERSION-distutils python$PYTHON_VERSION-dev
    sudo python$PYTHON_VERSION -m easy_install pip
else
    echo "Python installed"
fi

# Install ffmpeg & soundfile
sudo apt-get install -y ffmpeg libsndfile1

# Install Dependencies
python$PYTHON_VERSION -m pip install -r requirements.txt
echo "Successfully installed python packages"
echo "Install complete"
