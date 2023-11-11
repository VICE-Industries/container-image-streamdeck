#!/usr/bin/env bash

git clone https://github.com/thiagoralves/OpenPLC_v3
docker buildx build --platform linux/amd64 -t ghcr.io/vice-industries/openplc:latest OpenPLC_v3
