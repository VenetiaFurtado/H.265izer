FROM python:3.10-slim

# Install ffmpeg
RUN apt update && apt install -y ffmpeg && apt clean

WORKDIR /app
COPY main.py config.yaml /app/
RUN pip install pyyaml

CMD ["python", "main.py"]
