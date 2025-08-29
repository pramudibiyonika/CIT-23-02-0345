#!/bin/bash
echo "Removing Task Manager app ..."
docker compose down -v --rmi all
docker network rm app-network 2>/dev/null || true
docker volume rm db-data 2>/dev/null || true

