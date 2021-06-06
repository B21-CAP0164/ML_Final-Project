# Use Python37
FROM python:3.7-slim
# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt
# Set the WORKDIR to be the folder
COPY . /app
# Expose port 5000
EXPOSE 5000
ENV PORT 5000
WORKDIR /app
# Use gunicorn as the entrypoint
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 0 deploy:app