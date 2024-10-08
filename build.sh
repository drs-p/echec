#!/bin/sh
docker build --tag echec .
docker create --name echec -t echec
docker cp . echec:/echec
docker start echec
docker exec echec uvx tox run
docker exec echec uv build
docker cp echec:/echec/dist .
docker stop echec
docker rm echec
