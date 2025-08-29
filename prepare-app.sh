#!/bin/bash
echo "Preparing Task Manager app ..."
docker network create app-network 2>/dev/null || true
docker volume create db-data 2>/dev/null || true
docker compose build



