#!/bin/sh

token="DISCORD_TOKEN=ODQzODg2NDc5Nzk3NTE4MzM2.YKKYhw.3M4ZxOmE4Wl-IRCxL9YBPIC7IYE"

cd ~/Projects/NotionBuddy
if [[ $(git rev-parse HEAD) != $(git ls-remote $(git rev-parse --abbrev-ref @{u} | \sed 's/\// /g') | cut -f1) ]]
then
    git pull
    docker stop robocist/notion-buddy:latest
    docker build . -t robocist/notion-buddy:latest --build-arg "$token"
    docker run robocist/notion-buddy:latest
fi