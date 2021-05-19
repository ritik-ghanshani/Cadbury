#!/bin/sh

cd ~/Projects/NotionBuddy
if [[ $(git rev-parse HEAD) != $(git ls-remote $(git rev-parse --abbrev-ref @{u} | \sed 's/\// /g') | cut -f1) ]]
then
    git pull
    docker stop robocist/notion-buddy:latest
    echo "${TOKEN}"
    docker build . -t robocist/notion-buddy:latest --build-arg "${TOKEN}"
    docker run robocist/notion-buddy:latest
fi