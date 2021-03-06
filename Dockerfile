# For more information, please refer to https://aka.ms/vscode-docker-python
FROM arm32v7/python:3.8

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ARG DISCORD_TOKEN
ENV DISCORD_TOKEN=${DISCORD_TOKEN}

ARG HOST
ENV HOST=${HOST}

ARG USERNAME
ENV USERNAME=${USERNAME}

ARG PASSWORD
ENV PASSWORD=${PASSWORD}

ARG DB_NAME
ENV DB_NAME=${DB_NAME}

ARG PORT
ENV PORT=${PORT}

COPY . /app
WORKDIR /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "-u", "bot.py"]
