#!/bin/sh

cd ~/Projects/Cadbury
if [[ $(git rev-parse HEAD) != $(git ls-remote $(git rev-parse --abbrev-ref @{u} | \sed 's/\// /g') | cut -f1) ]]
then
    git pull
    docker stop $(docker ps -a -q)
    docker build . -t robocist/cadbury:latest "${TOKEN}"
    docker run robocist/cadbury:latest
fi
