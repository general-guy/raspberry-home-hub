#!/bin/bash

RSYNC_SOURCE="./"
RSYNC_TARGET="geraldo-server@raspberry-home-hub.local:/opt/rhh/"

rsync -avz --delete \
    --exclude '.git' \
    --exclude '__pycache__' \
    --exclude '.venv' \
    --exclude '.pytest_cache' \
    "$RSYNC_SOURCE" \
    "$RSYNC_TARGET"