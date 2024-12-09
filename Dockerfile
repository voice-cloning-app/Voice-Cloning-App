FROM pytorch/pytorch:2.5.1-cuda11.8-cudnn9-runtime

# Lib dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg \
                       build-essential \
                       htop
#    rm -rf /var/lib/apt/lists/*

# Setup
WORKDIR /app
COPY requirements.txt /app
# Python dependencies
RUN pip install -r requirements.txt
#    pip cache purge

# Application files
COPY application/ /app/application
COPY dataset/ /app/dataset
COPY training/ /app/training
COPY synthesis/ /app/synthesis
COPY main.py /app

# For vast.ai deployments
COPY scripts/onstart.sh /app/onstart.sh

# Start app
CMD [ "python3", "main.py" ]
